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
	main.title_open = false
	main.dialogue_open = false
	main.zone = "kallipolis"
	main.title_open = true
	main._unhandled_input(key_event(KEY_E))
	expect(not main.title_open, "a short E press did not leave the title screen")

	# Movement key events must never apply a second hidden step.
	main.player = Vector2(600, 400)
	var before_tap: Vector2 = main.player
	main._unhandled_input(key_event(KEY_D))
	expect(main.player == before_tap, "movement tap was applied twice outside _process")
	expect(main.tap_move_direction == Vector2.RIGHT and main.tap_move_time > 0.0, "short movement tap was not buffered")
	main.try_move_player(Vector2(12, 0))
	expect(main.player.x > before_tap.x, "continuous movement failed on walkable ground")
	main.player = Vector2(300, 400)
	var previous_x: float = main.player.x
	var moved_forward := false
	Input.action_press("move_right")
	for frame in range(6):
		await process_frame
		expect(main.player.x >= previous_x, "held movement reversed or teleported backward")
		moved_forward = moved_forward or main.player.x > previous_x
		previous_x = main.player.x
	Input.action_release("move_right")
	expect(moved_forward, "held movement never advanced the player")
	expect(main.cardinal_facing(Vector2.UP) == Vector2.UP, "up input did not select the back-facing row")
	expect(main.cardinal_facing(Vector2.DOWN) == Vector2.DOWN, "down input did not select the front-facing row")
	expect(main.cardinal_facing(Vector2.LEFT) == Vector2.LEFT, "left input did not select the left-facing row")
	expect(main.cardinal_facing(Vector2.RIGHT) == Vector2.RIGHT, "right input did not select the right-facing row")

	# Water and fountain boundaries are solid.
	main.zone = "kallipolis"
	expect(not main.can_walk_to(Vector2(480, 500)), "central sea accepted the player")
	expect(not main.can_walk_to(Vector2(480, 374)), "fountain accepted the player")
	expect(main.can_walk_to(main.FOUNTAIN_CENTER + Vector2(48, 0)), "fountain collision is still wider than the visible basin")
	expect(main.can_walk_to(Vector2(150, 520)), "western pier became non-walkable")
	main.player = main.FOUNTAIN_CENTER - Vector2(62, 0)
	main.try_move_player(Vector2(145, 0))
	expect(main.player.x < main.FOUNTAIN_CENTER.x, "swept movement tunneled through the fountain")
	expect(main.can_walk_to(main.player), "fountain collision left the player in an invalid point")
	expect(main.has_node("WaterPostFX"), "water post-processing layer is missing")
	expect(main.WAYFINDING_SIGNS != null and main.FOUNTAIN_FX_SHEET != null, "new environmental animation assets failed to load")
	var water_before: float = main.water_phase
	main._process(0.2)
	expect(main.water_phase > water_before, "water animation phase did not advance")

	# Resident routes use valid art cells and real multi-point paths.
	var mikon: Dictionary = {}
	for actor in main.ambient_actors:
		if actor["name"] == "Mikon":
			mikon = actor
			break
	expect(not mikon.is_empty(), "Mikon is missing from the resident roster")
	expect(Vector2i(mikon.get("slot", Vector2i(3, 1))) != Vector2i(3, 1), "Mikon still points at the empty sprite cell")
	expect(Array(mikon.get("points", [])).size() >= 4, "Mikon still uses a one-axis ping-pong route")
	for actor in main.ambient_actors:
		main.zone = String(actor["zone"])
		for route_point in Array(actor["points"]):
			expect(main.can_walk_to(Vector2(route_point)), "%s has a route point outside walkable ground" % actor["name"])
	main.zone = "kallipolis"

	# Entering the inn must spawn away from the exit and E must page/close dialogue.
	main.player = main.inn_door_position
	main.transition_cooldown = 0.0
	main.try_interact()
	expect(main.zone == "inn", "inn entrance did not change zone")
	expect(main.player.distance_to(main.inn_exit_position) > main.INTERACTION_DISTANCE, "inn entrance spawned on exit trigger")
	expect(main.can_walk_to(main.player), "inn entrance spawned inside furniture")
	expect(main.dialogue_open, "inn intro dialogue did not open")
	main._unhandled_input(key_event(KEY_E))
	expect(main.dialogue_open and main.dialogue_page == 1, "E did not advance the inn dialogue page")
	main._unhandled_input(key_event(KEY_E))
	expect(not main.dialogue_open, "E did not close the final inn dialogue page")
	expect(main.zone == "inn", "closing dialogue immediately ejected the player from the inn")
	main.quest_stage = 0
	var inn_objective: Dictionary = main.objective_target_data()
	expect(String(inn_objective.get("label", "")) == "Lysandra", "inside the inn, the objective did not point to Lysandra")
	main.player = main.inn_exit_position
	main.transition_cooldown = 0.0
	main.try_interact()
	expect(main.zone == "kallipolis", "inn exit did not return to Kallipolis")
	expect(main.player.distance_to(main.inn_door_position) >= main.INTERACTION_DISTANCE, "inn exit spawned inside the entrance trigger")

	# Wayfinding must always name the next landmark in the opening route.
	main.zone = "kallipolis"
	main.quest_stage = 0
	expect(String(main.objective_target_data().get("label", "")) == "Pensão dos Degraus", "opening objective does not identify the inn")
	main.quest_stage = 1
	expect(String(main.objective_target_data().get("label", "")) == "Ágora das Colunas", "second objective does not identify the Agora")
	main.player = main.agora_gate_position
	main.transition_cooldown = 0.0
	main.try_interact()
	expect(main.zone == "agora" and main.can_walk_to(main.player), "Agora entrance did not use a walkable spawn")
	main.close_dialogue()
	main.quest_stage = 9
	main.player = main.agora_route_position
	main.transition_cooldown = 0.0
	main.try_interact()
	expect(main.zone == "nereu" and main.can_walk_to(main.player), "ferry did not reach Nereu at a walkable spawn")
	expect(main.quest_text() == "Fale com Nerissa em Nereu", "Nereu kept showing the obsolete ferry instruction")
	main.close_dialogue()
	main.player = main.nereu_exit_position
	main.transition_cooldown = 0.0
	main.try_interact()
	expect(main.zone == "agora", "Nereu ferry did not return to the Agora")
	expect(main.player.distance_to(main.agora_route_position) >= main.INTERACTION_DISTANCE, "ferry return spawned inside its own trigger")
	main.zone = "kallipolis"
	main.quest_stage = 5
	main.player = main.cistern_gate_position
	main.transition_cooldown = 0.0
	main.try_interact()
	expect(main.zone == "cistern" and main.can_walk_to(main.player), "cistern entrance did not use a walkable spawn")
	main.close_dialogue()
	main.player = main.cistern_exit_position
	main.transition_cooldown = 0.0
	main.try_interact()
	expect(main.zone == "kallipolis", "cistern exit did not return to Kallipolis")
	expect(main.player.distance_to(main.cistern_gate_position) >= main.INTERACTION_DISTANCE, "cistern exit spawned inside its own trigger")

	# Ariane's first exchange must reach its choice and advance the quest.
	main.zone = "kallipolis"
	main.quest_stage = 3
	main.talk_to("ariane")
	expect(main.dialogue_open and main.dialogue_page == 0, "Ariane dialogue did not start")
	main._unhandled_input(key_event(KEY_E))
	expect(main.dialogue_page == 1, "Ariane dialogue stayed on the first sentence")
	main._unhandled_input(key_event(KEY_E))
	expect(main.quest_stage == 4, "Ariane choice did not advance quest to the Collector")

	# Story NPCs keep priority when an ambient resident walks nearby.
	main.close_dialogue()
	main.zone = "agora"
	main.quest_stage = 1
	main.player = main.agora_polemon_position
	main.transition_cooldown = 0.0
	main.try_interact()
	expect(main.dialogue_action == "polemon_job", "ambient resident stole Pólemon's quest interaction")
	expect("Pólemon" in String(main.interaction_prompt_data().get("label", "")), "interaction prompt did not prioritize Pólemon")
	main.close_dialogue()

	# Graphics changes are pending until Apply and Cancel restores the snapshot.
	main.begin_graphics_settings()
	var old_resolution: int = main.resolution_index
	main.settings_selection = 1
	main.change_graphics_setting(1)
	expect(main.graphics_dirty, "graphics menu did not mark pending changes")
	expect(main.resolution_index != old_resolution or main.RESOLUTION_OPTIONS.size() == 1, "resolution selection did not change")
	main.cancel_graphics_changes()
	expect(main.resolution_index == old_resolution, "Cancel did not restore the previous resolution")
	main.begin_graphics_settings()
	main.settings_selection = 1
	main.change_graphics_setting(1)
	main.settings_selection = 8
	main.pause_open = true
	main._unhandled_input(key_event(KEY_E))
	expect(not main.settings_open and not main.graphics_dirty, "Apply did not commit and close graphics settings")

	# Release playback handles before the standalone headless tree exits. Without
	# this, Godot reports false-positive audio leaks even though gameplay passed.
	for child in main.get_children():
		if child is AudioStreamPlayer:
			child.stop()
			child.stream = null
	main.queue_free()
	main = null
	await process_frame
	await process_frame
	if failures.is_empty():
		print("REGRESSION SUITE: %d checks passed" % checks)
		quit(0)
	else:
		for failure in failures:
			push_error(failure)
		print("REGRESSION SUITE: %d failure(s)" % failures.size())
		quit(1)
