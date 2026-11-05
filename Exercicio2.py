
import multiprocessing
import time
import random



def somatoria(id, valores):
    soma = 0
    for j in range(5):
        soma = soma + valores[j]
        time.sleep(0.2)
    print("Linha", id, "resultado", soma)


def main():
    parametros = []
    for i in range(3):
        identificador = i + 1
        valor1 = random.randint(1, 100)
        valor2 = random.randint(1, 100)
        valor3 = random.randint(1, 100)
        valor4 = random.randint(1, 100)
        valor5 = random.randint(1, 100)
        vet = [valor1, valor2, valor3, valor4, valor5]
        parametros.append((identificador, vet))    
    with multiprocessing.Pool(processes=3) as threads:

        threads.starmap(somatoria, parametros)


if __name__ == '__main__':
    main()
