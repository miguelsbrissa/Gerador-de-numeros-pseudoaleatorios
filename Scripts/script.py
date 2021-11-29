import time
import math
import random

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
    new_seed = int(semente_alt() * n)

    return new_seed

def aleatfloat():
    #x = semente_alt()
    #e = 0.1 * (pow(10, len(str(x))))
    #x = e/x
    x = random.random()

    return x

def aleatint(sup,inf):
    number = 0
    
    while number < 8 or number < inf or number > sup: 
        dec = aleatfloat()
        number = aleatorio(sup, len(str(sup)))
        number = int(number * dec)

    return number


class Repetiu_Error(Exception):
    pass

#semente inicial 119736    
seed_number = semente()

seed_list = []
seed_list.append(seed_number)
qtd_n = int(input("Digite a quantidade de numeros desejados: "))
tam_numero = len(str(seed_number))
number = seed_number
repetidos = []
num_ran = []
counter = 0
while counter < qtd_n:
    counter += 1
    number = aleatorio(number, tam_numero)
    try:
        if number in repetidos:
            raise Repetiu_Error
        else:
            pass
    except Repetiu_Error:
        number = exc_repetiu(counter)
        seed_list.append(number)
        number =  aleatorio(number, len(str(int(number))))
        
    repetidos.append(number)
    num_ran.append(number)
    print(f'Numero add {number}')
    print(f"Nota gerada: {aleatint(50,10)}")

print(f" Lista de numeros gerados: {num_ran}")
print(f"Lista de seeds: {seed_list}")
