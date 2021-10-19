import time

def sem_time():
    seed = int(time.time())
    print(f"Semente: {seed}")

    return seed

def semente():
    seed = int(input("Insira a semente: "))

    return seed

def aleatorio(numero):
    tam_numero = len(str(numero))
    ini = int((tam_numero/2))
    fim = int((tam_numero/2)+tam_numero)
    numero = int(str( numero * numero ).zfill(2*tam_numero)[ini:fim])

    return numero

seed_number = semente()
qtd_n = int(input("Digite a quantidade de numeros desejados: "))
number = seed_number
already_seen = set()
num_ran = []
counter = 0

while counter < qtd_n:
    counter += 1
    already_seen.add(number)
    number = aleatorio(number)
    num_ran.append(number)
    
    if number in already_seen:
        print(f"{number} repetiu")

print(f" Lista de numeros gerados: {num_ran}")

