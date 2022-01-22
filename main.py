def run():
    num = int(input('Enter number: '))
    numeros = []
    i=1
    while i <= num:
        numeros.append(i)
        i+=1
    cadena = "".join([str(_) for _ in numeros])
    print(cadena)
    print(len(cadena))


if __name__ == "__main__":
    run()
