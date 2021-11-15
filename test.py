import time

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

seed_number = semente()
qtd_n = int(input("Digite a quantidade de numeros desejados: "))
tam_numero = len(str(seed_number))
number = seed_number
already_seen = set()
num_ran = []
counter = 0

while counter < qtd_n:
    if number in already_seen:
        print(f"{number} repetiu")
    #print(f'Em int {number}')
    counter += 1
    #print(counter)
    already_seen.add(number)
    number = aleatorio(number, tam_numero)
    num_ran.append(number)
    
    

print(f" Lista de numeros gerados: {num_ran}")
