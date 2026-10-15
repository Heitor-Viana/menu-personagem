jogador = []
inventario = []
dano = 0
vida = 100
moedas = 0

while True: 
  print("===== MENU DE PERSONAGEM =====")
  print("|1- Código.                  |")
  print("|2- Nome.                    |")
  print("|3- Vida.                    |")
  print("|4- Ataque.                  |")
  print("|5- Moedas.                  |")
  print("|6- Inventário.              |")
  print("|7- Loja.                    |")
  print("|8- Sair.                    |")
  print("==============================")
  opção = int(input("Escolha uma opção: "))

  if opção == 1: 
    print("===== CÓDIGO =====")
    codigo = int(input("Qual o código do seu personagem: "))
    jogador.append(codigo)

  if opção == 2: 
    print("===== NOME =====")
    nome = input("Qual o nome do seu personagem: ")
    jogador.append(nome)

  if opção == 3: 
    print("===== VIDA =====")
    if vida >100: 
      vida = 100
    else:
      print(f"A vida do seu personagem é igual à {vida}.")

  if opção == 4: 
    print("===== DANO =====")
    dano = int(input("Seu personagem vai receber um ataque, qual o dano que ele recebeu: "))
    vida = vida - dano

  if opção == 5: 
    print("===== MOEDAS =====")
    if moedas > 0: 
      print(f"Você tem {moedas} moedas.")
    else: 
      moedas = int(input("Quantas moedas você tem: "))

  if opção == 6: 
    print(f"Esse é seu inventário: {inventario}\n")
    
  if opção == 7: 
    print("===== LOJA DE ITENS =====")
    print("1- Poção pequena | Cura 10 | R$ 5.00")
    print("2- Poção média | Cura 30 | R$ 15.00")
    print("3- Poção grande | Cura 50 | R$ 25.00")
    compra = int(input("Qual poção você deseja comprar: "))

    if compra == 1: 
      print("Você comprou uma poção pequena.")
      moedas = moedas - 5
      inventario.append(moedas)
      tomar_poção = input("Você deseja tomar a poção pequena? (s/n): ").strip().lower()
      if tomar_poção == "s": 
        if vida <100: 
          print("Você tomou uma poção pequena curou 5 de vida.")
          vida = vida + 5
        else:
          print("Sua vida está cheia.")
          print("Sua poção foi adicionada ao inventário.")
          poçãoP = "poçãoP"
          inventario.append(poçãoP)
      else:
        print("Sua poção foi adicionada no inventário.")
        poçãoP = "poçãoP"
        inventario.append(poçãoP)

      if compra == 2: 
        print("Você comprou uma poção média.")
        moedas = moedas - 15
        inventario.append(moedas)
        tomar_poção = input("Você deseja tomar a poção média? (s/n): ").strip().lower()
        if tomar_poção == "s": 
          if vida <100: 
            print("Você tomou uma poção média curou 30 de vida.")
            vida = vida + 30
          else:
            print("Sua vida está cheia.")
            print("Sua poção foi adicionada ao inventário.")
            poçãoM = "poçãoM"
            inventario.append(poçãoM)
        else:
          print("Sua poção foi adicionada no inventário.")
          poçãoM = "poçãoM"
          inventario.append(poçãoM)

      elif compra == 3: 
        print("Você comprou uma poção grande.")
        moedas = moedas - 25
        inventario.append(moedas)
        tomar_poção = input("Você deseja tomar a poção grande? (s/n): ").strip().lower()
        if tomar_poção == "s": 
          if vida <100: 
            print("Você tomou uma poção grande curou 50 de vida.")
            vida = vida + 50
          else:
            print("Sua vida está cheia.")
            print("Sua poção foi adicionada ao inventário.")
            poçãoG = "poçãoG"
            inventario.append(poçãoG)
        else:
          print("Sua poção foi adicionada no inventário.")
          poçãoG = "poçãoG"
          inventario.append(poçãoG)

    if opção == 8: 
      print("Saindo...")
      break