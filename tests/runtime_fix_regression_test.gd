extends SceneTree

var failures: Array[String] = []
var checks := 0


func _init() -> void:
	call_deferred("run_suite")


func expect(condition: bool, message: String) -> void:
	checks += 1
	if not condition:
		failures.append(message)


func key_event(code: Key) -> InputEventKey:
	var event := InputEventKey.new()
	event.keycode = code
	event.physical_keycode = code
	event.pressed = true
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

	# Hidden legacy TileMaps must no longer be constructed during startup.
	expect(main.get_node("World/Ground").tile_set == null, "hidden Kallipolis TileMap was still rebuilt")
	expect(main.get_node("World/AgoraGround").tile_set == null, "hidden Agora TileMap was still rebuilt")
	expect(main.get_node("World/LightLayer").get_child_count() == 0, "hidden light occluders were still created")

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
