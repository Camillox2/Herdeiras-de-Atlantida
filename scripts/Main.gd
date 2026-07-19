extends Node2D

const SPEED := 190.0
const WORLD := Rect2(28, 70, 904, 530)
const SAVE_PATH := "user://otherworld_save.cfg"
const GRAPHICS_PATH := "user://otherworld_graphics.cfg"
const TILE_SIZE := 32
const TOWN_ORIGIN := Vector2(0, 72)
const TOWN_COLUMNS := 30
const TOWN_ROWS := 17
const GAMEPLAY_RENDER_OFFSET := Vector2(0, -72)
const ARIANE_PORTRAIT := preload("res://assets/portraits/ariane.png")
const ARIANE_EMBARRASSED_PORTRAIT := preload("res://assets/portraits/ariane-embarrassed-v2.png")
const KALLIPOLIS_OPENING := preload("res://assets/backgrounds/kallipolis-opening.png")
const CISTERN_BACKGROUND := preload("res://assets/backgrounds/cistern-labyrinth.png")
const IVO_PORTRAIT := preload("res://assets/portraits/ivo.png")
const NERISSA_PORTRAIT := preload("res://assets/portraits/nerissa.png")
const NERISSA_EMBARRASSED_PORTRAIT := preload("res://assets/portraits/nerissa-embarrassed.png")
const THALIA_PORTRAIT := preload("res://assets/portraits/thalia.png")
const THALIA_EMBARRASSED_PORTRAIT := preload("res://assets/portraits/thalia-embarrassed.png")
const LYRA_PORTRAIT := preload("res://assets/portraits/lyra.png")
const LYRA_EMBARRASSED_PORTRAIT := preload("res://assets/portraits/lyra-embarrassed.png")
const MELIA_PORTRAIT := preload("res://assets/portraits/melia.png")
const MELIA_EMBARRASSED_PORTRAIT := preload("res://assets/portraits/melia-embarrassed.png")
const CASSIA_PORTRAIT := preload("res://assets/portraits/cassia.png")
const CASSIA_EMBARRASSED_PORTRAIT := preload("res://assets/portraits/cassia-embarrassed.png")
const TOWN_GRASS := preload("res://assets/kenney/tiny-town/Tiles/tile_0000.png")
const TOWN_FLOWERS := preload("res://assets/kenney/tiny-town/Tiles/tile_0001.png")
const TOWN_PATH := preload("res://assets/kenney/tiny-town/Tiles/tile_0012.png")
const TOWN_STONE := preload("res://assets/kenney/tiny-town/Tiles/tile_0048.png")
const TOWN_ROOF := preload("res://assets/kenney/tiny-town/Tiles/tile_0052.png")
const TOWN_TREE := preload("res://assets/kenney/tiny-town/Tiles/tile_0005.png")
const SPRITE_LYSANDRA := preload("res://assets/kenney/tiny-dungeon/Tiles/tile_0084.png")
const SPRITE_IVO := preload("res://assets/kenney/tiny-dungeon/Tiles/tile_0085.png")
const SPRITE_POLEMON := preload("res://assets/kenney/tiny-dungeon/Tiles/tile_0088.png")
const SPRITE_ARIANE := preload("res://assets/kenney/tiny-dungeon/Tiles/tile_0087.png")
const SPRITE_COLLECTOR := preload("res://assets/kenney/tiny-dungeon/Tiles/tile_0090.png")
const DUNGEON_FLOOR := preload("res://assets/kenney/tiny-dungeon/Tiles/tile_0048.png")
const DUNGEON_WALL := preload("res://assets/kenney/tiny-dungeon/Tiles/tile_0014.png")
const DUNGEON_TORCH := preload("res://assets/kenney/tiny-dungeon/Tiles/tile_0028.png")
const KALLIPOLIS_TILESET := preload("res://assets/custom/kallipolis-tileset-v2.png")
const KALLIPOLIS_TERRAIN_ATLAS := preload("res://assets/custom/kallipolis-terrain-native-v1.png")
const KALLIPOLIS_CHARACTER_SHEET := preload("res://assets/custom/kallipolis-characters-v1.png")
const IVO_WALK_SHEET := preload("res://assets/custom/ivo-walk-sheet-v1.png")
const KALLIPOLIS_PROPS_SHEET := preload("res://assets/custom/kallipolis-props-v1.png")
const KALLIPOLIS_ENVIRONMENT_SHEET := preload("res://assets/custom/kallipolis-environment-v1.png")
const KALLIPOLIS_AGORA_SHEET := preload("res://assets/custom/kallipolis-agora-v1.png")
const PENSION_EXTERIOR := preload("res://assets/custom/pension-exterior-v1.png")
const MARKET_EXTERIOR := preload("res://assets/custom/market-exterior-v1.png")
const ARCHIVE_EXTERIOR := preload("res://assets/custom/archive-exterior-v1.png")
const PENSION_INTERIOR := preload("res://assets/custom/pension-interior-v2.png")
const KALLIPOLIS_EXTERIOR := preload("res://assets/custom/kallipolis-exterior-v4.png")
const AGORA_EXTERIOR := preload("res://assets/custom/agora-exterior-v2.png")
const NEREU_EXTERIOR := preload("res://assets/custom/nereu-exterior-v1.png")
const HARBOR_WATER_SHADER := preload("res://shaders/harbor_water.gdshader")
const ART_SOURCE_ORIGINS := [17.0, 328.0, 638.0, 949.0]
const ART_SOURCE_SIZE := Vector2(289, 289)
const CHARACTER_CELL_SIZE := Vector2(443.5, 443.5)
const IVO_WALK_CELL_SIZE := Vector2(313.5, 313.5)
const IVO_WALK_ROW_ORIGINS := [0.0, 313.0, 627.0, 893.0]
const IVO_WALK_ROW_HEIGHTS := [313.0, 303.0, 266.0, 361.0]
const IVO_WALK_FOOT_OFFSETS := [86.0, 74.0, 75.0, 66.0]
const ENVIRONMENT_CELL_SIZE := Vector2(313.5, 313.5)
const ART_TILE_SCALE := 32.0 / 289.0
const CHARACTER_DRAW_SIZE := Vector2(72, 72)
const CHARACTER_DRAW_OFFSET := Vector2(36, 63)
const IVO_WALK_DRAW_SIZE := Vector2(96, 96)
const RESOLUTION_OPTIONS := [Vector2i(960, 540), Vector2i(1280, 720), Vector2i(1600, 900), Vector2i(1920, 1080), Vector2i(2560, 1440)]
const RESOLUTION_LABELS := ["960 x 540", "1280 x 720", "1600 x 900", "1920 x 1080", "2560 x 1440"]
const DISPLAY_MODE_LABELS := ["Janela", "Janela sem bordas", "Tela cheia"]
const SCALE_MODE_LABELS := ["Pixels nítidos", "Suavização HD"]

var player := Vector2(496, 456)
var gold := 7
var health := 24
var max_health := 24
var essence := 0
var max_essence := 3
var magic_unlocked := false
var equipped_weapon := "Faca de cais (+2 Ataque)"
var equipped_armor := "Capa de viagem (+1 Guarda)"
var equipped_relic := "Marca das Moiras (selada)"
var quest_stage := 0
var ariane_affinity := 0
var zone := "kallipolis"
var relics := 0
var resolve := 0
var cistern_shards := [false, false, false]
var shade_defeated := false
var cistern_chest_open := false
var dialogue_open := false
var dialogue_speaker := ""
var dialogue_lines: Array[String] = []
var dialogue_choices: Array[String] = []
var choice_index := 0
var dialogue_action := ""
var dialogue_expression := "neutral"
var notice := ""
var notice_time := 0.0
var battle_open := false
var battle_menu := 0
var enemy_health := 18
var enemy_max_health := 18
var enemy_name := "Coletor de Relíquias"
var battle_reward_action := "collector"
var battle_guarding := false
var combat_message := ""
var gallery_open := false
var gallery_index := 0
var gallery_expression := 0
var inventory_open := false
var map_open := false
var pause_open := false
var pause_selection := 0
var settings_open := false
var settings_selection := 0
var resolution_index := 0
var display_mode_index := 0
var scale_mode_index := 0
var vsync_enabled := true
var shadows_enabled := true
var water_effects_enabled := true
var warm_lighting_enabled := true
var brightness_percent := 100
var water_phase := 0.0
var title_open := true
var player_moving := false
var player_facing := Vector2.DOWN
var walk_phase := 0.0
var inventory_items: Array[String] = ["Pão seco", "Capa molhada"]

var cistern_shard_positions := [Vector2(265, 370), Vector2(505, 300), Vector2(748, 245)]
var cistern_door_position := Vector2(840, 150)
var cistern_exit_position := Vector2(104, 452)
var cistern_gate_position := Vector2(895, 420)
var cistern_chest_position := Vector2(456, 420)
var inn_door_position := Vector2(242, 325)
var inn_exit_position := Vector2(480, 552)
var inn_lysandra_position := Vector2(690, 335)
var inn_counter_interaction_position := Vector2(548, 350)
var agora_gate_position := Vector2(726, 346)
var agora_exit_position := Vector2(480, 500)
var agora_polemon_position := Vector2(348, 408)
var agora_notice_board_position := Vector2(282, 379)
var agora_route_position := Vector2(898, 327)
var nereu_exit_position := Vector2(480, 500)
var nereu_nerissa_position := Vector2(704, 366)
var nereu_palace_position := Vector2(480, 292)

var heroines := [
	{"name": "Ariane", "age": 18, "role": "Mensageira e ladra", "color": Color("4f87c8"), "portrait": ARIANE_PORTRAIT, "embarrassed": ARIANE_EMBARRASSED_PORTRAIT},
	{"name": "Mélia", "age": 20, "role": "Botânica de Asterion", "color": Color("5d9c69"), "portrait": MELIA_PORTRAIT, "embarrassed": MELIA_EMBARRASSED_PORTRAIT},
	{"name": "Lyra", "age": 21, "role": "Sacerdotisa e cantora", "color": Color("d3a64b"), "portrait": LYRA_PORTRAIT, "embarrassed": LYRA_EMBARRASSED_PORTRAIT},
	{"name": "Thalia", "age": 22, "role": "Guerreira da arena", "color": Color("c85a58"), "portrait": THALIA_PORTRAIT, "embarrassed": THALIA_EMBARRASSED_PORTRAIT},
	{"name": "Cassia", "age": 23, "role": "Princesa exilada", "color": Color("765a9e"), "portrait": CASSIA_PORTRAIT, "embarrassed": CASSIA_EMBARRASSED_PORTRAIT},
	{"name": "Nerissa", "age": 25, "role": "Capitã de Nereu", "color": Color("9ebed4"), "portrait": NERISSA_PORTRAIT, "embarrassed": NERISSA_EMBARRASSED_PORTRAIT},
]

var npcs := [
	{"name": "Lysandra", "position": Vector2(304, 250), "color": Color("b88963"), "role": "pension", "sprite": Vector2i(2, 0)},
	{"name": "Pólemon", "position": Vector2(464, 250), "color": Color("cfa24d"), "role": "smuggler", "sprite": Vector2i(3, 0)},
	{"name": "Ariane", "position": Vector2(752, 314), "color": Color("4f87c8"), "role": "ariane", "sprite": Vector2i(1, 0)},
	{"name": "Coletor", "position": Vector2(816, 442), "color": Color("9d4d58"), "role": "collector", "sprite": Vector2i(0, 1)},
]

var crate_position := Vector2(656, 442)

func _ready() -> void:
	load_game()
	load_graphics_settings()
	var launch_arguments := OS.get_cmdline_user_args()
	if "--skip-title" in launch_arguments:
		title_open = false
		dialogue_open = false
		zone = "kallipolis"
		player = Vector2(496, 456)
	if "--qa-inn" in launch_arguments:
		title_open = false
		dialogue_open = false
		zone = "inn"
		player = Vector2(548, 360)
		player_facing = Vector2.RIGHT
	if "--qa-agora" in launch_arguments:
		title_open = false
		dialogue_open = false
		zone = "agora"
		player = Vector2(480, 500)
		player_facing = Vector2.UP
	if "--qa-nereu" in launch_arguments:
		title_open = false
		dialogue_open = false
		zone = "nereu"
		quest_stage = max(quest_stage, 9)
		player = Vector2(480, 500)
		player_facing = Vector2.UP
	if "--qa-settings" in launch_arguments:
		title_open = false
		dialogue_open = false
		zone = "kallipolis"
		player = Vector2(480, 440)
		pause_open = true
		settings_open = true
	if "--qa-nerissa-dialogue" in launch_arguments:
		title_open = false
		pause_open = false
		settings_open = false
		zone = "nereu"
		player = Vector2(650, 400)
		start_nerissa_intro()
	apply_graphics_settings()
	configure_kallipolis_layers()
	configure_agora_layers()
	sync_world_visibility()
	queue_redraw()

func configure_kallipolis_layers() -> void:
	# The exploration world is now composed in Godot TileMap layers instead of a single backdrop.
	var terrain_set := create_native_art_tile_set(KALLIPOLIS_TERRAIN_ATLAS)
	var large_structure_set := create_scaled_art_tile_set(KALLIPOLIS_TILESET, 145)
	for layer in [$World/Ground, $World/Water, $World/Roofs]:
		layer.tile_set = terrain_set
		layer.position = Vector2.ZERO
		layer.scale = Vector2.ONE
	$World/Structures.tile_set = large_structure_set
	$World/Structures.position = Vector2.ZERO
	$World/Structures.scale = Vector2(32.0 / 145.0, 32.0 / 145.0)
	var water_material := ShaderMaterial.new()
	water_material.shader = HARBOR_WATER_SHADER
	$World/Water.material = water_material
	$World/Props.tile_set = create_scaled_art_tile_set(KALLIPOLIS_PROPS_SHEET, 193)
	$World/Props.position = Vector2.ZERO
	$World/Props.scale = Vector2(32.0 / 193.0, 32.0 / 193.0)
	$World/LightLayer.position = GAMEPLAY_RENDER_OFFSET
	build_kallipolis_tilemaps()
	build_kallipolis_lights()

func configure_agora_layers() -> void:
	var city_tile_set := create_art_tile_set(KALLIPOLIS_TILESET)
	var agora_tile_set := create_art_tile_set(KALLIPOLIS_AGORA_SHEET)
	for layer in [$World/AgoraGround, $World/AgoraStructures, $World/AgoraRoofs]:
		layer.tile_set = city_tile_set
		layer.position = Vector2.ZERO
		layer.scale = Vector2(ART_TILE_SCALE, ART_TILE_SCALE)
	$World/AgoraProps.tile_set = agora_tile_set
	$World/AgoraProps.position = Vector2.ZERO
	$World/AgoraProps.scale = Vector2(ART_TILE_SCALE, ART_TILE_SCALE)
	build_agora_tilemaps()

func build_agora_tilemaps() -> void:
	var ground: TileMapLayer = $World/AgoraGround
	var structures: TileMapLayer = $World/AgoraStructures
	var props: TileMapLayer = $World/AgoraProps
	var roofs: TileMapLayer = $World/AgoraRoofs
	ground.clear()
	structures.clear()
	props.clear()
	roofs.clear()
	for row in TOWN_ROWS:
		for column in TOWN_COLUMNS:
			var floor_tile := Vector2i(2, 0) if row in range(2, 12) and column in range(2, 28) else Vector2i(0, 0)
			ground.set_cell(Vector2i(column, row), 0, floor_tile)
	for column in TOWN_COLUMNS:
		if column not in range(13, 17):
			structures.set_cell(Vector2i(column, 1), 0, Vector2i(1, 1))
			roofs.set_cell(Vector2i(column, 0), 0, Vector2i(0, 1))
	for position_and_tile in [
		[Vector2i(4, 4), Vector2i(0, 0)], [Vector2i(9, 3), Vector2i(1, 0)],
		[Vector2i(14, 5), Vector2i(2, 0)], [Vector2i(21, 4), Vector2i(3, 0)],
		[Vector2i(9, 7), Vector2i(0, 1)], [Vector2i(17, 8), Vector2i(1, 1)],
		[Vector2i(22, 8), Vector2i(2, 1)], [Vector2i(26, 10), Vector2i(3, 1)],
		[Vector2i(4, 9), Vector2i(0, 2)], [Vector2i(12, 10), Vector2i(1, 2)],
		[Vector2i(15, 10), Vector2i(2, 2)], [Vector2i(24, 3), Vector2i(3, 2)],
		[Vector2i(6, 11), Vector2i(0, 3)], [Vector2i(19, 10), Vector2i(1, 3)],
		[Vector2i(28, 5), Vector2i(2, 3)], [Vector2i(26, 6), Vector2i(3, 3)]
	]:
		props.set_cell(position_and_tile[0], 0, position_and_tile[1])

func sync_world_visibility() -> void:
	# Exterior districts now use single, authored map illustrations. Legacy TileMaps stay
	# available as source material, but no longer leak repeated tiles behind the new art.
	for layer in [$World/Ground, $World/Water, $World/Structures, $World/Props, $World/Roofs, $World/LightLayer]:
		layer.visible = false
	for layer in [$World/AgoraGround, $World/AgoraStructures, $World/AgoraProps, $World/AgoraRoofs]:
		layer.visible = false

func create_art_tile_set(texture: Texture2D) -> TileSet:
	var tile_set := TileSet.new()
	tile_set.tile_size = Vector2i(289, 289)
	var atlas := TileSetAtlasSource.new()
	atlas.texture = texture
	atlas.texture_region_size = Vector2i(289, 289)
	atlas.margins = Vector2i(17, 17)
	atlas.separation = Vector2i(21, 21)
	for row in 4:
		for column in 4:
			atlas.create_tile(Vector2i(column, row))
	tile_set.add_source(atlas, 0)
	return tile_set

func create_native_art_tile_set(texture: Texture2D) -> TileSet:
	var tile_set := TileSet.new()
	tile_set.tile_size = Vector2i(TILE_SIZE, TILE_SIZE)
	var atlas := TileSetAtlasSource.new()
	atlas.texture = texture
	atlas.texture_region_size = Vector2i(TILE_SIZE, TILE_SIZE)
	for row in 4:
		for column in 4:
			atlas.create_tile(Vector2i(column, row))
	tile_set.add_source(atlas, 0)
	return tile_set

func create_scaled_art_tile_set(texture: Texture2D, logical_tile_size: int) -> TileSet:
	var tile_set := TileSet.new()
	tile_set.tile_size = Vector2i(logical_tile_size, logical_tile_size)
	var atlas := TileSetAtlasSource.new()
	atlas.texture = texture
	atlas.texture_region_size = Vector2i(289, 289)
	atlas.margins = Vector2i(17, 17)
	atlas.separation = Vector2i(21, 21)
	for row in 4:
		for column in 4:
			atlas.create_tile(Vector2i(column, row))
	tile_set.add_source(atlas, 0)
	return tile_set

func build_kallipolis_lights() -> void:
	var light_layer: Node2D = $World/LightLayer
	for child in light_layer.get_children():
		child.queue_free()
	var gradient := Gradient.new()
	gradient.offsets = PackedFloat32Array([0.0, 0.22, 1.0])
	gradient.colors = PackedColorArray([Color(1.0, 0.76, 0.36, 0.86), Color(1.0, 0.45, 0.12, 0.3), Color(1.0, 0.22, 0.04, 0.0)])
	var light_texture := GradientTexture2D.new()
	light_texture.gradient = gradient
	light_texture.width = 256
	light_texture.height = 256
	light_texture.fill = GradientTexture2D.FILL_RADIAL
	for light_position in [Vector2(280, 254), Vector2(472, 254), Vector2(727, 350), Vector2(210, 435)]:
		var lantern := PointLight2D.new()
		lantern.texture = light_texture
		lantern.position = light_position
		lantern.energy = 0.38
		lantern.texture_scale = 0.38
		lantern.color = Color("ffce83")
		lantern.shadow_enabled = true
		light_layer.add_child(lantern)
	# Only large structures cast dynamic shadows. This keeps the scene readable and inexpensive.
	for building in [Rect2i(5, 2, 4, 3), Rect2i(11, 2, 5, 3), Rect2i(20, 3, 5, 3)]:
		var occluder := LightOccluder2D.new()
		var polygon := OccluderPolygon2D.new()
		var size := Vector2(building.size.x * TILE_SIZE, building.size.y * TILE_SIZE)
		polygon.polygon = PackedVector2Array([Vector2.ZERO, Vector2(size.x, 0), size, Vector2(0, size.y)])
		occluder.occluder = polygon
		occluder.position = TOWN_ORIGIN + Vector2(building.position.x * TILE_SIZE, building.position.y * TILE_SIZE)
		light_layer.add_child(occluder)

func build_kallipolis_tilemaps() -> void:
	var ground: TileMapLayer = $World/Ground
	var water: TileMapLayer = $World/Water
	var structures: TileMapLayer = $World/Structures
	var props: TileMapLayer = $World/Props
	var roofs: TileMapLayer = $World/Roofs
	ground.clear()
	water.clear()
	structures.clear()
	props.clear()
	roofs.clear()
	for row in TOWN_ROWS:
		for column in TOWN_COLUMNS:
			var cell := Vector2i(column, row)
			var kind := town_tile_kind(column, row)
			var variation := posmod(column * 7 + row * 11, 4)
			var ground_slot := Vector2i(variation, 0)
			if kind == "water":
				ground_slot = Vector2i(posmod(column + row * 2, 4), 2)
				water.set_cell(cell, 0, ground_slot)
			elif kind == "path":
				ground_slot = Vector2i(variation, 1)
			elif kind == "building":
				# Collision is still solid, but complete landmark sprites provide the visible building.
				ground_slot = Vector2i(variation, 0)
			elif kind == "tree":
				ground_slot = Vector2i(variation, 0)
			ground.set_cell(cell, 0, ground_slot)
	# Extra water rows cover the full 16:9 viewport below the playable map.
	for row in range(TOWN_ROWS, TOWN_ROWS + 3):
		for column in TOWN_COLUMNS:
			var water_slot := Vector2i(posmod(column + row * 2, 4), 2)
			ground.set_cell(Vector2i(column, row), 0, water_slot)
			water.set_cell(Vector2i(column, row), 0, water_slot)
	# Purpose-built coastal transitions replace the repeated generic wall strip.
	for column in range(4, 30):
		roofs.set_cell(Vector2i(column, 13), 0, Vector2i(0, 3))
	for row in range(8, 14):
		roofs.set_cell(Vector2i(2, row), 0, Vector2i(1, 3))
	# The three former building blocks are now complete landmark sprites: pension, market and archive.
	# Keeping this layer empty there prevents repeated roof strips from peeking through their silhouettes.
	structures.set_cell(Vector2i(14, 7), 0, Vector2i(2, 2))
	for pier_x in range(3, 8):
		structures.set_cell(Vector2i(pier_x, 11), 0, Vector2i(1, 2))
	# A prop layer makes the city readable: each cluster implies a purpose and a story.
	for prop_data in [
		[Vector2i(9, 7), Vector2i(0, 1)], [Vector2i(11, 7), Vector2i(1, 1)],
		[Vector2i(3, 10), Vector2i(0, 0)], [Vector2i(4, 10), Vector2i(3, 0)],
		[Vector2i(1, 8), Vector2i(2, 1)], [Vector2i(2, 9), Vector2i(3, 1)],
		[Vector2i(8, 8), Vector2i(0, 2)], [Vector2i(17, 8), Vector2i(2, 2)],
		[Vector2i(19, 8), Vector2i(3, 2)], [Vector2i(7, 10), Vector2i(0, 3)],
		[Vector2i(22, 7), Vector2i(1, 3)], [Vector2i(25, 9), Vector2i(2, 3)],
		[Vector2i(6, 12), Vector2i(3, 3)]
	]:
		props.set_cell(prop_data[0], 0, prop_data[1])

func _process(delta: float) -> void:
	player_moving = false
	if water_effects_enabled:
		water_phase = fmod(water_phase + delta * 1.4, TAU)
	if notice_time > 0.0:
		notice_time -= delta
	if title_open:
		if Input.is_action_just_pressed("interact"):
			title_open = false
			$AudioConfirm.play()
		if Input.is_action_just_pressed("restart"):
			reset_game()
	elif battle_open:
		handle_battle_input()
	elif gallery_open:
		handle_gallery_input()
	elif inventory_open:
		handle_inventory_input()
	elif map_open:
		handle_map_input()
	elif pause_open:
		pass # Pause and graphics navigation are event-driven in _unhandled_input.
	elif dialogue_open:
		pass # Dialogue choices are also event-driven for reliable short key taps.
	else:
		var direction := Input.get_vector("move_left", "move_right", "move_up", "move_down")
		player_moving = direction.length_squared() > 0.01
		if player_moving:
			player_facing = direction.normalized()
			walk_phase += delta * 10.0
		else:
			walk_phase = 0.0
		try_move_player(direction * SPEED * delta)
		if Input.is_action_just_pressed("interact"):
			try_interact()
		if Input.is_action_just_pressed("save_game"):
			save_game()
		if Input.is_action_just_pressed("journal"):
			gallery_open = true
		if Input.is_action_just_pressed("inventory"):
			inventory_open = true
			$AudioConfirm.play()
		if Input.is_action_just_pressed("map"):
			map_open = true
			$AudioConfirm.play()
		if Input.is_action_just_pressed("pause_menu"):
			pause_open = true
			$AudioConfirm.play()
	queue_redraw()

func _unhandled_input(event: InputEvent) -> void:
	# A short key tap still advances one readable step; holding the key remains smooth in _process.
	if pause_open:
		handle_pause_event(event)
		return
	if dialogue_open:
		handle_dialogue_event(event)
		return
	if title_open or battle_open or gallery_open or inventory_open or map_open:
		return
	var tapped_direction := Vector2.ZERO
	if event is InputEventKey and event.pressed and not event.echo:
		match event.keycode:
			KEY_A, KEY_LEFT: tapped_direction = Vector2.LEFT
			KEY_D, KEY_RIGHT: tapped_direction = Vector2.RIGHT
			KEY_W, KEY_UP: tapped_direction = Vector2.UP
			KEY_S, KEY_DOWN: tapped_direction = Vector2.DOWN
	if tapped_direction == Vector2.ZERO:
		if event.is_action_pressed("move_left"):
			tapped_direction = Vector2.LEFT
		elif event.is_action_pressed("move_right"):
			tapped_direction = Vector2.RIGHT
		elif event.is_action_pressed("move_up"):
			tapped_direction = Vector2.UP
		elif event.is_action_pressed("move_down"):
			tapped_direction = Vector2.DOWN
	if tapped_direction != Vector2.ZERO:
		player_facing = tapped_direction
		player_moving = true
		walk_phase += 1.0
		try_move_player(tapped_direction * 8.0)
		queue_redraw()

func handle_pause_event(event: InputEvent) -> void:
	if not (event is InputEventKey) or not event.pressed or event.echo:
		return
	var code: Key = event.keycode if event.keycode != 0 else event.physical_keycode
	var go_up: bool = code in [KEY_W, KEY_UP] or event.is_action_pressed("move_up")
	var go_down: bool = code in [KEY_S, KEY_DOWN] or event.is_action_pressed("move_down")
	var go_left: bool = code in [KEY_A, KEY_LEFT] or event.is_action_pressed("move_left")
	var go_right: bool = code in [KEY_D, KEY_RIGHT] or event.is_action_pressed("move_right")
	var confirm: bool = code in [KEY_E, KEY_SPACE, KEY_ENTER] or event.is_action_pressed("interact")
	var cancel: bool = code == KEY_ESCAPE or event.is_action_pressed("pause_menu")
	if settings_open:
		if cancel:
			settings_open = false
			save_graphics_settings()
			$AudioClick.play()
		elif go_up:
			settings_selection = posmod(settings_selection - 1, 8)
			$AudioClick.play()
		elif go_down:
			settings_selection = posmod(settings_selection + 1, 8)
			$AudioClick.play()
		elif go_left:
			change_graphics_setting(-1)
		elif go_right or confirm:
			change_graphics_setting(1)
		queue_redraw()
		return
	if cancel:
		pause_open = false
		$AudioClick.play()
	elif go_up:
		pause_selection = posmod(pause_selection - 1, 4)
		$AudioClick.play()
	elif go_down:
		pause_selection = posmod(pause_selection + 1, 4)
		$AudioClick.play()
	elif confirm:
		activate_pause_selection()
	queue_redraw()

func handle_dialogue_event(event: InputEvent) -> void:
	if not (event is InputEventKey) or not event.pressed or event.echo:
		return
	var code: Key = event.keycode if event.keycode != 0 else event.physical_keycode
	var go_up: bool = code in [KEY_W, KEY_UP] or event.is_action_pressed("move_up")
	var go_down: bool = code in [KEY_S, KEY_DOWN] or event.is_action_pressed("move_down")
	var confirm: bool = code in [KEY_E, KEY_SPACE, KEY_ENTER] or event.is_action_pressed("interact")
	if not dialogue_choices.is_empty():
		if go_up:
			choice_index = posmod(choice_index - 1, dialogue_choices.size())
			$AudioClick.play()
		elif go_down:
			choice_index = posmod(choice_index + 1, dialogue_choices.size())
			$AudioClick.play()
		elif confirm:
			choose_dialogue()
			$AudioConfirm.play()
	elif confirm:
		close_dialogue()
		$AudioClick.play()
	queue_redraw()

func try_move_player(motion: Vector2) -> void:
	var candidate := player + motion
	if zone in ["kallipolis", "inn", "agora", "nereu"]:
		candidate.x = clampf(candidate.x, 16.0, 944.0)
		candidate.y = clampf(candidate.y, TOWN_ORIGIN.y + 16.0, TOWN_ORIGIN.y + TOWN_ROWS * TILE_SIZE - 16.0)
	else:
		candidate.x = clampf(candidate.x, WORLD.position.x + 12.0, WORLD.end.x - 12.0)
		candidate.y = clampf(candidate.y, WORLD.position.y + 12.0, WORLD.end.y - 12.0)
	if can_walk_to(candidate):
		player = candidate

func can_walk_to(candidate: Vector2) -> bool:
	if zone == "kallipolis":
		return can_walk_kallipolis(candidate)
	if zone == "cistern":
		var tile := town_tile_from_position(candidate)
		return cistern_tile_kind(tile.x, tile.y) != "wall"
	if zone == "inn":
		if candidate.x < 34.0 or candidate.x > 926.0 or candidate.y < 154.0 or candidate.y > 552.0:
			return false
		var furniture := [
			Rect2(58, 178, 220, 176), Rect2(318, 268, 208, 142),
			Rect2(326, 374, 206, 140), Rect2(566, 226, 310, 284),
			Rect2(870, 158, 58, 310), Rect2(34, 404, 270, 96)
		]
		for obstacle in furniture:
			if obstacle.grow(9.0).has_point(candidate):
				return false
	if zone == "agora":
		return can_walk_agora(candidate)
	if zone == "nereu":
		return can_walk_nereu(candidate)
	return true

func can_walk_kallipolis(candidate: Vector2) -> bool:
	# World coordinates are 72 px below the painted viewport. Broad regions keep
	# movement readable while landmark silhouettes, fountain and sea stay solid.
	var on_promenade := Rect2(64, 310, 832, 154).has_point(candidate)
	var on_west_pier := Rect2(58, 418, 190, 118).has_point(candidate)
	var on_sea_gate_landing := Rect2(430, 418, 100, 76).has_point(candidate)
	if not (on_promenade or on_west_pier or on_sea_gate_landing):
		return false
	var fountain_center := Vector2(480, 374)
	if candidate.distance_to(fountain_center) < 56.0:
		return false
	return true

func can_walk_agora(candidate: Vector2) -> bool:
	var in_central_plaza := Rect2(205, 220, 555, 300).has_point(candidate)
	var in_market_lane := Rect2(145, 315, 245, 165).has_point(candidate)
	var in_route_lane := Rect2(720, 245, 195, 170).has_point(candidate)
	if not (in_central_plaza or in_market_lane or in_route_lane):
		return false
	var armillary_center := Vector2(480, 340)
	if candidate.distance_to(armillary_center) < 58.0:
		return false
	return true

func can_walk_nereu(candidate: Vector2) -> bool:
	var in_lower_quay := Rect2(365, 392, 230, 142).has_point(candidate)
	var in_outer_boulevard := Rect2(90, 318, 790, 168).has_point(candidate)
	var in_north_avenue := Rect2(405, 220, 150, 170).has_point(candidate)
	var in_side_gate := Rect2(45, 280, 125, 135).has_point(candidate) or Rect2(820, 275, 115, 145).has_point(candidate)
	if not (in_lower_quay or in_outer_boulevard or in_north_avenue or in_side_gate):
		return false
	var central_pool := Vector2(480, 345)
	if candidate.distance_to(central_pool) < 98.0:
		return false
	return true

func town_tile_from_position(position: Vector2) -> Vector2i:
	return Vector2i(floori(position.x / TILE_SIZE), floori((position.y - TOWN_ORIGIN.y) / TILE_SIZE))

func town_tile_kind(column: int, row: int) -> String:
	if column < 0 or column >= TOWN_COLUMNS or row < 0 or row >= TOWN_ROWS:
		return "water"
	if row >= 14:
		return "water"
	# The western harbour and the northern canal create a recognisable shoreline.
	if (column <= 2 and row >= 7) or (column >= 27 and row <= 2):
		return "water"
	# Main avenue, fountain square and the pier.
	if (row == 8 and column >= 3) or (column == 14 and row >= 3) or (row in [6, 7] and column in range(11, 18)) or (row == 11 and column <= 7):
		return "path"
	# Pension, market hall and cliffside home.
	var buildings := [Rect2i(5, 2, 4, 3), Rect2i(11, 2, 5, 3), Rect2i(20, 3, 5, 3)]
	for building in buildings:
		if building.has_point(Vector2i(column, row)):
			return "building"
	var trees := [Vector2i(3, 2), Vector2i(4, 2), Vector2i(3, 3), Vector2i(9, 2), Vector2i(18, 2), Vector2i(19, 2), Vector2i(25, 2), Vector2i(26, 3), Vector2i(4, 12), Vector2i(5, 12), Vector2i(24, 11), Vector2i(25, 11), Vector2i(27, 10)]
	if Vector2i(column, row) in trees:
		return "tree"
	return "grass"

func cistern_tile_kind(column: int, row: int) -> String:
	if column < 0 or column >= TOWN_COLUMNS or row < 0 or row >= TOWN_ROWS:
		return "wall"
	if column == 0 or column == TOWN_COLUMNS - 1 or row == 0 or row == TOWN_ROWS - 1:
		return "wall"
	var wall_cells := [
		Vector2i(6, 1), Vector2i(6, 2), Vector2i(6, 3), Vector2i(6, 4), Vector2i(6, 5),
		Vector2i(11, 8), Vector2i(11, 9), Vector2i(11, 10), Vector2i(11, 11), Vector2i(11, 12),
		Vector2i(18, 1), Vector2i(18, 2), Vector2i(18, 3), Vector2i(18, 4), Vector2i(18, 5),
		Vector2i(23, 8), Vector2i(23, 9), Vector2i(23, 10), Vector2i(23, 11), Vector2i(23, 12)
	]
	return "wall" if Vector2i(column, row) in wall_cells else "floor"

func agora_tile_kind(column: int, row: int) -> String:
	if column < 0 or column >= TOWN_COLUMNS or row < 0 or row >= TOWN_ROWS:
		return "building"
	if row == 1 and column not in range(13, 17):
		return "building"
	var blocked_props := [Vector2i(4, 4), Vector2i(9, 3), Vector2i(14, 5), Vector2i(21, 4), Vector2i(9, 7), Vector2i(17, 8), Vector2i(22, 8), Vector2i(26, 10), Vector2i(4, 9), Vector2i(12, 10), Vector2i(15, 10), Vector2i(24, 3), Vector2i(6, 11), Vector2i(19, 10), Vector2i(28, 5), Vector2i(26, 6)]
	return "building" if Vector2i(column, row) in blocked_props else "floor"

func handle_gallery_input() -> void:
	if Input.is_action_just_pressed("move_left"):
		gallery_index = posmod(gallery_index - 1, heroines.size())
	if Input.is_action_just_pressed("move_right"):
		gallery_index = posmod(gallery_index + 1, heroines.size())
	if Input.is_action_just_pressed("move_up") or Input.is_action_just_pressed("move_down"):
		gallery_expression = 1 - gallery_expression
	if Input.is_action_just_pressed("journal") or Input.is_action_just_pressed("interact"):
		gallery_open = false

func handle_inventory_input() -> void:
	if Input.is_action_just_pressed("inventory") or Input.is_action_just_pressed("interact"):
		inventory_open = false
		$AudioClick.play()

func handle_map_input() -> void:
	if Input.is_action_just_pressed("map") or Input.is_action_just_pressed("pause_menu") or Input.is_action_just_pressed("interact"):
		map_open = false
		$AudioClick.play()

func activate_pause_selection() -> void:
	match pause_selection:
		0:
			pause_open = false
		1:
			settings_open = true
			settings_selection = 0
		2:
			save_game()
		3:
			pause_open = false
			title_open = true
	$AudioConfirm.play()

func change_graphics_setting(change: int) -> void:
	match settings_selection:
		0: display_mode_index = posmod(display_mode_index + change, DISPLAY_MODE_LABELS.size())
		1: resolution_index = posmod(resolution_index + change, RESOLUTION_OPTIONS.size())
		2: scale_mode_index = posmod(scale_mode_index + change, SCALE_MODE_LABELS.size())
		3: vsync_enabled = not vsync_enabled
		4: shadows_enabled = not shadows_enabled
		5: water_effects_enabled = not water_effects_enabled
		6: warm_lighting_enabled = not warm_lighting_enabled
		7: brightness_percent = clampi(brightness_percent + change * 5, 70, 120)
	apply_graphics_settings()
	save_graphics_settings()
	$AudioConfirm.play()

func load_graphics_settings() -> void:
	var config := ConfigFile.new()
	if config.load(GRAPHICS_PATH) != OK:
		return
	display_mode_index = clampi(config.get_value("graphics", "display_mode", display_mode_index), 0, DISPLAY_MODE_LABELS.size() - 1)
	resolution_index = clampi(config.get_value("graphics", "resolution", resolution_index), 0, RESOLUTION_OPTIONS.size() - 1)
	scale_mode_index = clampi(config.get_value("graphics", "scale_mode", scale_mode_index), 0, SCALE_MODE_LABELS.size() - 1)
	vsync_enabled = config.get_value("graphics", "vsync", vsync_enabled)
	shadows_enabled = config.get_value("graphics", "shadows", shadows_enabled)
	water_effects_enabled = config.get_value("graphics", "water_effects", water_effects_enabled)
	warm_lighting_enabled = config.get_value("graphics", "warm_lighting", warm_lighting_enabled)
	brightness_percent = clampi(config.get_value("graphics", "brightness", brightness_percent), 70, 120)

func save_graphics_settings() -> void:
	var config := ConfigFile.new()
	config.set_value("graphics", "display_mode", display_mode_index)
	config.set_value("graphics", "resolution", resolution_index)
	config.set_value("graphics", "scale_mode", scale_mode_index)
	config.set_value("graphics", "vsync", vsync_enabled)
	config.set_value("graphics", "shadows", shadows_enabled)
	config.set_value("graphics", "water_effects", water_effects_enabled)
	config.set_value("graphics", "warm_lighting", warm_lighting_enabled)
	config.set_value("graphics", "brightness", brightness_percent)
	config.save(GRAPHICS_PATH)

func apply_graphics_settings() -> void:
	var root_window := get_tree().root
	root_window.content_scale_mode = Window.CONTENT_SCALE_MODE_CANVAS_ITEMS
	root_window.content_scale_aspect = Window.CONTENT_SCALE_ASPECT_KEEP
	# Fractional stretch fills every 16:9 mode; texture filtering decides whether
	# the enlarged pixels stay crisp or receive a softer high-resolution pass.
	root_window.content_scale_stretch = Window.CONTENT_SCALE_STRETCH_FRACTIONAL
	texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST if scale_mode_index == 0 else CanvasItem.TEXTURE_FILTER_LINEAR
	if DisplayServer.get_name() == "headless":
		return
	DisplayServer.window_set_vsync_mode(DisplayServer.VSYNC_ENABLED if vsync_enabled else DisplayServer.VSYNC_DISABLED)
	match display_mode_index:
		0:
			DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_WINDOWED)
			DisplayServer.window_set_flag(DisplayServer.WINDOW_FLAG_BORDERLESS, false)
			var usable := DisplayServer.screen_get_usable_rect()
			var requested: Vector2i = RESOLUTION_OPTIONS[resolution_index]
			var fit_scale: float = minf(1.0, minf(float(usable.size.x) / requested.x, float(usable.size.y) / requested.y))
			var fitted := Vector2i(roundi(requested.x * fit_scale), roundi(requested.y * fit_scale))
			DisplayServer.window_set_size(fitted)
			DisplayServer.window_set_position(usable.position + (usable.size - fitted) / 2)
		1:
			DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_MAXIMIZED)
			DisplayServer.window_set_flag(DisplayServer.WINDOW_FLAG_BORDERLESS, true)
		2:
			DisplayServer.window_set_flag(DisplayServer.WINDOW_FLAG_BORDERLESS, false)
			DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_FULLSCREEN)

func handle_battle_input() -> void:
	var battle_options := 4 if magic_unlocked else 3
	if Input.is_action_just_pressed("move_up"):
		battle_menu = posmod(battle_menu - 1, battle_options)
	if Input.is_action_just_pressed("move_down"):
		battle_menu = posmod(battle_menu + 1, battle_options)
	if Input.is_action_just_pressed("interact"):
		if battle_menu == 0:
			$AudioAttack.play()
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
				$AudioAttack.play()
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
	health = max(1, health - damage)
	combat_message += "  %s revida: -%d Vida." % [enemy_name, damage]

func finish_battle() -> void:
	battle_open = false
	if battle_reward_action == "collector":
		quest_stage = 5
		gold += 8
		ariane_affinity = max(ariane_affinity, 1)
		show_dialogue("Ariane", ["Você não precisava ficar.", "Mas ficou.", "VÍNCULO COM ARIANE AUMENTOU. A entrada da cisterna foi aberta."], [], "")
	elif battle_reward_action == "shade":
		shade_defeated = true
		gold += 5
		show_dialogue("Ariane", ["A sombra não estava protegendo o labirinto.", "Estava protegendo alguém de lembrar quem a criou.", "A segunda relíquia canta. Continue."], [], "")

func try_interact() -> void:
	$AudioClick.play()
	if zone == "cistern":
		interact_cistern()
		return
	if zone == "inn":
		interact_inn()
		return
	if zone == "agora":
		interact_agora()
		return
	if zone == "nereu":
		interact_nereu()
		return
	if player.distance_to(inn_door_position) < 58.0:
		zone = "inn"
		player = inn_exit_position
		sync_world_visibility()
		show_dialogue("Pensão dos Degraus", ["O cheiro de pão, azeite e madeira antiga tira um pouco do sal da sua garganta.", "Atrás do balcão, uma mulher observa sua entrada como se já soubesse que você viria."], [], "")
		return
	if player.distance_to(agora_gate_position) < 62.0:
		zone = "agora"
		player = agora_exit_position
		sync_world_visibility()
		show_dialogue("Ágora das Colunas", ["O mercado se abre atrás do arco de pedra: vozes, címbalos e o atrito de sandálias no mosaico.", "Aqui, toda pessoa parece vender alguma coisa — até o silêncio."], [], "")
		return
	if quest_stage >= 5 and player.distance_to(cistern_gate_position) < 58.0:
		zone = "cistern"
		quest_stage = max(quest_stage, 6)
		player = Vector2(110, 420)
		sync_world_visibility()
		show_dialogue("Ariane", ["A cisterna não aparece nos mapas porque a cidade decidiu esquecê-la.", "Três ecos mantêm a porta fechada. Pegue-os sem deixar o medo escolher por você."], [], "")
		return
	if quest_stage == 2 and player.distance_to(crate_position) < 54.0:
		quest_stage = 3
		inventory_items.append("Moeda azul de Atlântida")
		magic_unlocked = true
		essence = max_essence
		equipped_relic = "Marca das Moiras (Ressonância)"
		show_dialogue("Caixa selada", ["A marca no seu pulso esquenta.", "Dentro da caixa há uma moeda azul e um símbolo que parece um labirinto.", "No telhado, alguém observa você."], [], "")
		return
	for npc in npcs:
		if player.distance_to(npc.position) < 60.0:
			talk_to(npc.role)
			return
	notice = "Nada para interagir aqui."
	notice_time = 1.7

func interact_inn() -> void:
	if player.distance_to(inn_exit_position) < 64.0:
		zone = "kallipolis"
		player = inn_door_position + Vector2(0, 48)
		sync_world_visibility()
		notice = "Você volta à praça de Kallípolis."
		notice_time = 1.8
		return
	if player.distance_to(inn_counter_interaction_position) < 76.0:
		talk_to("pension")
		return
	notice = "A pensão está quieta. Lysandra parece esperar que você diga alguma coisa."
	notice_time = 1.8

func interact_agora() -> void:
	if player.distance_to(agora_exit_position) < 66.0:
		zone = "kallipolis"
		player = agora_gate_position - Vector2(42, 0)
		sync_world_visibility()
		notice = "O cais continua atrás de você."
		notice_time = 1.8
		return
	if player.distance_to(agora_polemon_position) < 70.0:
		talk_to("smuggler")
		return
	if player.distance_to(agora_notice_board_position) < 70.0:
		show_dialogue("Edital da cidade", ["O bronze lista dívidas de marinheiros, preços de azeite e uma recompensa por 'objetos que cantam sob a água'.", "A última linha foi riscada tantas vezes que o metal parece ferido."], [], "")
		return
	if player.distance_to(agora_route_position) < 72.0:
		if quest_stage < 9:
			show_dialogue("Portão de Nereu", ["O arco oriental permanece fechado. Guardas azuis conferem selos de travessia.", "Ainda existe algo sob Kallípolis que você precisa terminar."], [], "")
		else:
			zone = "nereu"
			player = nereu_exit_position
			player_facing = Vector2.UP
			sync_world_visibility()
			show_dialogue("Nereu", ["A travessia termina entre velas azuis e muralhas que parecem nascer da água.", "Kallípolis cheirava a sobrevivência. Nereu cheira a poder bem administrado — o que talvez seja mais perigoso."], [], "")
		return
	notice = "Mercadores negociam, crianças correm entre as colunas e ninguém parece ter tempo a perder."
	notice_time = 1.8

func interact_nereu() -> void:
	if player.distance_to(nereu_exit_position) < 64.0:
		zone = "agora"
		player = agora_route_position - Vector2(48, 0)
		player_facing = Vector2.LEFT
		sync_world_visibility()
		notice = "O ferry retorna à Ágora de Kallípolis."
		notice_time = 1.8
		return
	if player.distance_to(nereu_nerissa_position) < 72.0:
		start_nerissa_intro()
		return
	if player.distance_to(nereu_palace_position) < 72.0:
		show_dialogue("Palácio da Maré", ["Guardas cruzam lanças diante do salão da capitã.", "O símbolo na sua marca responde às fontes do pátio com uma pulsação quase imperceptível."], [], "")
		return
	notice = "Canais luminosos dividem a praça. Cada ponte parece levar a uma versão diferente da cidade."
	notice_time = 1.8

func start_nerissa_intro() -> void:
	show_dialogue("Nerissa", ["Então você é o estrangeiro que fez Kallípolis lembrar do que enterrou.", "Em Nereu, memórias são catalogadas, armadas e lançadas ao mar.", "Se veio por respostas, aprenda a reconhecer uma pergunta perigosa."], ["Perguntar sobre Atlântida.", "Dizer que procura Ariane.", "Admitir que ainda não sabe o que procura."], "nerissa_intro", "neutral")

func interact_cistern() -> void:
	if player.distance_to(cistern_exit_position) < 58.0:
		zone = "kallipolis"
		player = Vector2(850, 400)
		sync_world_visibility()
		notice = "Você voltou à superfície."
		notice_time = 1.8
		return
	if not cistern_chest_open and player.distance_to(cistern_chest_position) < 52.0:
		cistern_chest_open = true
		equipped_weapon = "Daga de bronze (+4 Ataque)"
		equipped_armor = "Manto de escamas (+2 Guarda)"
		inventory_items.append("Daga de bronze de Orfeon")
		inventory_items.append("Manto de escamas de Nereu")
		show_dialogue("Baú afundado", ["Você encontra uma lâmina de bronze intacta e um manto de escamas leves.", "EQUIPAMENTO ATUALIZADO: ataque e guarda aumentaram."], [], "")
		return
	for i in cistern_shard_positions.size():
		if not cistern_shards[i] and player.distance_to(cistern_shard_positions[i]) < 48.0:
			cistern_shards[i] = true
			relics += 1
			inventory_items.append("Eco de Atlântida %d" % relics)
			if i == 1 and not shade_defeated:
				start_battle("Sombra da Cisterna", 20, "shade")
			else:
				show_dialogue("Eco de Atlântida", ["Uma lembrança sem dono toca sua mão.", "Relíquia obtida: Eco %d de 3." % relics], [], "")
			return
	if player.distance_to(cistern_door_position) < 64.0:
		if relics < 3:
			show_dialogue("Porta de Bronze", ["Três círculos vazios esperam por ecos perdidos.", "Você possui %d de 3 relíquias." % relics], [], "")
		else:
			quest_stage = 9
			ariane_affinity += 1
			show_dialogue("Ariane", ["Você ouviu a cidade quando ela pediu silêncio.", "Isso não é poder, Ivo. É responsabilidade.", "FIM DO PRÓLOGO — A rota para Nereu foi revelada."], ["Prometer seguir com Ariane.", "Pedir tempo para entender a marca."], "cistern_ending", "embarrassed")
		return
	notice = "A água esconde passagens. Procure os brilhos azuis."
	notice_time = 1.7

func talk_to(role: String) -> void:
	match role:
		"pension":
			if quest_stage == 0:
				show_dialogue("Lysandra", ["Você dormiu no cais. Isso explica o cheiro e a expressão.", "Kallípolis não é gentil com quem chega sem nome, moedas ou amigos.", "Vai continuar fingindo que sabe aonde vai?"], ["Dizer a verdade: estou perdido.", "Fingir que só procuro trabalho.", "Fazer uma piada e mudar de assunto."], "lysandra_intro")
			else:
				show_dialogue("Lysandra", ["Uma cidade se conhece pelos degraus, Ivo.", "Quem sobe não vê quem ficou embaixo. Quem desce talvez não volte."], [], "")
		"smuggler":
			if quest_stage < 2:
				show_dialogue("Pólemon", ["Você tem cara de quem perdeu tudo antes do almoço.", "Leve esta caixa até o cais e eu pago sete moedas. Não abra."], ["Aceitar o trabalho.", "Perguntar o que há dentro.", "Recusar."], "polemon_job")
			else:
				show_dialogue("Pólemon", ["A caixa ainda está ali. Não faça perguntas que custam mais que o pagamento."], [], "")
		"ariane":
			if quest_stage < 3:
				show_dialogue("Ariane", ["Você está olhando para o telhado errado.", "Ou isso é coragem demais, ou falta de prática."], [], "")
			elif quest_stage == 3:
				show_dialogue("Ariane", ["Você abriu a caixa. Isso foi uma escolha, não um acidente.", "Você podia vender a moeda e sumir. Por que ainda está aqui?"], ["Porque não quero ser a pessoa que foge.", "Os guardas estavam olhando.", "Eu gosto de entradas dramáticas."], "ariane_truth")
			else:
				show_dialogue("Ariane", ["O Coletor está procurando a moeda. Ele não vai perguntar duas vezes.", "Use o que aprendeu: não decida sozinho quando puder pedir ajuda."], [], "")
		"collector":
			if quest_stage >= 4 and quest_stage < 5:
				start_battle()
			else:
				show_dialogue("Coletor", ["Cidadãos sem registro não carregam relíquias.", "Entregue a moeda e ninguém se machuca."], [], "")

func show_dialogue(speaker: String, lines: Array, choices: Array = [], action := "", expression := "neutral") -> void:
	$AudioConfirm.play()
	dialogue_speaker = speaker
	dialogue_lines.assign(lines)
	dialogue_choices.assign(choices)
	dialogue_action = action
	dialogue_expression = expression
	choice_index = 0
	dialogue_open = true

func close_dialogue() -> void:
	dialogue_open = false
	dialogue_lines.clear()
	dialogue_choices.clear()
	dialogue_action = ""

func choose_dialogue() -> void:
	var chosen := dialogue_choices[choice_index]
	match dialogue_action:
		"lysandra_intro":
			quest_stage = max(quest_stage, 1)
			if choice_index == 0:
				show_dialogue("Lysandra", ["Bom. A verdade não compra cama, mas evita que você durma em lugar pior.", "Pólemon procura braços fortes perto da fonte."], [], "")
			elif choice_index == 1:
				show_dialogue("Lysandra", ["Todo mundo procura trabalho. Pouca gente admite que procura uma chance.", "Pólemon está perto da fonte."], [], "")
			else:
				show_dialogue("Lysandra", ["Humor é uma casa sem janela. Um dia você vai precisar sair dela.", "Pólemon está perto da fonte."], [], "")
		"polemon_job":
			if choice_index == 0:
				quest_stage = 2
				show_dialogue("Pólemon", ["Bom senso é raro. Leve a caixa até a marca no cais."], [], "")
			elif choice_index == 1:
				quest_stage = 2
				show_dialogue("Pólemon", ["Dentro? Problema. E problema paga melhor que pão.", "Leve a caixa até a marca no cais."], [], "")
			else:
				show_dialogue("Pólemon", ["Então continue sem moedas. A cidade adora gente orgulhosa."], [], "")
		"ariane_truth":
			quest_stage = 4
			if choice_index == 0:
				ariane_affinity += 1
				show_dialogue("Ariane", ["Você fala como alguém que já deixou pessoas para trás.", "Pelo menos não mentiu agora.", "O Coletor está no cais. Vamos impedir que ele leve a moeda."], [], "", "embarrassed")
			elif choice_index == 1:
				show_dialogue("Ariane", ["Isso não responde à pergunta. Mas responde outra.", "O Coletor está no cais. Não entregue a moeda."], [], "")
			else:
				show_dialogue("Ariane", ["Foi uma resposta ruim.", "Mas não foi covarde.", "O Coletor está no cais. Vamos."], [], "")
		"cistern_ending":
			if choice_index == 0:
				ariane_affinity += 1
				show_dialogue("Ariane", ["Então não me deixe decidir o caminho sozinha.", "Há uma cidade além do mar. E seis nomes presos ao mesmo juramento."], [], "", "embarrassed")
			else:
				show_dialogue("Ariane", ["Tempo não é fuga, se você souber para que está voltando.", "Quando estiver pronto, Nereu estará esperando."], [], "")
		"nerissa_intro":
			if choice_index == 0:
				show_dialogue("Nerissa", ["Atlântida não afundou de uma vez. Primeiro afundou dentro das pessoas.", "Se quer o resto da resposta, prove que sabe carregar uma verdade sem transformá-la em arma."], [], "")
			elif choice_index == 1:
				show_dialogue("Nerissa", ["Ariane sempre chega antes das consequências e depois finge surpresa quando elas a alcançam.", "Ela está segura. Por enquanto."], [], "", "embarrassed")
			else:
				show_dialogue("Nerissa", ["Ótimo. Pessoas muito certas são fáceis de governar e ainda mais fáceis de destruir.", "Quando descobrir o que procura, volte sem ensaiar a resposta."], [], "")

func start_battle(name := "Coletor de Relíquias", max_enemy_health := 18, reward_action := "collector") -> void:
	battle_open = true
	battle_menu = 0
	enemy_name = name
	enemy_max_health = max_enemy_health
	enemy_health = max_enemy_health
	battle_reward_action = reward_action
	resolve = 0
	battle_guarding = false
	combat_message = "%s bloqueia seu caminho. A marca pulsa entre vocês." % enemy_name

func save_game() -> void:
	var save := ConfigFile.new()
	save.set_value("player", "x", player.x)
	save.set_value("player", "y", player.y)
	save.set_value("state", "gold", gold)
	save.set_value("state", "health", health)
	save.set_value("state", "essence", essence)
	save.set_value("state", "magic_unlocked", magic_unlocked)
	save.set_value("equipment", "weapon", equipped_weapon)
	save.set_value("equipment", "armor", equipped_armor)
	save.set_value("equipment", "relic", equipped_relic)
	save.set_value("state", "quest_stage", quest_stage)
	save.set_value("state", "ariane_affinity", ariane_affinity)
	save.set_value("state", "zone", zone)
	save.set_value("state", "relics", relics)
	save.set_value("state", "cistern_shards", cistern_shards)
	save.set_value("state", "shade_defeated", shade_defeated)
	save.set_value("state", "cistern_chest_open", cistern_chest_open)
	save.set_value("state", "inventory_items", inventory_items)
	if save.save(SAVE_PATH) == OK:
		notice = "Jogo salvo."
		notice_time = 2.0

func load_game() -> void:
	var save := ConfigFile.new()
	if save.load(SAVE_PATH) == OK:
		player.x = save.get_value("player", "x", player.x)
		player.y = save.get_value("player", "y", player.y)
		gold = save.get_value("state", "gold", gold)
		health = save.get_value("state", "health", health)
		essence = save.get_value("state", "essence", essence)
		magic_unlocked = save.get_value("state", "magic_unlocked", magic_unlocked)
		equipped_weapon = save.get_value("equipment", "weapon", equipped_weapon)
		equipped_armor = save.get_value("equipment", "armor", equipped_armor)
		equipped_relic = save.get_value("equipment", "relic", equipped_relic)
		quest_stage = save.get_value("state", "quest_stage", quest_stage)
		ariane_affinity = save.get_value("state", "ariane_affinity", ariane_affinity)
		zone = save.get_value("state", "zone", zone)
		relics = save.get_value("state", "relics", relics)
		cistern_shards = save.get_value("state", "cistern_shards", cistern_shards)
		shade_defeated = save.get_value("state", "shade_defeated", shade_defeated)
		cistern_chest_open = save.get_value("state", "cistern_chest_open", cistern_chest_open)
		inventory_items = save.get_value("state", "inventory_items", inventory_items)

func reset_game() -> void:
	player = Vector2(496, 456)
	gold = 7
	health = max_health
	essence = 0
	magic_unlocked = false
	quest_stage = 0
	ariane_affinity = 0
	zone = "kallipolis"
	relics = 0
	resolve = 0
	cistern_shards = [false, false, false]
	shade_defeated = false
	cistern_chest_open = false
	equipped_weapon = "Faca de cais (+2 Ataque)"
	equipped_armor = "Capa de viagem (+1 Guarda)"
	equipped_relic = "Marca das Moiras (selada)"
	inventory_items = ["Pão seco", "Capa molhada"]
	ConfigFile.new().save(SAVE_PATH)
	title_open = false
	sync_world_visibility()
	show_dialogue("Ivo", ["O mar devolve você a Kallípolis.", "Desta vez, a história começa antes da primeira escolha."], [], "")

func quest_text() -> String:
	match quest_stage:
		0, 1: return "Encontre um trabalho em Kallípolis"
		2: return "Leve a caixa ao cais"
		3: return "Descubra quem observa você"
		4: return "Enfrente o Coletor no cais"
		5: return "Entre na Cisterna esquecida"
		6, 7, 8: return "Colete os Ecos de Atlântida (%d/3)" % relics
		9: return "Atravesse a Ágora e siga para Nereu"
		_: return "Descubra o Juramento das Moiras"

func location_name() -> String:
	match zone:
		"inn": return "Pensão dos Degraus"
		"agora": return "Ágora das Colunas"
		"nereu": return "Nereu"
		"cistern": return "Cisterna Esquecida"
		_: return "Kallípolis"

func weapon_bonus() -> int:
	return 4 if equipped_weapon.begins_with("Daga") else 2

func armor_bonus() -> int:
	return 2 if equipped_armor.begins_with("Manto") else 1

func _draw() -> void:
	var font := ThemeDB.fallback_font
	if zone == "cistern" and not title_open:
		draw_cistern(font)
		return
	if zone == "inn" and not title_open:
		draw_inn(font)
		return
	if zone == "agora" and not title_open:
		draw_agora(font)
		return
	if zone == "nereu" and not title_open:
		draw_nereu(font)
		return
	# A single authored environment replaces the former mixed tiles and façade collage.
	draw_texture_rect(KALLIPOLIS_EXTERIOR, Rect2(0, 0, 960, 540), false, Color.WHITE)
	draw_water_shimmer(405.0, 540.0)
	# Crate objective.
	if quest_stage == 2:
		var crate_display := display_position(crate_position)
		draw_art_tile(Vector2i(3, 2), Rect2(crate_display - Vector2(16, 16), Vector2(32, 32)))
		draw_circle(crate_display + Vector2(0, -25), 7, Color("61d7e5"))
	if quest_stage >= 5:
		var gate_display := display_position(cistern_gate_position)
		draw_circle(gate_display, 13.0 + sin(water_phase * 2.0) * 2.0, Color(0.32, 0.88, 0.93, 0.16))
		draw_arc(gate_display, 10.0, 0.0, TAU, 20, Color("7ce8ef"), 2.0)
	# NPCs.
	for npc in npcs:
		var visible: bool = npc["role"] != "pension" and npc["role"] != "smuggler" and (npc["role"] != "ariane" or quest_stage >= 3)
		if visible:
			var npc_position: Vector2 = display_position(npc["position"])
			draw_character(npc_position, npc["sprite"])
	# Player sprite.
	draw_player_character(display_position(player))
	draw_scene_color_grade()
	if title_open:
		draw_title(font)
	elif battle_open:
		draw_battle(font)
	elif gallery_open:
		draw_gallery(font)
	elif inventory_open:
		draw_inventory(font)
	elif map_open:
		draw_map(font)
	elif pause_open:
		draw_pause_menu(font)
	elif dialogue_open:
		draw_dialogue(font)

func draw_inn(font: Font) -> void:
	# A bespoke room illustration provides a coherent floor plan while actors and collisions stay live.
	draw_texture_rect(PENSION_INTERIOR, Rect2(0, 0, 960, 540), false, Color.WHITE)
	draw_character(display_position(inn_lysandra_position), Vector2i(2, 0))
	draw_player_character(display_position(player))
	draw_scene_color_grade()
	if battle_open:
		draw_battle(font)
	elif gallery_open:
		draw_gallery(font)
	elif inventory_open:
		draw_inventory(font)
	elif map_open:
		draw_map(font)
	elif pause_open:
		draw_pause_menu(font)
	elif dialogue_open:
		draw_dialogue(font)

func draw_agora(font: Font) -> void:
	# The second district follows the same authored-map pipeline as the harbor city.
	draw_texture_rect(AGORA_EXTERIOR, Rect2(0, 0, 960, 540), false, Color.WHITE)
	draw_water_shimmer(466.0, 540.0)
	draw_character(display_position(agora_polemon_position), Vector2i(3, 0))
	draw_circle(display_position(agora_notice_board_position) + Vector2(0, -18), 7, Color(0.95, 0.76, 0.34, 0.24 + sin(water_phase * 2.0) * 0.06))
	draw_player_character(display_position(player))
	draw_scene_color_grade()
	if battle_open:
		draw_battle(font)
	elif gallery_open:
		draw_gallery(font)
	elif inventory_open:
		draw_inventory(font)
	elif map_open:
		draw_map(font)
	elif pause_open:
		draw_pause_menu(font)
	elif dialogue_open:
		draw_dialogue(font)

func draw_nereu(font: Font) -> void:
	draw_texture_rect(NEREU_EXTERIOR, Rect2(0, 0, 960, 540), false, Color.WHITE)
	draw_water_shimmer(468.0, 540.0)
	draw_character(display_position(nereu_nerissa_position), Vector2i(1, 0))
	draw_player_character(display_position(player))
	draw_scene_color_grade()
	if battle_open:
		draw_battle(font)
	elif gallery_open:
		draw_gallery(font)
	elif inventory_open:
		draw_inventory(font)
	elif map_open:
		draw_map(font)
	elif pause_open:
		draw_pause_menu(font)
	elif dialogue_open:
		draw_dialogue(font)

func draw_kallipolis_map(font: Font) -> void:
	# This is deliberately a real traversable tile grid, not a painted backdrop.
	for row in TOWN_ROWS:
		for column in TOWN_COLUMNS:
			var map_position := TOWN_ORIGIN + Vector2(column * TILE_SIZE, row * TILE_SIZE)
			var destination := Rect2(map_position, Vector2(TILE_SIZE, TILE_SIZE))
			match town_tile_kind(column, row):
				"water":
					draw_art_tile(Vector2i(3, 0), destination)
				"path":
					draw_art_tile(Vector2i(2, 0), destination)
				"building":
					draw_art_tile(Vector2i(1, 1), destination)
				"tree":
					draw_art_tile(Vector2i(0, 0), destination)
					draw_art_tile(Vector2i(2, 1) if (column + row) % 2 == 0 else Vector2i(3, 1), destination)
				_:
					draw_art_tile(Vector2i(1, 0) if (column + row * 3) % 9 == 0 else Vector2i(0, 0), destination)
	# Roofs are drawn after the grid, making each solid building legible in the play space.
	draw_town_building(Vector2i(5, 2), Vector2i(4, 3), "PENSÃO")
	draw_town_building(Vector2i(11, 2), Vector2i(5, 3), "MERCADO")
	draw_town_building(Vector2i(20, 3), Vector2i(5, 3), "FAROL")
	# Fountain plaza and a small pier make the city navigable landmarks instead of floating labels.
	draw_art_tile(Vector2i(2, 2), Rect2(TOWN_ORIGIN + Vector2(14 * TILE_SIZE, 7 * TILE_SIZE), Vector2(TILE_SIZE, TILE_SIZE)))
	for pier_x in range(3, 8):
		var pier_position := TOWN_ORIGIN + Vector2(pier_x * TILE_SIZE, 11 * TILE_SIZE)
		draw_art_tile(Vector2i(1, 2), Rect2(pier_position, Vector2(TILE_SIZE, TILE_SIZE)))
	draw_string(font, TOWN_ORIGIN + Vector2(55, 429), "CAIS DAS ONDAS", HORIZONTAL_ALIGNMENT_LEFT, -1, 12, Color("d9eff1"))

func draw_town_building(origin: Vector2i, size: Vector2i, label: String) -> void:
	for column in range(origin.x, origin.x + size.x):
		var roof_position := TOWN_ORIGIN + Vector2(column * TILE_SIZE, origin.y * TILE_SIZE)
		draw_art_tile(Vector2i(0, 1), Rect2(roof_position, Vector2(TILE_SIZE, TILE_SIZE)))
	var label_position := TOWN_ORIGIN + Vector2((origin.x + size.x * 0.5) * TILE_SIZE, (origin.y + size.y) * TILE_SIZE + 15)
	draw_rect(Rect2(label_position + Vector2(-43, -17), Vector2(86, 15)), Color(0.015, 0.03, 0.07, 0.82))
	draw_string(ThemeDB.fallback_font, label_position + Vector2(-39, -5), label, HORIZONTAL_ALIGNMENT_CENTER, 78, 10, Color("fff0cf"))

func draw_art_tile(slot: Vector2i, destination: Rect2) -> void:
	var source := Rect2(ART_SOURCE_ORIGINS[slot.x], ART_SOURCE_ORIGINS[slot.y], ART_SOURCE_SIZE.x, ART_SOURCE_SIZE.y)
	draw_texture_rect_region(KALLIPOLIS_TILESET, destination, source, Color.WHITE)

func draw_cistern(font: Font) -> void:
	draw_cistern_map()
	for i in cistern_shard_positions.size():
		if not cistern_shards[i]:
			var shard: Vector2 = display_position(cistern_shard_positions[i])
			draw_circle(shard, 13, Color(0.2, 0.95, 1.0, 0.25))
			draw_circle(shard, 7, Color("9ef9ff"))
			draw_line(shard + Vector2(0, -20), shard + Vector2(0, 20), Color("d9ffff"), 2.0)
	var door_display := display_position(cistern_door_position)
	var exit_display := display_position(cistern_exit_position)
	draw_rect(Rect2(door_display - Vector2(26, 44), Vector2(52, 72)), Color(0.2, 0.12, 0.08, 0.8))
	draw_arc(door_display - Vector2(0, 20), 26, PI, TAU, 20, Color("d7a75d"), 3.0)
	draw_rect(Rect2(exit_display - Vector2(25, 18), Vector2(50, 36)), Color(0.05, 0.08, 0.13, 0.9))
	if not cistern_chest_open:
		var chest_display := display_position(cistern_chest_position)
		draw_rect(Rect2(chest_display - Vector2(17, 12), Vector2(34, 24)), Color("7a4e2e"))
		draw_rect(Rect2(chest_display - Vector2(17, 12), Vector2(34, 24)), Color("dfb55f"), false, 2.0)
	draw_player_character(display_position(player))
	draw_scene_color_grade()
	if battle_open:
		draw_battle(font)
	elif gallery_open:
		draw_gallery(font)
	elif inventory_open:
		draw_inventory(font)
	elif map_open:
		draw_map(font)
	elif pause_open:
		draw_pause_menu(font)
	elif dialogue_open:
		draw_dialogue(font)

func draw_cistern_map() -> void:
	for row in TOWN_ROWS:
		for column in TOWN_COLUMNS:
			var map_position := display_position(TOWN_ORIGIN + Vector2(column * TILE_SIZE, row * TILE_SIZE))
			var destination := Rect2(map_position, Vector2(TILE_SIZE, TILE_SIZE))
			if cistern_tile_kind(column, row) == "wall":
				draw_art_tile(Vector2i(1, 3), destination)
			else:
				draw_art_tile(Vector2i(3, 3), destination)
	for torch_position in [Vector2(208, 214), Vector2(592, 246), Vector2(784, 374)]:
		draw_art_tile(Vector2i(2, 3), Rect2(display_position(torch_position) - Vector2(16, 16), Vector2(32, 32)))

func draw_hud(font: Font, location: String) -> void:
	draw_rect(Rect2(20, 16, 920, 56), Color(0.015, 0.03, 0.075, 0.92))
	draw_rect(Rect2(20, 16, 920, 56), Color("7db8ca"), false, 1.5)
	draw_string(font, Vector2(38, 40), location, HORIZONTAL_ALIGNMENT_LEFT, 230, 19, Color("f8edcf"))
	draw_string(font, Vector2(38, 61), "Vida %d/%d  •  Essência %d/%d  •  Ouro %d" % [health, max_health, essence, max_essence, gold], HORIZONTAL_ALIGNMENT_LEFT, 310, 14, Color("d5e8ec"))
	draw_rect(Rect2(600, 25, 320, 38), Color(0.08, 0.13, 0.22, 0.9))
	draw_string(font, Vector2(616, 42), "OBJETIVO", HORIZONTAL_ALIGNMENT_LEFT, -1, 12, Color("e9c87e"))
	draw_string(font, Vector2(616, 58), quest_text(), HORIZONTAL_ALIGNMENT_LEFT, 286, 14, Color("f5f7fb"))

func draw_controls(font: Font) -> void:
	draw_rect(Rect2(246, 501, 468, 25), Color(0.01, 0.02, 0.05, 0.78))
	draw_string(font, Vector2(260, 519), "WASD mover  •  E interagir  •  I bolsa  •  J vínculos  •  F5 salvar", HORIZONTAL_ALIGNMENT_LEFT, -1, 13, Color("e3e8f3"))

func display_position(world_position: Vector2) -> Vector2:
	return world_position + GAMEPLAY_RENDER_OFFSET

func draw_character(position: Vector2, slot: Vector2i) -> void:
	var source := Rect2(slot.x * CHARACTER_CELL_SIZE.x, slot.y * CHARACTER_CELL_SIZE.y, CHARACTER_CELL_SIZE.x, CHARACTER_CELL_SIZE.y)
	draw_sprite_shadow(position + Vector2(0, 6), Vector2(14, 4), Color(0.01, 0.02, 0.04, 0.35))
	draw_texture_rect_region(KALLIPOLIS_CHARACTER_SHEET, Rect2(position - CHARACTER_DRAW_OFFSET, CHARACTER_DRAW_SIZE), source, Color.WHITE)

func draw_kallipolis_environment() -> void:
	var tree_cells := [
		Vector2i(3, 2), Vector2i(4, 2), Vector2i(3, 3), Vector2i(9, 2),
		Vector2i(18, 2), Vector2i(19, 2), Vector2i(25, 2), Vector2i(26, 3),
		Vector2i(4, 12), Vector2i(5, 12), Vector2i(24, 11), Vector2i(25, 11), Vector2i(27, 10)
	]
	for index in tree_cells.size():
		var cell: Vector2i = tree_cells[index]
		var foot := display_position(Vector2(cell.x * TILE_SIZE + 16, TOWN_ORIGIN.y + cell.y * TILE_SIZE + 29))
		if index % 3 == 0:
			draw_environment_sprite(foot, Vector2i(index % 4, 0), Vector2(100, 100), Vector2(50, 91))
		else:
			draw_environment_sprite(foot, Vector2i(index % 4, 1), Vector2(72, 108), Vector2(36, 100))
	for shrub_data in [
		[Vector2i(3, 6), Vector2i(0, 2)], [Vector2i(9, 9), Vector2i(1, 2)],
		[Vector2i(18, 10), Vector2i(2, 2)], [Vector2i(26, 7), Vector2i(3, 2)],
		[Vector2i(10, 12), Vector2i(1, 2)]
	]:
		var shrub_cell: Vector2i = shrub_data[0]
		var shrub_foot := display_position(Vector2(shrub_cell.x * TILE_SIZE + 16, TOWN_ORIGIN.y + shrub_cell.y * TILE_SIZE + 28))
		draw_environment_sprite(shrub_foot, shrub_data[1], Vector2(56, 56), Vector2(28, 51))

func draw_environment_sprite(foot_position: Vector2, slot: Vector2i, draw_size: Vector2, offset: Vector2) -> void:
	var source := Rect2(slot.x * ENVIRONMENT_CELL_SIZE.x, slot.y * ENVIRONMENT_CELL_SIZE.y, ENVIRONMENT_CELL_SIZE.x, ENVIRONMENT_CELL_SIZE.y)
	draw_sprite_shadow(foot_position + Vector2(0, 2), Vector2(draw_size.x * 0.22, 4), Color(0.01, 0.02, 0.03, 0.28))
	draw_texture_rect_region(KALLIPOLIS_ENVIRONMENT_SHEET, Rect2(foot_position - offset, draw_size), source, Color.WHITE)

func draw_player_character(position: Vector2) -> void:
	var direction_row := 0
	if absf(player_facing.x) > absf(player_facing.y):
		direction_row = 1 if player_facing.x < 0.0 else 2
	elif player_facing.y < 0.0:
		direction_row = 3
	var frame := posmod(int(floor(walk_phase)), 4) if player_moving else 0
	var source := Rect2(frame * IVO_WALK_CELL_SIZE.x, IVO_WALK_ROW_ORIGINS[direction_row], IVO_WALK_CELL_SIZE.x, IVO_WALK_ROW_HEIGHTS[direction_row])
	var step := absf(sin(walk_phase * PI * 0.5)) if player_moving else 0.0
	var bob := -roundf(step * 1.5)
	var shadow_width := lerpf(14.0, 17.0, step)
	draw_sprite_shadow(position + Vector2(0, 1), Vector2(shadow_width, 3), Color(0.01, 0.02, 0.04, 0.34))
	var destination := Rect2(position - Vector2(48, IVO_WALK_FOOT_OFFSETS[direction_row]) + Vector2(0, bob), IVO_WALK_DRAW_SIZE)
	draw_texture_rect_region(IVO_WALK_SHEET, destination, source, Color.WHITE)
	if player_moving and step > 0.86:
		var dust_direction := Vector2(-signf(player_facing.x), 0.4).normalized()
		draw_circle(position + dust_direction * Vector2(11, 5) + Vector2(0, 3), 2.0, Color(0.78, 0.68, 0.48, 0.32))

func draw_nameplate(font: Font, position: Vector2, character_name: String) -> void:
	draw_rect(Rect2(position + Vector2(-37, -71), Vector2(74, 16)), Color(0.02, 0.04, 0.09, 0.82))
	draw_string(font, position + Vector2(-33, -59), character_name, HORIZONTAL_ALIGNMENT_CENTER, 66, 12, Color.WHITE)

func draw_sprite_shadow(center: Vector2, radii: Vector2, color: Color) -> void:
	if not shadows_enabled:
		return
	var points := PackedVector2Array()
	for index in range(13):
		var angle := TAU * float(index) / 12.0
		points.append(center + Vector2(cos(angle) * radii.x, sin(angle) * radii.y))
	draw_colored_polygon(points, color)

func draw_water_shimmer(surface_y: float, bottom_y: float) -> void:
	if not water_effects_enabled:
		return
	for row in range(4):
		var y := lerpf(surface_y + 13.0, bottom_y - 18.0, float(row) / 3.0)
		var points := PackedVector2Array()
		for column in range(33):
			var x := float(column) * 30.0
			var wave := sin(column * 0.82 + water_phase * (1.1 + row * 0.12)) * (1.3 + row * 0.35)
			points.append(Vector2(x, y + wave))
		draw_polyline(points, Color(0.62, 0.94, 0.94, 0.055 + row * 0.012), 1.0, true)

func draw_scene_color_grade() -> void:
	if warm_lighting_enabled:
		draw_rect(Rect2(0, 0, 960, 540), Color(1.0, 0.72, 0.38, 0.025))
	if brightness_percent < 100:
		var darkness := float(100 - brightness_percent) / 100.0 * 0.72
		draw_rect(Rect2(0, 0, 960, 540), Color(0.01, 0.02, 0.05, darkness))
	elif brightness_percent > 100:
		var lift := float(brightness_percent - 100) / 100.0 * 0.32
		draw_rect(Rect2(0, 0, 960, 540), Color(1.0, 0.93, 0.78, lift))

func draw_pixel_person(position: Vector2, hair: Color, clothes: Color) -> void:
	# Sprite procedural em grade de pixels: fácil de substituir por spritesheets finais sem mudar o gameplay.
	var pixel := 3.0
	draw_rect(Rect2(position + Vector2(-6, -22), Vector2(12, 6)), hair)
	draw_rect(Rect2(position + Vector2(-9, -16), Vector2(18, 12)), Color("f2c797"))
	draw_rect(Rect2(position + Vector2(-7, -13), Vector2(3, 3)), Color("2a2530"))
	draw_rect(Rect2(position + Vector2(4, -13), Vector2(3, 3)), Color("2a2530"))
	draw_rect(Rect2(position + Vector2(-9, -4), Vector2(18, 17)), clothes)
	draw_rect(Rect2(position + Vector2(-12, 0), Vector2(3, 12)), Color("f2c797"))
	draw_rect(Rect2(position + Vector2(9, 0), Vector2(3, 12)), Color("f2c797"))
	draw_rect(Rect2(position + Vector2(-7, 13), Vector2(5, 7)), Color("263244"))
	draw_rect(Rect2(position + Vector2(2, 13), Vector2(5, 7)), Color("263244"))

func draw_title(font: Font) -> void:
	draw_texture_rect(KALLIPOLIS_OPENING, Rect2(0, 0, 960, 540), false, Color.WHITE)
	draw_rect(Rect2(0, 0, 960, 540), Color(0.02, 0.03, 0.09, 0.28))
	draw_rect(Rect2(0, 362, 960, 178), Color(0.015, 0.02, 0.06, 0.75))
	draw_string(font, Vector2(67, 100), "UM JURAMENTO", HORIZONTAL_ALIGNMENT_LEFT, -1, 18, Color("e7d4a4"))
	draw_string(font, Vector2(62, 159), "HERDEIRAS", HORIZONTAL_ALIGNMENT_LEFT, -1, 47, Color("fff3d4"))
	draw_string(font, Vector2(65, 205), "DE ATLÂNTIDA", HORIZONTAL_ALIGNMENT_LEFT, -1, 35, Color("a9daf0"))
	draw_string(font, Vector2(65, 253), "O mar devolveu o que os deuses esconderam.", HORIZONTAL_ALIGNMENT_LEFT, -1, 18, Color("f6eed9"))
	draw_string(font, Vector2(64, 408), "Ivo acorda sem nome, sem aliados e com uma marca que não lhe pertence.", HORIZONTAL_ALIGNMENT_LEFT, -1, 17, Color("d8e0ec"))
	draw_string(font, Vector2(64, 438), "Em Kallípolis, cada promessa deixa uma cicatriz.", HORIZONTAL_ALIGNMENT_LEFT, -1, 17, Color("d8e0ec"))
	draw_string(font, Vector2(64, 485), "[E] continuar jornada", HORIZONTAL_ALIGNMENT_LEFT, -1, 20, Color("ffdf92"))
	draw_string(font, Vector2(64, 514), "[R] novo jogo", HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("d7e7f4"))

func draw_map(font: Font) -> void:
	draw_rect(Rect2(42, 30, 876, 480), Color(0.02, 0.035, 0.075, 0.97))
	draw_rect(Rect2(42, 30, 876, 480), Color("83c8d6"), false, 2.0)
	draw_string(font, Vector2(78, 76), "MAPA: " + location_name().to_upper(), HORIZONTAL_ALIGNMENT_LEFT, -1, 27, Color("f6e7bf"))
	draw_string(font, Vector2(78, 106), "Objetivo atual: " + quest_text(), HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("e4edf3"))
	# A clean schematic is more readable than labels floating over the play space.
	draw_rect(Rect2(88, 142, 488, 290), Color("152942"))
	draw_rect(Rect2(106, 310, 434, 36), Color("b48a57"))
	draw_rect(Rect2(304, 168, 38, 228), Color("b48a57"))
	draw_rect(Rect2(106, 346, 82, 86), Color("1f6f91"))
	draw_rect(Rect2(480, 142, 60, 76), Color("1f6f91"))
	for landmark in [Vector2(228, 246), Vector2(322, 278), Vector2(433, 246), Vector2(507, 332)]:
		draw_circle(landmark, 10, Color("f1c96a"))
	draw_circle(Vector2(322, 343), 7, Color("7ee6f1"))
	draw_string(font, Vector2(624, 166), "REGISTRO", HORIZONTAL_ALIGNMENT_LEFT, -1, 17, Color("e9c97e"))
	draw_string(font, Vector2(624, 202), "Vida %d/%d" % [health, max_health], HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("eaf2f6"))
	draw_string(font, Vector2(624, 229), "Essência %d/%d" % [essence, max_essence], HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("eaf2f6"))
	draw_string(font, Vector2(624, 256), "Ouro %d" % gold, HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("eaf2f6"))
	draw_string(font, Vector2(624, 312), "M: fechar mapa", HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color("c9d7e5"))
	draw_string(font, Vector2(624, 338), "I: bolsa   J: vínculos", HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color("c9d7e5"))
	draw_string(font, Vector2(624, 364), "Esc: pausa e tela", HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color("c9d7e5"))
	draw_string(font, Vector2(78, 476), "M ou Esc para voltar", HORIZONTAL_ALIGNMENT_LEFT, -1, 15, Color("f4d890"))

func draw_pause_menu(font: Font) -> void:
	if settings_open:
		draw_graphics_menu(font)
		return
	draw_rect(Rect2(0, 0, 960, 540), Color(0.01, 0.02, 0.05, 0.54))
	draw_rect(Rect2(244, 76, 472, 388), Color(0.025, 0.045, 0.09, 0.985))
	draw_rect(Rect2(244, 76, 472, 388), Color("7fc8d8"), false, 2.0)
	draw_string(font, Vector2(286, 124), "JORNADA PAUSADA", HORIZONTAL_ALIGNMENT_LEFT, -1, 27, Color("f6e7bf"))
	draw_string(font, Vector2(286, 151), location_name() + " continua respirando ao seu redor.", HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color("bcd3df"))
	var options := ["Continuar", "Configurações gráficas", "Salvar jornada", "Voltar ao título"]
	for index in options.size():
		var row := Rect2(278, 182 + index * 52, 404, 42)
		var selected := index == pause_selection
		draw_rect(row, Color("173653") if selected else Color("0c1c32"))
		if selected:
			draw_rect(Rect2(row.position, Vector2(5, row.size.y)), Color("edc66e"))
		draw_string(font, row.position + Vector2(20, 28), (">  " if selected else "   ") + options[index], HORIZONTAL_ALIGNMENT_LEFT, 360, 17, Color("fff1cc") if selected else Color("dbe8ef"))
	draw_string(font, Vector2(286, 430), "W/S escolher  •  E confirmar  •  Esc continuar", HORIZONTAL_ALIGNMENT_LEFT, -1, 13, Color("9fb9c8"))

func draw_graphics_menu(font: Font) -> void:
	draw_rect(Rect2(0, 0, 960, 540), Color(0.005, 0.012, 0.03, 0.68))
	draw_rect(Rect2(132, 22, 696, 496), Color(0.022, 0.04, 0.082, 0.995))
	draw_rect(Rect2(132, 22, 696, 496), Color("79c8d8"), false, 2.0)
	draw_string(font, Vector2(170, 66), "CONFIGURAÇÕES GRÁFICAS", HORIZONTAL_ALIGNMENT_LEFT, -1, 26, Color("f7e5b8"))
	draw_string(font, Vector2(170, 91), "A imagem permanece em 16:9 e se adapta sem deformar.", HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color("bcd2df"))
	var labels := ["Modo de exibição", "Resolução", "Escala da arte", "Sincronização vertical", "Sombras dos personagens", "Reflexos da água", "Luz mediterrânea", "Brilho"]
	var values := [
		DISPLAY_MODE_LABELS[display_mode_index],
		RESOLUTION_LABELS[resolution_index],
		SCALE_MODE_LABELS[scale_mode_index],
		"Ligada" if vsync_enabled else "Desligada",
		"Ligadas" if shadows_enabled else "Desligadas",
		"Ligados" if water_effects_enabled else "Desligados",
		"Ligada" if warm_lighting_enabled else "Desligada",
		"%d%%" % brightness_percent,
	]
	for index in labels.size():
		var row := Rect2(164, 112 + index * 43, 632, 35)
		var selected := index == settings_selection
		draw_rect(row, Color("173b59") if selected else Color("0b1b31"))
		if selected:
			draw_rect(Rect2(row.position, Vector2(4, row.size.y)), Color("edc66e"))
		draw_string(font, row.position + Vector2(17, 24), labels[index], HORIZONTAL_ALIGNMENT_LEFT, 330, 15, Color("f5efd9") if selected else Color("d5e2ea"))
		draw_string(font, row.position + Vector2(360, 24), "<  %s  >" % values[index], HORIZONTAL_ALIGNMENT_CENTER, 245, 15, Color("ffdc87") if selected else Color("a9c8d4"))
	draw_string(font, Vector2(170, 489), "W/S selecionar  •  A/D ou E alterar  •  Esc voltar", HORIZONTAL_ALIGNMENT_LEFT, -1, 13, Color("a5bdca"))

func draw_gallery(font: Font) -> void:
	var heroine: Dictionary = heroines[gallery_index]
	draw_rect(Rect2(30, 32, 900, 476), Color(0.03, 0.04, 0.08, 0.98))
	draw_rect(Rect2(30, 32, 900, 476), heroine["color"], false, 3.0)
	draw_string(font, Vector2(62, 74), "VÍNCULOS DE ATLÂNTIDA", HORIZONTAL_ALIGNMENT_LEFT, -1, 24, Color("f5e7c9"))
	draw_string(font, Vector2(63, 108), "Arquivo de Vínculos: futuros encontros serão registrados aqui conforme a jornada avança.", HORIZONTAL_ALIGNMENT_LEFT, -1, 15, Color("cdd4e1"))
	for i in heroines.size():
		var candidate: Dictionary = heroines[i]
		var y := 151 + i * 43
		var selected := i == gallery_index
		draw_rect(Rect2(57, y - 25, 310, 34), candidate["color"] if selected else Color("20283a"), selected)
		draw_string(font, Vector2(74, y), ("▶ " if selected else "  ") + candidate["name"], HORIZONTAL_ALIGNMENT_LEFT, -1, 19, Color.WHITE)
		draw_string(font, Vector2(247, y), "%d anos" % candidate["age"], HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color("e1e5ec"))
	var gallery_portrait: Texture2D = heroine["portrait"] if gallery_expression == 0 else heroine["embarrassed"]
	draw_texture_rect(gallery_portrait, Rect2(568, 105, 275, 360), false, Color.WHITE)
	draw_string(font, Vector2(400, 160), heroine["name"].to_upper(), HORIZONTAL_ALIGNMENT_LEFT, -1, 25, heroine["color"])
	draw_string(font, Vector2(400, 193), heroine["role"], HORIZONTAL_ALIGNMENT_LEFT, -1, 17, Color("edf1f7"))
	var expression_label := "neutra" if gallery_expression == 0 else "envergonhada"
	draw_string(font, Vector2(400, 238), "Expressão em exibição: " + expression_label, HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("f0d69a"))
	draw_string(font, Vector2(400, 265), "neutra • feliz • irritada • triste", HORIZONTAL_ALIGNMENT_LEFT, -1, 15, Color("d3dae7"))
	draw_string(font, Vector2(400, 288), "surpresa • envergonhada • determinada", HORIZONTAL_ALIGNMENT_LEFT, -1, 15, Color("d3dae7"))
	draw_string(font, Vector2(400, 311), "vulnerável", HORIZONTAL_ALIGNMENT_LEFT, -1, 15, Color("d3dae7"))
	draw_string(font, Vector2(600, 492), "A/D: heroína | W/S: expressão | E/J: voltar", HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color("d1d9e8"))

func draw_inventory(font: Font) -> void:
	draw_rect(Rect2(170, 72, 620, 400), Color(0.025, 0.035, 0.08, 0.98))
	draw_rect(Rect2(170, 72, 620, 400), Color("d5b46d"), false, 3.0)
	draw_string(font, Vector2(208, 118), "BOLSA DE IVO", HORIZONTAL_ALIGNMENT_LEFT, -1, 27, Color("f7e6bf"))
	draw_string(font, Vector2(208, 155), "Vida: %d/%d    Essência: %d/%d    Ouro: %d" % [health, max_health, essence, max_essence, gold], HORIZONTAL_ALIGNMENT_LEFT, -1, 18, Color("d7e6ee"))
	draw_string(font, Vector2(208, 187), "Arma: " + equipped_weapon, HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("ffd78d"))
	draw_string(font, Vector2(208, 213), "Armadura: " + equipped_armor, HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("d1dced"))
	draw_string(font, Vector2(208, 239), "Relíquia: " + equipped_relic, HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("9ee8ef"))
	draw_line(Vector2(208, 252), Vector2(750, 252), Color("4f607b"), 2.0)
	for i in inventory_items.size():
		draw_rect(Rect2(210, 270 + i * 31, 500, 24), Color("172239"))
		draw_string(font, Vector2(226, 290 + i * 31), "• " + inventory_items[i], HORIZONTAL_ALIGNMENT_LEFT, -1, 17, Color("edf1f7"))
	draw_string(font, Vector2(559, 442), "[I/E] fechar", HORIZONTAL_ALIGNMENT_LEFT, -1, 15, Color("ffd888"))

func draw_dialogue(font: Font) -> void:
	var rendered_lines := wrap_dialogue_lines(76)
	var choice_height := dialogue_choices.size() * 21 + 28 if not dialogue_choices.is_empty() else 28
	var panel_height := maxf(164.0, 78.0 + rendered_lines.size() * 23.0 + choice_height)
	var panel_y := 512.0 - panel_height
	draw_rect(Rect2(28, panel_y, 904, panel_height), Color(0.02, 0.03, 0.07, 0.97))
	draw_rect(Rect2(28, panel_y, 904, panel_height), Color("d5b46d"), false, 2.0)
	draw_string(font, Vector2(58, panel_y + 33), dialogue_speaker.to_upper(), HORIZONTAL_ALIGNMENT_LEFT, 650, 18, Color("f2cd7e"))
	for i in rendered_lines.size():
		draw_string(font, Vector2(58, panel_y + 63 + i * 23), rendered_lines[i], HORIZONTAL_ALIGNMENT_LEFT, 650, 16, Color("f8f2e7"))
	var portrait_y := maxf(20.0, panel_y - 240.0)
	if dialogue_speaker == "Ariane":
		var ariane_expression: Texture2D = ARIANE_EMBARRASSED_PORTRAIT if dialogue_expression == "embarrassed" else ARIANE_PORTRAIT
		draw_texture_rect(ariane_expression, Rect2(748, portrait_y, 150, 240), false, Color.WHITE)
	elif dialogue_speaker == "Nerissa":
		var nerissa_expression: Texture2D = NERISSA_EMBARRASSED_PORTRAIT if dialogue_expression == "embarrassed" else NERISSA_PORTRAIT
		draw_texture_rect(nerissa_expression, Rect2(748, portrait_y, 150, 240), false, Color.WHITE)
	if dialogue_choices.is_empty():
		draw_string(font, Vector2(800, panel_y + panel_height - 22), "[E] continuar", HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color("d5b46d"))
	else:
		var start_y := panel_y + 73 + rendered_lines.size() * 23
		for i in dialogue_choices.size():
			var color := Color("ffdf92") if i == choice_index else Color("e5e8f1")
			var marker := "▶ " if i == choice_index else "  "
			draw_string(font, Vector2(58, start_y + i * 21), marker + dialogue_choices[i], HORIZONTAL_ALIGNMENT_LEFT, 610, 14, color)

func wrap_dialogue_lines(max_characters: int) -> Array[String]:
	var result: Array[String] = []
	for original in dialogue_lines:
		var current := ""
		for raw_word in original.split(" "):
			var word: String = raw_word
			var candidate := word if current.is_empty() else current + " " + word
			if candidate.length() > max_characters and not current.is_empty():
				result.append(current)
				current = word
			else:
				current = candidate
		if not current.is_empty():
			result.append(current)
	return result

func draw_battle(font: Font) -> void:
	draw_rect(Rect2(90, 110, 780, 340), Color(0.03, 0.04, 0.08, 0.97))
	draw_rect(Rect2(90, 110, 780, 340), Color("ba7782"), false, 3.0)
	draw_string(font, Vector2(122, 152), "ENCONTRO: " + enemy_name.to_upper(), HORIZONTAL_ALIGNMENT_LEFT, -1, 23, Color("f4d2d2"))
	draw_circle(Vector2(692, 248), 48, Color("9d4d58"))
	draw_rect(Rect2(650, 282, 84, 54), Color("343246"))
	draw_string(font, Vector2(570, 368), "%s  HP: %d/%d" % [enemy_name, enemy_health, enemy_max_health], HORIZONTAL_ALIGNMENT_LEFT, -1, 17, Color.WHITE)
	draw_string(font, Vector2(122, 220), combat_message, HORIZONTAL_ALIGNMENT_LEFT, 420, 18, Color("e7eaf2"))
	var attack_color := Color("ffe099") if battle_menu == 0 else Color("e6e9f2")
	var defend_color := Color("ffe099") if battle_menu == 1 else Color("e6e9f2")
	var focus_color := Color("ffe099") if battle_menu == 2 else Color("e6e9f2")
	var magic_color := Color("9feeff") if battle_menu == 3 else Color("e6e9f2")
	draw_string(font, Vector2(130, 308), ("▶ " if battle_menu == 0 else "  ") + "ATACAR", HORIZONTAL_ALIGNMENT_LEFT, -1, 19, attack_color)
	draw_string(font, Vector2(130, 340), ("▶ " if battle_menu == 1 else "  ") + "DEFENDER", HORIZONTAL_ALIGNMENT_LEFT, -1, 19, defend_color)
	draw_string(font, Vector2(130, 372), ("▶ " if battle_menu == 2 else "  ") + "FOCAR  (Foco: %d)" % resolve, HORIZONTAL_ALIGNMENT_LEFT, -1, 19, focus_color)
	if magic_unlocked:
		draw_string(font, Vector2(130, 404), ("▶ " if battle_menu == 3 else "  ") + "RESSONÂNCIA  (%d Essência)" % essence, HORIZONTAL_ALIGNMENT_LEFT, -1, 19, magic_color)
	draw_string(font, Vector2(124, 432), "W/S: escolher  |  E: agir", HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color("b9c1d5"))
