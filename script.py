import time
import math

def semente_alt():
    seed = int(time.time())
    print(f"Semente: {seed}")

    return seed

def semente():
    seed = int(input("Insira a semente: "))

    return seed

def aleatorio(numero, tam_numero):
    ini = int((tam_numero/2))
    fim = int((tam_numero/2)+tam_numero)
    numero = str(numero * numero ).zfill(2*tam_numero)[ini:fim]
    #print(f'Em string {numero}')

    return int(numero)

def exc_repetiu(n):
    new_seed = semente_alt()/math.exp(n) + math.factorial(n)

    return new_seed

seed_number = semente()
seed_list = []
seed_list.append(seed_number)
qtd_n = int(input("Digite a quantidade de numeros desejados: "))
tam_numero = len(str(seed_number))
number = seed_number
already_seen = set()
num_ran = []
counter = 0

while counter < qtd_n:
    if number in already_seen:
        print("Nao corrigiu")
    print(f'Em int {number}')
    counter += 1
    print(counter)
    
    number = aleatorio(number, tam_numero)
    if number in already_seen:
        print(f"{number} excecao")
        number = exc_repetiu(counter)
        seed_list.append(number)
        number =  aleatorio(number, len(str(int(number))))
    already_seen.add(number)
    num_ran.append(number)
    print(f'Numero add {number}')

print(f" Lista de numeros gerados: {num_ran}")
print(f"Lista de seeds: {seed_list}")

