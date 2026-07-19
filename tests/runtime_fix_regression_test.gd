extends SceneTree

var failures: Array[String] = []
var checks := 0


func _init() -> void:
	call_deferred("run_suite")


func expect(condition: bool, message: String) -> void:
	checks += 1
	if not condition:
		failures.append(message)


func key_event(code: Key, pressed := true) -> InputEventKey:
	var event := InputEventKey.new()
	event.keycode = code
	event.physical_keycode = code
	event.pressed = pressed
	return event


func run_suite() -> void:
	var main = load("res://scenes/Main.tscn").instantiate()
	root.add_child(main)
	await process_frame
	main.persistence_enabled = false
	main.audio_enabled = false
	main.title_open = false
	main.dialogue_open = false
	main.pause_open = false
	main.settings_open = false
	main.zone = "kallipolis"

	# Graphics application keeps one stable logical canvas and closes the pause
	# stack after Apply, so the user immediately sees the selected display mode.
	main.display_mode_index = 2
	main.resolution_index = 3
	main.pause_open = true
	main.settings_open = true
	main.graphics_dirty = true
	main.confirm_graphics_changes()
	expect(root.content_scale_size == main.BASE_VIEWPORT_SIZE, "graphics apply changed the logical 960x540 canvas")
	expect(not main.settings_open and not main.pause_open, "Apply left the graphics or pause menu open")
	expect(not main.graphics_dirty, "Apply left graphics marked as pending")
	expect("resolução atual do monitor" in main.notice, "fullscreen feedback still claimed the selected window resolution")
	main.notice_time = 0.0

	# Hidden legacy TileMaps must no longer be constructed during startup.
	expect(main.get_node("World/Ground").tile_set == null, "hidden Kallipolis TileMap was still rebuilt")
	expect(main.get_node("World/AgoraGround").tile_set == null, "hidden Agora TileMap was still rebuilt")
	expect(main.get_node("World/LightLayer").get_child_count() == 0, "hidden light occluders were still created")

	# The 1254px walk sheet must be split on integer boundaries. Fractional source
	# rectangles caused consecutive poses to sample half pixels and visibly jump.
	expect(main.ivo_frame_sources.size() == 16, "walk sheet did not create sixteen frame regions")
	expect(main.ivo_frame_foot_anchors.size() == 16, "walk sheet did not create sixteen foot anchors")
	for source in main.ivo_frame_sources:
		expect(is_equal_approx(source.position.x, roundf(source.position.x)), "walk frame starts on a fractional X coordinate")
		expect(is_equal_approx(source.position.y, roundf(source.position.y)), "walk frame starts on a fractional Y coordinate")
		expect(is_equal_approx(source.size.x, roundf(source.size.x)), "walk frame has a fractional width")
		expect(is_equal_approx(source.size.y, roundf(source.size.y)), "walk frame has a fractional height")
	for foot_anchor in main.ivo_frame_foot_anchors:
		expect(foot_anchor >= main.IVO_WALK_DRAW_SIZE.y * 0.72 and foot_anchor <= main.IVO_WALK_DRAW_SIZE.y, "walk frame foot anchor escaped the sprite bounds")

	# A one-second render hitch must not move the player as if a full second of
	# input had been rendered in one frame.
	main.player = Vector2(600, 400)
	main.player_velocity = Vector2.ZERO
	main.tap_move_time = 0.0
	var before_hitch: Vector2 = main.player
	Input.action_press("move_right")
	main._process(1.0)
	Input.action_release("move_right")
	expect(main.player.x > before_hitch.x, "clamped hitch frame discarded movement completely")
	expect(main.player.distance_to(before_hitch) < 6.0, "render hitch still teleported the player")

	# A short tap remains responsive, but releasing it removes the airborne glide.
	main.player_velocity = Vector2.ZERO
	main._unhandled_input(key_event(KEY_D))
	expect(main.tap_move_time > 0.0 and main.tap_move_time <= main.SHORT_TAP_BUFFER + 0.001, "movement tap retained the old long buffer")
	main._unhandled_input(key_event(KEY_D, false))
	expect(main.tap_move_time == 0.0, "movement release did not clear the short-tap buffer")

	# Opening a screen must survive the same process frame that received the key.
	main._unhandled_input(key_event(KEY_I))
	expect(main.inventory_open, "inventory did not open")
	main._process(0.016)
	expect(main.inventory_open, "inventory closed itself in the opening frame")
	main._unhandled_input(key_event(KEY_I))
	expect(not main.inventory_open, "inventory did not close on the second key press")

	main._unhandled_input(key_event(KEY_M))
	expect(main.map_open, "map did not open")
	main._process(0.016)
	expect(main.map_open, "map closed itself in the opening frame")
	main._unhandled_input(key_event(KEY_M))
	expect(not main.map_open, "map did not close on the second key press")

	main._unhandled_input(key_event(KEY_J))
	expect(main.gallery_open, "gallery did not open")
	main._process(0.016)
	expect(main.gallery_open, "gallery closed itself in the opening frame")
	main._unhandled_input(key_event(KEY_J))
	expect(not main.gallery_open, "gallery did not close on the second key press")

	# The interaction that starts a battle must not also execute the first attack.
	main.zone = "kallipolis"
	main.quest_stage = 4
	main.player = Vector2(main.npcs[3]["position"])
	main.transition_cooldown = 0.0
	main._unhandled_input(key_event(KEY_E))
	expect(main.battle_open, "collector interaction did not start battle")
	expect(main.enemy_health == main.enemy_max_health, "battle-opening E press also attacked")
	main._process(0.016)
	expect(main.enemy_health == main.enemy_max_health, "battle attacked from process polling")
	main._unhandled_input(key_event(KEY_E))
	expect(main.enemy_health < main.enemy_max_health, "next E press did not execute the selected battle action")

	# Lethal damage now produces a real defeat state and a safe retry position.
	main.health = 1
	main.enemy_turn(99)
	expect(not main.battle_open, "lethal damage did not end the battle")
	expect(main.health == main.max_health, "defeat did not restore the retry health")
	expect(main.dialogue_open, "defeat feedback dialogue did not open")
	expect(main.player.distance_to(Vector2(main.npcs[3]["position"])) > main.INTERACTION_DISTANCE, "defeat respawn stayed inside the collector trigger")
	main.close_dialogue()

	# Re-examining the completed cistern door must not farm affinity.
	main.zone = "cistern"
	main.quest_stage = 9
	main.relics = 3
	main.cistern_shards = [true, true, true]
	main.player = main.cistern_door_position
	main.transition_cooldown = 0.0
	var affinity_before: int = main.ariane_affinity
	main.try_interact()
	expect(main.ariane_affinity == affinity_before, "completed cistern door awarded repeated affinity")
	expect(main.dialogue_open, "completed cistern door did not provide stable feedback")
	main.close_dialogue()

	# Pixel-crisp and HD modes must select matching water samplers.
	main.zone = "kallipolis"
	main.title_open = false
	main.dialogue_open = false
	main.water_effects_enabled = true
	main.scale_mode_index = 0
	main.sync_water_post_effect()
	var material := main.get_node("WaterPostFX").material as ShaderMaterial
	expect(material.shader.resource_path.ends_with("water_postprocess_nearest.gdshader"), "crisp mode kept the linear water shader")
	main.scale_mode_index = 1
	main.sync_water_post_effect()
	expect(material.shader.resource_path.ends_with("water_postprocess.gdshader"), "HD mode did not restore the linear water shader")

	for child in main.get_children():
		if child is AudioStreamPlayer:
			child.stop()
			child.stream = null
	main.queue_free()
	main = null
	await process_frame
	await process_frame

	if failures.is_empty():
		print("RUNTIME FIX REGRESSION: %d checks passed" % checks)
		quit(0)
	else:
		for failure in failures:
			push_error(failure)
		print("RUNTIME FIX REGRESSION: %d failure(s)" % failures.size())
		quit(1)