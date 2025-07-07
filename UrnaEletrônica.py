def verificandoasenha(senha):
  tentativas = 0
  while tentativas < 4:
      if senha == 1234:
          return True
      else:
          tentativas += 1
          if tentativas < 4:
              senha = int(input("Senha incorreta. Tente novamente: "))
          else:
              return False

def confirmacaovoto(confirmacao):
  return confirmacao == 1

def voto_candidatos(voto):
  if voto == 14:
      print("#######################")
      print("CANDIDATO: JOAO BATISTA\nPARTIDO: AO MEIO")
      print("#######################")
  elif voto == 15:
      print("#######################")
      print("CANDIDATO: LUIZ RODRIGUES\nPARTIDO: PV")
      print("#######################")
  elif voto == 16:
      print("#######################")
      print("CANDIDATO: MEREDITH GREY\nPARTIDO: GERAL")
      print("#######################")
  else:
      print("#######################")
      print("VOTO EM BRANCO OU NULO")
      print("#######################")

def calculandooresultado(v1, v2, v3, brancos_nulos):
  total = v1 + v2 + v3 + brancos_nulos
  if total == 0:
      print("Nenhum voto registrado.")
      return

  if brancos_nulos > total / 2:
      print("ELEIÇÃO ANULADA - BRANCOS/NULOS SÃO MAIORIA")
      return

  print("\n===== RESULTADO FINAL =====")
  print(f"JOAO BATISTA: {(v1 * 100) / total:.2f}% ({v1} votos)")
  print(f"LUIZ RODRIGUES: {(v2 * 100) / total:.2f}% ({v2} votos)")
  print(f"MEREDITH GREY: {(v3 * 100) / total:.2f}% ({v3} votos)")
  print(f"BRANCOS/NULOS: {(brancos_nulos * 100) / total:.2f}% ({brancos_nulos} votos)")
  print(f"TOTAL DE VOTOS: {total}")

  if v1 > v2 and v1 > v3:
      print("VENCEDOR: JOAO BATISTA")
  elif v2 > v1 and v2 > v3:
      print("VENCEDOR: LUIZ RODRIGUES")
  elif v3 > v1 and v3 > v2:
      print("VENCEDOR: MEREDITH GREY")
  else:
      print("EMPATE")

voto_candidato1 = 0
voto_candidato2 = 0
voto_candidato3 = 0
voto_brancos_nulos = 0

print("SEJA BEM VINDO AO SISTEMA DE VOTAÇÃO")
senha = int(input("DIGITE A SENHA PARA ATIVAR: "))

if not verificandoasenha(senha):
  print("URNA DESLIGADA")
else:
  print("INICIANDO VOTAÇÃO\n")

  while True:
      voto = int(input("DIGITE O NÚMERO DO CANDIDATO: "))

      if voto == 1234:
          print("VOTAÇÃO ENCERRADA")
          calculandooresultado(voto_candidato1, voto_candidato2, voto_candidato3, voto_brancos_nulos)
          break

      voto_candidatos(voto)
      try:
          confirmacao = int(input("CONFIRME SEU VOTO (1 para confirmar): "))
      except ValueError:
          confirmacao = 0

      if confirmacaovoto(confirmacao):
          print("***************")
          print("VOTO CONFIRMADO")
          print("***************")
          if voto == 14:
              voto_candidato1 += 1
          elif voto == 15:
              voto_candidato2 += 1
          elif voto == 16:
              voto_candidato3 += 1
          else:
              voto_brancos_nulos += 1
      else:
          print("VOTO ANULADO/BRANCO")
          voto_brancos_nulos += 1