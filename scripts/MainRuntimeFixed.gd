extends "res://scripts/Main.gd"

const WATER_POSTFX_LINEAR_SHADER := preload("res://shaders/water_postprocess.gdshader")
const WATER_POSTFX_NEAREST_SHADER := preload("res://shaders/water_postprocess_nearest.gdshader")
const MAX_SIMULATION_DELTA := 1.0 / 30.0
const SHORT_TAP_BUFFER := 0.055
const IVO_SHEET_COLUMNS := 4
const IVO_SHEET_ROWS := 4
const IVO_FOOT_SCREEN_OFFSET := Vector2(0, 2)

var ivo_frame_sources: Array[Rect2] = []
var ivo_frame_foot_anchors: Array[float] = []


func _ready() -> void:
	super()
	build_ivo_frame_metadata()
	queue_redraw()


# A render hitch must not turn into a large visible movement jump. The original
# controller already sweeps collisions, but a full delayed frame was still drawn
# as one long displacement. Capping the simulation step prefers a tiny slowdown
# during a hitch instead of making Ivo appear to teleport.
func _process(delta: float) -> void:
	super(clampf(delta, 0.0, MAX_SIMULATION_DELTA))


# The exterior maps are authored 16:9 illustrations in the current build. The
# legacy TileMaps remain in the scene as source material, but rebuilding hidden
# atlases, lights and occluders on every launch wastes startup time and memory.
func configure_kallipolis_layers() -> void:
	pass


func configure_agora_layers() -> void:
	pass


# These interfaces are event-driven below. Keeping their old polling handlers
# empty prevents the key that opens a screen from closing it in the same frame.
func handle_battle_input() -> void:
	pass


func handle_gallery_input() -> void:
	pass


func handle_inventory_input() -> void:
	pass


func handle_map_input() -> void:
	pass


func _unhandled_input(event: InputEvent) -> void:
	# Stop the short-tap assist as soon as the player releases the final movement
	# key. This removes the residual glide that made a quick tap feel airborne.
	if event is InputEventKey and not event.pressed:
		if event.is_action_released("move_left") or event.is_action_released("move_right") or event.is_action_released("move_up") or event.is_action_released("move_down"):
			var held_direction := Input.get_vector("move_left", "move_right", "move_up", "move_down")
			if held_direction.length_squared() <= 0.01:
				tap_move_time = 0.0

	if battle_open:
		handle_battle_event(event)
		return
	if gallery_open:
		handle_gallery_event(event)
		return
	if inventory_open:
		handle_inventory_event(event)
		return
	if map_open:
		handle_map_event(event)
		return

	# Title, pause, dialogue, exploration and directional presses keep using the
	# thoroughly tested implementation in Main.gd.
	super(event)

	# Main.gd buffers taps for 110 ms. A shorter window retains responsive taps
	# while avoiding the long coast after the key is released.
	if is_fresh_key_press(event):
		if event.is_action_pressed("move_left") or event.is_action_pressed("move_right") or event.is_action_pressed("move_up") or event.is_action_pressed("move_down"):
			tap_move_time = minf(tap_move_time, SHORT_TAP_BUFFER)


func is_fresh_key_press(event: InputEvent) -> bool:
	return event is InputEventKey and event.pressed and not event.echo


func handle_inventory_event(event: InputEvent) -> void:
	if not is_fresh_key_press(event):
		return
	if event.is_action_pressed("inventory") or event.is_action_pressed("interact"):
		inventory_open = false
		play_sound($AudioClick)
		queue_redraw()


func handle_map_event(event: InputEvent) -> void:
	if not is_fresh_key_press(event):
		return
	if event.is_action_pressed("map") or event.is_action_pressed("pause_menu") or event.is_action_pressed("interact"):
		map_open = false
		play_sound($AudioClick)
		queue_redraw()


func handle_gallery_event(event: InputEvent) -> void:
	if not is_fresh_key_press(event):
		return
	if event.is_action_pressed("move_left"):
		gallery_index = posmod(gallery_index - 1, heroines.size())
		play_sound($AudioClick)
	elif event.is_action_pressed("move_right"):
		gallery_index = posmod(gallery_index + 1, heroines.size())
		play_sound($AudioClick)
	elif event.is_action_pressed("move_up") or event.is_action_pressed("move_down"):
		gallery_expression = 1 - gallery_expression
		play_sound($AudioClick)
	elif event.is_action_pressed("journal") or event.is_action_pressed("interact"):
		gallery_open = false
		play_sound($AudioClick)
	queue_redraw()


func handle_battle_event(event: InputEvent) -> void:
	if not is_fresh_key_press(event):
		return
	var battle_options := 4 if magic_unlocked else 3
	if event.is_action_pressed("move_up"):
		battle_menu = posmod(battle_menu - 1, battle_options)
		play_sound($AudioClick)
	elif event.is_action_pressed("move_down"):
		battle_menu = posmod(battle_menu + 1, battle_options)
		play_sound($AudioClick)
	elif event.is_action_pressed("interact"):
		execute_battle_action()
	queue_redraw()


func execute_battle_action() -> void:
	if battle_menu == 0:
		play_sound($AudioAttack)
		var damage := 6 + resolve + weapon_bonus()
		resolve = 0
		enemy_health -= damage
		combat_message = "Ivo ataca com a marca: %d de dano." % damage
		if enemy_health <= 0:
			finish_battle()
		else:
			enemy_turn(4)
	elif battle_menu == 1:
		battle_guarding = true
		resolve += 2
		combat_message = "Ivo se protege e lê o ritmo do inimigo. Foco +2."
		enemy_turn(4)
	elif battle_menu == 2:
		resolve += 3
		essence = min(max_essence, essence + 1)
		combat_message = "A marca responde ao medo. Foco +3 e Essência +1, mas você fica exposto."
		enemy_turn(5)
	elif battle_menu == 3:
		if essence <= 0:
			combat_message = "A Marca está vazia. Você precisa recuperar Essência com Focar."
			enemy_turn(4)
		else:
			play_sound($AudioAttack)
			essence -= 1
			var magic_damage := 10 + resolve
			resolve = 0
			enemy_health -= magic_damage
			combat_message = "Ressonância das Moiras atravessa a defesa: %d de dano." % magic_damage
			if enemy_health <= 0:
				finish_battle()
			else:
				enemy_turn(5)


func enemy_turn(base_damage: int) -> void:
	var damage: int = max(1, base_damage - armor_bonus())
	if battle_guarding:
		damage = max(1, damage - 2)
	battle_guarding = false
	health = max(0, health - damage)
	combat_message += "  %s revida: -%d Vida." % [enemy_name, damage]
	if health <= 0:
		finish_player_defeat()


func finish_player_defeat() -> void:
	battle_open = false
	battle_guarding = false
	resolve = 0
	health = max_health
	transition_cooldown = 0.35

	if battle_reward_action == "shade":
		# The middle shard starts the Shade battle after being collected. Roll that
		# collection back on defeat so the encounter can be attempted again.
		if cistern_shards.size() > 1 and cistern_shards[1]:
			cistern_shards[1] = false
			relics = maxi(0, relics - 1)
			for index in range(inventory_items.size() - 1, -1, -1):
				if inventory_items[index].begins_with("Eco de Atlântida"):
					inventory_items.remove_at(index)
					break
		player = Vector2(505, 410)
		show_dialogue("Ivo", ["A Sombra rompe sua guarda e a água apaga seus sentidos.", "A Marca o arrasta de volta. O Eco retorna ao labirinto e espera uma nova tentativa."], [], "")
	else:
		player = Vector2(690, 442)
		show_dialogue("Ivo", ["O golpe do Coletor o derruba, mas a Marca se recusa a deixá-lo partir.", "Você desperta alguns passos atrás, ferido no orgulho e pronto para tentar novamente."], [], "")


func interact_cistern() -> void:
	# Once the ending has advanced the story to Nereu, examining the door again
	# must not repeatedly award Ariane affinity.
	if player.distance_to(cistern_door_position) < INTERACTION_DISTANCE and relics >= 3 and quest_stage >= 9:
		show_dialogue("Porta de Bronze", ["Os três círculos permanecem acesos.", "A rota para Nereu já está aberta; a cisterna não exige outra promessa."], [], "")
		return
	super()


func sync_water_post_effect() -> void:
	if not has_node("WaterPostFX"):
		return
	var exterior_with_water := zone in ["kallipolis", "agora", "nereu"]
	var interface_covering_scene := title_open or battle_open or gallery_open or inventory_open or map_open or pause_open or dialogue_open
	$WaterPostFX.visible = water_effects_enabled and exterior_with_water and not interface_covering_scene
	if not $WaterPostFX.visible:
		return

	var surface_y := 405.0
	if zone == "agora":
		surface_y = 466.0
	elif zone == "nereu":
		surface_y = 468.0

	var material := $WaterPostFX.material as ShaderMaterial
	if material:
		var desired_shader: Shader = WATER_POSTFX_NEAREST_SHADER if scale_mode_index == 0 else WATER_POSTFX_LINEAR_SHADER
		if material.shader != desired_shader:
			material.shader = desired_shader
		material.set_shader_parameter("water_top", surface_y / 540.0)
		material.set_shader_parameter("motion_strength", 0.0018 if scale_mode_index == 0 else 0.0024)


# The source sheet is 1254x1254, which is not evenly divisible by its 4x4 grid.
# The previous 313.5-pixel Rect2 slices sampled half pixels and made consecutive
# poses jump. Integer boundaries plus per-frame alpha-foot anchoring keep the
# character's feet locked to the world while the body animates above them.
func build_ivo_frame_metadata() -> void:
	ivo_frame_sources.clear()
	ivo_frame_foot_anchors.clear()
	var image := IVO_WALK_SHEET.get_image()
	if image == null or image.is_empty():
		build_fallback_ivo_frame_metadata()
		return

	var sheet_width := image.get_width()
	var sheet_height := image.get_height()
	for row in IVO_SHEET_ROWS:
		var top := roundi(float(row) * float(sheet_height) / float(IVO_SHEET_ROWS))
		var bottom := roundi(float(row + 1) * float(sheet_height) / float(IVO_SHEET_ROWS))
		for frame in IVO_SHEET_COLUMNS:
			var left := roundi(float(frame) * float(sheet_width) / float(IVO_SHEET_COLUMNS))
			var right := roundi(float(frame + 1) * float(sheet_width) / float(IVO_SHEET_COLUMNS))
			var source_i := Rect2i(left, top, right - left, bottom - top)
			ivo_frame_sources.append(Rect2(source_i.position, source_i.size))

			var region := image.get_region(source_i)
			var used := region.get_used_rect()
			var visible_bottom := float(used.end.y) if not used.has_area() else float(source_i.size.y) * 0.93
			var scaled_foot := visible_bottom / float(source_i.size.y) * IVO_WALK_DRAW_SIZE.y
			ivo_frame_foot_anchors.append(clampf(scaled_foot, IVO_WALK_DRAW_SIZE.y * 0.72, IVO_WALK_DRAW_SIZE.y))


func build_fallback_ivo_frame_metadata() -> void:
	var sheet_width := IVO_WALK_SHEET.get_width()
	var sheet_height := IVO_WALK_SHEET.get_height()
	for row in IVO_SHEET_ROWS:
		var top := roundi(float(row) * float(sheet_height) / float(IVO_SHEET_ROWS))
		var bottom := roundi(float(row + 1) * float(sheet_height) / float(IVO_SHEET_ROWS))
		for frame in IVO_SHEET_COLUMNS:
			var left := roundi(float(frame) * float(sheet_width) / float(IVO_SHEET_COLUMNS))
			var right := roundi(float(frame + 1) * float(sheet_width) / float(IVO_SHEET_COLUMNS))
			ivo_frame_sources.append(Rect2(left, top, right - left, bottom - top))
			ivo_frame_foot_anchors.append(IVO_WALK_DRAW_SIZE.y - 3.0)


func draw_player_character(position: Vector2) -> void:
	var direction_row := 0
	if absf(player_facing.x) > absf(player_facing.y):
		direction_row = 1 if player_facing.x < 0.0 else 2
	elif player_facing.y < 0.0:
		direction_row = 3

	var frame := posmod(int(floor(walk_phase)), IVO_SHEET_COLUMNS) if player_moving else 0
	var metadata_index := direction_row * IVO_SHEET_COLUMNS + frame
	var source := Rect2(
		frame * IVO_WALK_CELL_SIZE.x,
		direction_row * IVO_WALK_CELL_SIZE.y,
		IVO_WALK_CELL_SIZE.x,
		IVO_WALK_CELL_SIZE.y
	)
	var foot_anchor := IVO_WALK_DRAW_SIZE.y - 3.0
	if metadata_index >= 0 and metadata_index < ivo_frame_sources.size():
		source = ivo_frame_sources[metadata_index]
		foot_anchor = ivo_frame_foot_anchors[metadata_index]

	var step := absf(sin(walk_phase * PI * 0.5)) if player_moving else 0.0
	var shadow_width := lerpf(11.0, 13.0, step)
	draw_sprite_shadow(position + Vector2(0, 2), Vector2(shadow_width, 3), Color(0.01, 0.02, 0.04, 0.34))

	# No artificial vertical bob: the actual opaque foot line of each frame is the
	# anchor. This removes the floating effect without making the animation static.
	var destination_position := position + IVO_FOOT_SCREEN_OFFSET - Vector2(IVO_WALK_DRAW_SIZE.x * 0.5, foot_anchor)
	var destination := Rect2(destination_position, IVO_WALK_DRAW_SIZE)
	draw_texture_rect_region(IVO_WALK_SHEET, destination, source, Color.WHITE)

	if player_moving and step > 0.86:
		var dust_direction := Vector2(-signf(player_facing.x), 0.4).normalized()
		draw_circle(position + dust_direction * Vector2(11, 5) + Vector2(0, 3), 2.0, Color(0.78, 0.68, 0.48, 0.32))


func draw_inventory(font: Font) -> void:
	draw_rect(Rect2(170, 72, 620, 400), Color(0.025, 0.035, 0.08, 0.98))
	draw_rect(Rect2(170, 72, 620, 400), Color("d5b46d"), false, 3.0)
	draw_string(font, Vector2(208, 118), "BOLSA DE IVO", HORIZONTAL_ALIGNMENT_LEFT, -1, 27, Color("f7e6bf"))
	draw_string(font, Vector2(208, 155), "Vida: %d/%d    Essência: %d/%d    Ouro: %d" % [health, max_health, essence, max_essence, gold], HORIZONTAL_ALIGNMENT_LEFT, -1, 18, Color("d7e6ee"))
	draw_string(font, Vector2(208, 187), "Arma: " + equipped_weapon, HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("ffd78d"))
	draw_string(font, Vector2(208, 213), "Armadura: " + equipped_armor, HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("d1dced"))
	draw_string(font, Vector2(208, 239), "Relíquia: " + equipped_relic, HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("9ee8ef"))
	draw_line(Vector2(208, 252), Vector2(750, 252), Color("4f607b"), 2.0)

	var items_per_column := 5
	var visible_item_count := mini(inventory_items.size(), items_per_column * 2)
	for index in visible_item_count:
		var column := floori(float(index) / float(items_per_column))
		var row := index % items_per_column
		var x := 208.0 + column * 276.0
		var y := 267.0 + row * 31.0
		draw_rect(Rect2(x, y, 260, 24), Color("172239"))
		draw_string(font, Vector2(x + 12, y + 19), "• " + inventory_items[index], HORIZONTAL_ALIGNMENT_LEFT, 240, 14, Color("edf1f7"))

	if inventory_items.size() > visible_item_count:
		draw_string(font, Vector2(208, 438), "+%d itens guardados" % (inventory_items.size() - visible_item_count), HORIZONTAL_ALIGNMENT_LEFT, 250, 13, Color("c9d7e5"))
	draw_string(font, Vector2(640, 442), "[I/E] fechar", HORIZONTAL_ALIGNMENT_LEFT, -1, 15, Color("ffd888"))