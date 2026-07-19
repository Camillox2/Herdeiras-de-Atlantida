extends Node2D

const SPEED := 190.0
const WORLD := Rect2(28, 70, 904, 410)
const SAVE_PATH := "user://otherworld_save.cfg"
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

var player := Vector2(480, 410)
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
var title_open := true
var inventory_items: Array[String] = ["Pão seco", "Capa molhada"]

var cistern_shard_positions := [Vector2(265, 370), Vector2(505, 300), Vector2(748, 245)]
var cistern_door_position := Vector2(840, 150)
var cistern_exit_position := Vector2(104, 452)
var cistern_gate_position := Vector2(895, 420)
var cistern_chest_position := Vector2(456, 420)

var heroines := [
	{"name": "Ariane", "age": 18, "role": "Mensageira e ladra", "color": Color("4f87c8"), "portrait": ARIANE_PORTRAIT, "embarrassed": ARIANE_EMBARRASSED_PORTRAIT},
	{"name": "Mélia", "age": 20, "role": "Botânica de Asterion", "color": Color("5d9c69"), "portrait": MELIA_PORTRAIT, "embarrassed": MELIA_EMBARRASSED_PORTRAIT},
	{"name": "Lyra", "age": 21, "role": "Sacerdotisa e cantora", "color": Color("d3a64b"), "portrait": LYRA_PORTRAIT, "embarrassed": LYRA_EMBARRASSED_PORTRAIT},
	{"name": "Thalia", "age": 22, "role": "Guerreira da arena", "color": Color("c85a58"), "portrait": THALIA_PORTRAIT, "embarrassed": THALIA_EMBARRASSED_PORTRAIT},
	{"name": "Cassia", "age": 23, "role": "Princesa exilada", "color": Color("765a9e"), "portrait": CASSIA_PORTRAIT, "embarrassed": CASSIA_EMBARRASSED_PORTRAIT},
	{"name": "Nerissa", "age": 25, "role": "Capitã de Nereu", "color": Color("9ebed4"), "portrait": NERISSA_PORTRAIT, "embarrassed": NERISSA_EMBARRASSED_PORTRAIT},
]

var npcs := [
	{"name": "Lysandra", "position": Vector2(205, 230), "color": Color("b88963"), "role": "pension"},
	{"name": "Pólemon", "position": Vector2(496, 214), "color": Color("cfa24d"), "role": "smuggler"},
	{"name": "Ariane", "position": Vector2(760, 214), "color": Color("4f87c8"), "role": "ariane"},
	{"name": "Coletor", "position": Vector2(745, 386), "color": Color("9d4d58"), "role": "collector"},
]

var crate_position := Vector2(560, 368)

func _ready() -> void:
	load_game()
	queue_redraw()

func _process(delta: float) -> void:
	if notice_time > 0.0:
		notice_time -= delta
	if title_open:
		if Input.is_action_just_pressed("interact"):
			title_open = false
			$AudioConfirm.play()
	elif battle_open:
		handle_battle_input()
	elif gallery_open:
		handle_gallery_input()
	elif inventory_open:
		handle_inventory_input()
	elif dialogue_open:
		handle_dialogue_input()
	else:
		var direction := Input.get_vector("move_left", "move_right", "move_up", "move_down")
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
	queue_redraw()

func try_move_player(motion: Vector2) -> void:
	var candidate := player + motion
	candidate.x = clampf(candidate.x, WORLD.position.x + 12.0, WORLD.end.x - 12.0)
	candidate.y = clampf(candidate.y, WORLD.position.y + 12.0, WORLD.end.y - 12.0)
	if can_walk_to(candidate):
		player = candidate

func can_walk_to(candidate: Vector2) -> bool:
	if zone == "kallipolis":
		var city_obstacles := [Rect2(50, 92, 230, 115), Rect2(357, 98, 214, 86), Rect2(650, 86, 254, 110)]
		for obstacle in city_obstacles:
			if obstacle.grow(8.0).has_point(candidate):
				return false
	return true

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

func handle_dialogue_input() -> void:
	if not dialogue_choices.is_empty():
		if Input.is_action_just_pressed("move_up"):
			choice_index = posmod(choice_index - 1, dialogue_choices.size())
		if Input.is_action_just_pressed("move_down"):
			choice_index = posmod(choice_index + 1, dialogue_choices.size())
		if Input.is_action_just_pressed("interact"):
			choose_dialogue()
	elif Input.is_action_just_pressed("interact"):
		close_dialogue()

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
	if quest_stage >= 5 and player.distance_to(cistern_gate_position) < 58.0:
		zone = "cistern"
		quest_stage = max(quest_stage, 6)
		player = Vector2(110, 420)
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

func interact_cistern() -> void:
	if player.distance_to(cistern_exit_position) < 58.0:
		zone = "kallipolis"
		player = Vector2(850, 400)
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
				show_dialogue("Ariane", ["Você abriu a caixa. Isso foi uma escolha, não um acidente.", "Por que voltou para salvar a criança da cisterna?"], ["Eu teria sabido se tivesse ido embora.", "Os guardas estavam olhando.", "Eu gosto de entradas dramáticas."], "ariane_truth")
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

func quest_text() -> String:
	match quest_stage:
		0, 1: return "Encontre um trabalho em Kallípolis"
		2: return "Leve a caixa ao cais"
		3: return "Descubra quem observa você"
		4: return "Enfrente o Coletor no cais"
		5: return "Entre na Cisterna esquecida"
		6, 7, 8: return "Colete os Ecos de Atlântida (%d/3)" % relics
		9: return "Prólogo concluído: siga Ariane"
		_: return "Descubra o Juramento das Moiras"

func weapon_bonus() -> int:
	return 4 if equipped_weapon.begins_with("Daga") else 2

func armor_bonus() -> int:
	return 2 if equipped_armor.begins_with("Manto") else 1

func _draw() -> void:
	var font := ThemeDB.fallback_font
	if zone == "cistern" and not title_open:
		draw_cistern(font)
		return
	draw_texture_rect(KALLIPOLIS_OPENING, Rect2(0, 0, 960, 540), false, Color.WHITE)
	draw_rect(Rect2(0, 0, 960, 540), Color(0.015, 0.03, 0.08, 0.12))
	# Crate objective.
	if quest_stage == 2:
		draw_rect(Rect2(crate_position - Vector2(16, 13), Vector2(32, 26)), Color("795036"))
		draw_rect(Rect2(crate_position - Vector2(12, 10), Vector2(24, 20)), Color("bd8348"), false, 2.0)
		draw_circle(crate_position + Vector2(0, -25), 7, Color("61d7e5"))
	if quest_stage >= 5:
		draw_rect(Rect2(cistern_gate_position - Vector2(20, 45), Vector2(40, 70)), Color("25364d"))
		draw_arc(cistern_gate_position - Vector2(0, 15), 20, PI, TAU, 18, Color("72d7e5"), 3.0)
		draw_string(font, cistern_gate_position + Vector2(-48, 38), "CISTERNA", HORIZONTAL_ALIGNMENT_LEFT, -1, 13, Color("9ee7f1"))
	# NPCs.
	for npc in npcs:
		var visible: bool = npc["role"] != "ariane" or quest_stage >= 3
		if visible:
			var npc_position: Vector2 = npc["position"]
			draw_pixel_person(npc_position, npc["color"], Color("293246"))
			draw_rect(Rect2(npc_position + Vector2(-34, -43), Vector2(68, 17)), Color(0.02, 0.04, 0.09, 0.82))
			draw_string(font, npc_position + Vector2(-29, -30), npc["name"], HORIZONTAL_ALIGNMENT_CENTER, 58, 13, Color.WHITE)
	# Player sprite.
	draw_pixel_person(player, Color("55342f"), Color("bf4d55"))
	draw_hud(font, "KALLÍPOLIS")
	if notice_time > 0.0:
		draw_string(font, Vector2(31, 514), notice, HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("fff0ad"))
	if title_open:
		draw_title(font)
	elif battle_open:
		draw_battle(font)
	elif gallery_open:
		draw_gallery(font)
	elif inventory_open:
		draw_inventory(font)
	elif dialogue_open:
		draw_dialogue(font)
	else:
		draw_controls(font)

func draw_cistern(font: Font) -> void:
	draw_texture_rect(CISTERN_BACKGROUND, Rect2(0, 0, 960, 540), false, Color.WHITE)
	draw_rect(Rect2(0, 0, 960, 540), Color(0.01, 0.04, 0.09, 0.18))
	for i in cistern_shard_positions.size():
		if not cistern_shards[i]:
			var shard: Vector2 = cistern_shard_positions[i]
			draw_circle(shard, 13, Color(0.2, 0.95, 1.0, 0.25))
			draw_circle(shard, 7, Color("9ef9ff"))
			draw_line(shard + Vector2(0, -20), shard + Vector2(0, 20), Color("d9ffff"), 2.0)
	draw_rect(Rect2(cistern_door_position - Vector2(26, 44), Vector2(52, 72)), Color(0.2, 0.12, 0.08, 0.8))
	draw_arc(cistern_door_position - Vector2(0, 20), 26, PI, TAU, 20, Color("d7a75d"), 3.0)
	draw_string(font, cistern_door_position + Vector2(-38, 42), "PORTA", HORIZONTAL_ALIGNMENT_LEFT, -1, 13, Color("ffe0a0"))
	draw_rect(Rect2(cistern_exit_position - Vector2(25, 18), Vector2(50, 36)), Color(0.05, 0.08, 0.13, 0.9))
	draw_string(font, cistern_exit_position + Vector2(-28, 42), "SAÍDA", HORIZONTAL_ALIGNMENT_LEFT, -1, 13, Color("d4dce7"))
	if not cistern_chest_open:
		draw_rect(Rect2(cistern_chest_position - Vector2(17, 12), Vector2(34, 24)), Color("7a4e2e"))
		draw_rect(Rect2(cistern_chest_position - Vector2(17, 12), Vector2(34, 24)), Color("dfb55f"), false, 2.0)
		draw_string(font, cistern_chest_position + Vector2(-28, 36), "BAÚ", HORIZONTAL_ALIGNMENT_LEFT, -1, 13, Color("ffe09b"))
	draw_pixel_person(player, Color("55342f"), Color("bf4d55"))
	draw_hud(font, "CISTERNA ESQUECIDA")
	if notice_time > 0.0:
		draw_string(font, Vector2(31, 514), notice, HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("fff0ad"))
	if battle_open:
		draw_battle(font)
	elif gallery_open:
		draw_gallery(font)
	elif inventory_open:
		draw_inventory(font)
	elif dialogue_open:
		draw_dialogue(font)
	else:
		draw_controls(font)

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
	draw_string(font, Vector2(64, 497), "[E] Começar a jornada", HORIZONTAL_ALIGNMENT_LEFT, -1, 20, Color("ffdf92"))

func draw_gallery(font: Font) -> void:
	var heroine: Dictionary = heroines[gallery_index]
	draw_rect(Rect2(30, 32, 900, 476), Color(0.03, 0.04, 0.08, 0.98))
	draw_rect(Rect2(30, 32, 900, 476), heroine["color"], false, 3.0)
	draw_string(font, Vector2(62, 74), "VÍNCULOS DE ATLÂNTIDA", HORIZONTAL_ALIGNMENT_LEFT, -1, 24, Color("f5e7c9"))
	draw_string(font, Vector2(63, 108), "Retratos, histórias e expressões serão liberados conforme a jornada avança.", HORIZONTAL_ALIGNMENT_LEFT, -1, 15, Color("cdd4e1"))
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
	draw_rect(Rect2(28, 348, 904, 164), Color(0.02, 0.03, 0.07, 0.97))
	draw_rect(Rect2(28, 348, 904, 164), Color("d5b46d"), false, 2.0)
	draw_string(font, Vector2(58, 381), dialogue_speaker.to_upper(), HORIZONTAL_ALIGNMENT_LEFT, 580, 18, Color("f2cd7e"))
	for i in dialogue_lines.size():
		draw_string(font, Vector2(58, 411 + i * 23), dialogue_lines[i], HORIZONTAL_ALIGNMENT_LEFT, 625, 16, Color("f8f2e7"))
	if dialogue_speaker == "Ariane":
		var ariane_expression: Texture2D = ARIANE_EMBARRASSED_PORTRAIT if dialogue_expression == "embarrassed" else ARIANE_PORTRAIT
		draw_texture_rect(ariane_expression, Rect2(748, 92, 150, 240), false, Color.WHITE)
	if dialogue_choices.is_empty():
		draw_string(font, Vector2(800, 490), "[E] continuar", HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color("d5b46d"))
	else:
		var start_y := 435
		for i in dialogue_choices.size():
			var color := Color("ffdf92") if i == choice_index else Color("e5e8f1")
			var marker := "▶ " if i == choice_index else "  "
			draw_string(font, Vector2(58, start_y + i * 21), marker + dialogue_choices[i], HORIZONTAL_ALIGNMENT_LEFT, 610, 14, color)

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
