# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for i in range(n):
  participante = input().strip().split(", ")
  nome = participante[0]
  tema = participante[1]

  if tema in eventos:
    eventos[tema].append(nome)
  else:
    eventos[tema] = []
    eventos[tema].append(nome)


# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")