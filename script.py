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
number = seed_number
already_seen = set()
counter = 0

while number not in already_seen :
    counter += 1
    already_seen.add(number)
    number = aleatorio(number)
# zfill adds padding of zeroes
    print ( f"#{ counter }: { number }")

print( f"We began with { seed_number } , and"f" have repeated ourselves after { counter } steps "f" with { number }.")

