# EXERCÍCIO 11 #
import random

# ------------------------ UTILITÁRIOS ------------------------

def gerar_status():
    hp = random.randint(200, 1000)
    ataque = random.randint(1, 50)
    defesa = random.randint(1, 50)
    return hp, ataque, defesa

def calcular_dano(ataque, defesa):
    return max(0, ataque - defesa)

def chance_critico(dano):
    if random.random() < 0.1:
        print("💥 Crítico!")
        return dano * 2
    return dano

def mostrar_status(p1, p2):
    print("\n--- STATUS ---")
    print(f"{p1['nome']} - HP: {p1['hp']} | ATK: {p1['ataque']} | DEF: {p1['defesa']}")
    print(f"{p2['nome']} - HP: {p2['hp']} | ATK: {p2['ataque']} | DEF: {p2['defesa']}")
    print("--------------")

# ------------------------ EFEITOS DE STATUS ------------------------

def aplicar_efeitos(jogador):
    if jogador['status'].get('buffer_overflow', 0) > 0:
        dano = int(jogador['hp_max'] * 0.05)
        jogador['hp'] -= dano
        print(f"{jogador['nome']} sofre {dano} de dano por Buffer Overflow!")
        jogador['status']['buffer_overflow'] -= 1

    if jogador['status'].get('loop_infinito', 0) > 0:
        print(f"{jogador['nome']} está em Loop Infinito e perde o turno!")
        jogador['status']['loop_infinito'] -= 1
        return False  # Perde o turno

    if jogador['status'].get('tela_azul', 0) > 0:
        jogador['defesa'] = 0
        jogador['status']['tela_azul'] -= 1
        print(f"{jogador['nome']} está com defesa zerada por Tela Azul!")
    else:
        jogador['defesa'] = jogador['defesa_base']

    return True

# ------------------------ ITENS ------------------------

def usar_item(jogador):
    print("\nEscolha um item:")
    print("1 - Poção de Força (ATK +20 por 2 turnos)")
    print("2 - Poção de Defesa (DEF +20 por 2 turnos)")
    print("3 - Poção de Cura Total")
    print("4 - Poção Misteriosa (efeito aleatório)")

    escolha = input(">> ")

    if escolha == "1":
        jogador['ataque'] += 20
        jogador['status']['forca'] = 2
        print("Você usou Poção de Força!")
    elif escolha == "2":
        jogador['defesa'] += 20
        jogador['status']['defesa'] = 2
        print("Você usou Poção de Defesa!")
    elif escolha == "3":
        jogador['hp'] = jogador['hp_max']
        print("HP totalmente restaurado!")
    elif escolha == "4":
        efeito = random.choice(["cura", "forca", "defesa", "dano"])
        if efeito == "cura":
            jogador['hp'] += 100
            print("Poção misteriosa curou 100 de HP!")
        elif efeito == "forca":
            jogador['ataque'] += 15
            jogador['status']['forca'] = 2
            print("Poção misteriosa aumentou o ataque!")
        elif efeito == "defesa":
            jogador['defesa'] += 15
            jogador['status']['defesa'] = 2
            print("Poção misteriosa aumentou a defesa!")
        elif efeito == "dano":
            jogador['hp'] -= 50
            print("Poção misteriosa causou 50 de dano!")
    else:
        print("Item inválido.")

# ------------------------ STATUS ÚNICO ------------------------

def usar_status_especial(jogador, alvo):
    if jogador['status_usado']:
        print("Você já usou seu efeito especial!")
        return

    print("\nEfeitos de Status:")
    print("1 - Buffer Overflow (inimigo sofre dano por 3 turnos)")
    print("2 - Loop Infinito (inimigo perde 1 turno)")
    print("3 - Tela Azul (inimigo sem defesa por 2 turnos)")
    print("4 - Cache Hit (cura 30% do HP se abaixo de 25%)")

    escolha = input("Escolha seu efeito: ")
    if escolha == "1":
        alvo['status']['buffer_overflow'] = 3
    elif escolha == "2":
        alvo['status']['loop_infinito'] = 1
    elif escolha == "3":
        alvo['status']['tela_azul'] = 2
    elif escolha == "4":
        if jogador['hp'] < jogador['hp_max'] * 0.25:
            jogador['hp'] += int(jogador['hp_max'] * 0.3)
            print("Cache Hit ativado! HP restaurado.")
        else:
            print("HP muito alto para usar Cache Hit.")
            return
    else:
        print("Efeito inválido.")
        return

    jogador['status_usado'] = True

# ------------------------ TURNO ------------------------

def turno(jogador, inimigo, is_cpu=False):
    if not aplicar_efeitos(jogador):
        return

    if jogador['status'].get('forca', 0) > 0:
        jogador['status']['forca'] -= 1
        if jogador['status']['forca'] == 0:
            jogador['ataque'] -= 20

    if jogador['status'].get('defesa', 0) > 0:
        jogador['status']['defesa'] -= 1
        if jogador['status']['defesa'] == 0:
            jogador['defesa'] -= 20

    if is_cpu:
        acao = random.choice(["atacar", "curar"])
    else:
        print(f"\nTurno de {jogador['nome']}")
        print("1 - Atacar")
        print("2 - Curar")
        print("3 - Usar Item")
        print("4 - Efeito Especial")
        acao = input(">> ")

    if acao == "1" or (is_cpu and acao == "atacar"):
        dano = calcular_dano(jogador['ataque'], inimigo['defesa'])
        dano = chance_critico(dano)
        inimigo['hp'] -= dano
        print(f"{jogador['nome']} causou {dano} de dano!")
    elif acao == "2" or (is_cpu and acao == "curar"):
        cura = random.randint(10, 50)
        jogador['hp'] += cura
        print(f"{jogador['nome']} curou {cura} de HP!")
    elif acao == "3":
        usar_item(jogador)
    elif acao == "4":
        usar_status_especial(jogador, inimigo)
    else:
        print("Ação inválida!")

# ------------------------ JOGO ------------------------

def jogar(multiplayer=False):
    hp, atk, dfs = gerar_status()
    jogador1 = {
        "nome": "Jogador 1",
        "hp": hp, "hp_max": hp,
        "ataque": atk, "defesa": dfs,
        "defesa_base": dfs,
        "status": {}, "status_usado": False
    }

    if multiplayer:
        hp2, atk2, dfs2 = gerar_status()
        jogador2 = {
            "nome": "Jogador 2",
            "hp": hp2, "hp_max": hp2,
            "ataque": atk2, "defesa": dfs2,
            "defesa_base": dfs2,
            "status": {}, "status_usado": False
        }
    else:
        atk2, dfs2 = random.randint(1, 50), random.randint(1, 50)
        jogador2 = {
            "nome": "CPU",
            "hp": hp, "hp_max": hp,
            "ataque": atk2, "defesa": dfs2,
            "defesa_base": dfs2,
            "status": {}, "status_usado": False
        }

    print(f"\n🎮 Combate Iniciado!")
    mostrar_status(jogador1, jogador2)

    while jogador1['hp'] > 0 and jogador2['hp'] > 0:
        mostrar_status(jogador1, jogador2)
        turno(jogador1, jogador2)
        if jogador2['hp'] <= 0:
            print(f"\n{jogador2['nome']} foi derrotado! {jogador1['nome']} venceu!")
            break
        turno(jogador2, jogador1, is_cpu=not multiplayer)
        if jogador1['hp'] <= 0:
            print(f"\n{jogador1['nome']} foi derrotado! {jogador2['nome']} venceu!")
            break

# ------------------------ MENU ------------------------

def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Single Player")
        print("2 - Multiplayer")
        print("3 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            jogar(multiplayer=False)
        elif opcao == "2":
            jogar(multiplayer=True)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()
