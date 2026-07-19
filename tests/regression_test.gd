extends SceneTree

var failures: Array[String] = []


func _init() -> void:
	call_deferred("run_suite")


func expect(condition: bool, message: String) -> void:
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

	# Movement key events must never apply a second hidden step.
	main.player = Vector2(600, 400)
	var before_tap: Vector2 = main.player
	main._unhandled_input(key_event(KEY_D))
	expect(main.player == before_tap, "movement tap was applied twice outside _process")
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

	# Water and fountain boundaries are solid.
	main.zone = "kallipolis"
	expect(not main.can_walk_to(Vector2(480, 500)), "central sea accepted the player")
	expect(not main.can_walk_to(Vector2(480, 374)), "fountain accepted the player")

	# Entering the inn must spawn away from the exit and E must page/close dialogue.
	main.player = main.inn_door_position
	main.transition_cooldown = 0.0
	main.try_interact()
	expect(main.zone == "inn", "inn entrance did not change zone")
	expect(main.player.distance_to(main.inn_exit_position) > 64.0, "inn entrance spawned on exit trigger")
	expect(main.can_walk_to(main.player), "inn entrance spawned inside furniture")
	expect(main.dialogue_open, "inn intro dialogue did not open")
	main._unhandled_input(key_event(KEY_E))
	expect(main.dialogue_open and main.dialogue_page == 1, "E did not advance the inn dialogue page")
	main._unhandled_input(key_event(KEY_E))
	expect(not main.dialogue_open, "E did not close the final inn dialogue page")
	expect(main.zone == "inn", "closing dialogue immediately ejected the player from the inn")

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

	main.queue_free()
	await process_frame
	if failures.is_empty():
		print("REGRESSION SUITE: 25 checks passed")
		quit(0)
	else:
		for failure in failures:
			push_error(failure)
		print("REGRESSION SUITE: %d failure(s)" % failures.size())
		quit(1)
