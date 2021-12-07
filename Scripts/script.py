import time


def semente_alt():
    seed = int(time.time())

    return seed

def semente():
    seed = int(input("Insira a semente: "))

    return seed

def aleatorio(numero, tam_numero):
    ini = int((tam_numero/2))
    fim = int((tam_numero/2)+tam_numero)
    numero = str(numero * numero ).zfill(2*tam_numero)[ini:fim]

    return int(numero)

#função para mudar a seed
def exc_repetiu(n):
    new_seed = int(semente_alt() * n)

    return new_seed

def aleatfloat(x):
    e = x / (pow(10, len(str(x))))
  
    return e

def aleatint(sup,inf, number):

    if number < 10:
        number += 1
        number = number * 100
    x = int(str(number)[1]) + int(str(number)[0])

    while x > sup or x < inf:
        if x > sup:
            x = x-1
        else:
            x = x+1
    return x


class Repetiu_Error(Exception):
    pass
  
seed_number = semente()
seed_list = []
seed_list.append(seed_number)
tam_numero = len(str(seed_number))
number = seed_number
repetidos = []
num_ran = []
counter = 0
nota = []
nota_aux = 0
aux = 0
prontuarios = ["SL3003175","SL3003663","SL3002705","SL3001814","SL3004783","SL3002462",
"SL3001865","SL3002781","SL300385X","SL3002501","SL3001466","SL3003698","SL3008568","SL3002802",
"SL3004686","SL3008142","SL3001881","SL300189X","SL3001903","SL3002519","SL3001806","SL3002497",
"SL3002691","SL3001482","SL3001831","SL300323X","SL3003213"]

while counter < 27:
    number = aleatorio(number, tam_numero)
    nota_aux = aleatint(10, 0, number) * aleatfloat(number)

    #tratamento se a nota estiver abaixo de 8
    while counter == 22 and nota_aux < 8:
        print('?')
        number = exc_repetiu(aux)
        nota_aux = aleatint(10, 0, number) * aleatfloat(number)
        aux += 1
    nota.append(nota_aux)
    try:
        if (number in repetidos) or (counter == 22 and nota[counter] < 8):
            raise Repetiu_Error
        else:
            pass
    except Repetiu_Error:
        #print("!")
        number = exc_repetiu(counter)
        seed_list.append(number)
        nota_aux = aleatint(10, 0, number) * aleatfloat(number)

        #tratamento se a nota estiver abaixo de 8
        while counter == 22 and nota_aux < 8:
            #print('?')
            number = exc_repetiu(aux)
            nota_aux = aleatint(10, 0, number) * aleatfloat(number)
            aux += 1
        nota.insert(counter, nota_aux)
        
    repetidos.append(number)
    num_ran.append(number)
    counter += 1

i =0

#escrevento no arquivo
with open("notassecretas.txt", "w") as f:
    f.write(f"{seed_list}\n")
    for pront in prontuarios:
        f.write(f"{pront} {int(nota[i])}\n")
        i+=1


