import Form



soma_olhos_mae = Form.Zigoto_Olho_Mae[0] + Form.Zigoto_Olho_Mae[1]
soma_olhos_pai = Form.Zigoto_Olho_Pai[0] + Form.Zigoto_Olho_Pai[1]


if soma_olhos_mae == 16 and soma_olhos_pai == 16:
    Quo_olhos = 1
elif soma_olhos_mae == 8 and soma_olhos_pai == 8:
    Quo_olhos = 1
elif  soma_olhos_mae == 4 and soma_olhos_pai == 4:
    Quo_olhos = 1
elif soma_olhos_mae == 2 and soma_olhos_pai == 2:
    Quo_olhos = 1
    



elif soma_olhos_mae == 12 and soma_olhos_pai == 12:
    Quo_olhos = 2
elif soma_olhos_mae == 12 and (soma_olhos_pai == 8 or soma_olhos_pai == 16): 
    Quo_olhos = 2
elif soma_olhos_pai == 12 and (soma_olhos_mae == 8 or soma_olhos_mae == 16):
    Quo_olhos = 2
elif (soma_olhos_pai == 8 and soma_olhos_mae == 16) or (soma_olhos_mae == 8 and soma_olhos_pai == 16):
    Quo_olhos = 2
else:
    Quo_olhos = "erro"

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")


print(Quo_olhos)

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")







