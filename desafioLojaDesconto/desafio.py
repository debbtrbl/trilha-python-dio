# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

novo_preco = 0
if cupom == "DESCONTO10":
  novo_preco = preco - (preco * descontos.get("DESCONTO10"))
elif cupom == "DESCONTO20":
  novo_preco = preco - (preco * descontos.get("DESCONTO20"))
elif cupom == "SEM_DESCONTO":
  novo_preco = preco - (preco * descontos.get("SEM_DESCONTO"))
  
print(f"{novo_preco:.2f}")