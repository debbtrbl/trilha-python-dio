# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append({"nome": nome, "idade": idade, "status": status})

# Função de prioridade + idade decrescente
def prioridade(p):
    if p["status"] == "urgente":
        return (0, -p["idade"])
    elif p["idade"] >= 60:
        return (1, -p["idade"])
    else:
        return (2, -p["idade"])

# Ordenar pacientes
pacientes = sorted(pacientes, key=prioridade)

# Exibir nomes
nomes = [p["nome"] for p in pacientes]
print("Ordem de Atendimento:", ", ".join(nomes))
