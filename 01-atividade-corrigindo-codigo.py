# Variáveis para armazenar os números:
import os 
os.system("cls||clear")

QTD = 5
lista_num=[]


for i in range(QTD):
    while True:
        numero1 = int(input(f"Informe o {i+1}º numero: "))
        lista_num.append(numero1)
        break

# Processando cada número
def media (a):
    if a

"""def processando_par_impar(a):
    quantidade_pares = 0
    soma_pares = 0
    quantidade_impares = 0
    soma_impares = 0
    for numero in a:
        if numero %2==0:
            quantidade_pares +=1

        else:
            quantidade_impares +=1

    return quantidade_pares, media_pares, quantidade_impares, media_impares


def processando_posi_nega (a):
    quantidade_negativo=0
    quantidade_positivo=0
    for numero in a:
        if numero >=0:
            quantidade_positivo+=1
        else:
            quantidade_negativo+=1
    return quantidade_negativo, quantidade_positivo

qtd_par, qtd_imp= processando_par_impar(lista_num)
negativo, positivo = processando_posi_nega(lista_num)







print(f"Quantidade de pares: {qtd_par}")
print(f"Media dos pares: {md_par}")
print(f"Quantidade dos impares: {qtd_imp}")
print(f"Media dos impares: {md_imp}")
print(f"Quantidade de numero negativo: {negativo}")
print(f"Quantidade de numero positivo: {positivo}")"""

