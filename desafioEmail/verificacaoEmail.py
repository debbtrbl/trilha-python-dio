# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:
if "@" not in email:
    print("E-mail inválido")
elif email.count("@") > 1:
    print("E-mail inválido")
elif ".com" not in email.split("@")[1]:
    print("E-mail inválido") 
elif email[0] == "@" or email[-1] == "@":
    print("E-mail inválido")
elif email != email.strip():
    print("E-mail inválido")
else:
    print("E-mail válido")