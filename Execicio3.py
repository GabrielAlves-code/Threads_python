
import threading
import random
import time



def corrida(id, distancia_maxima):

    salto_maximo = random.randint(1, 5)
    distancia_percorrida = 0


    print("Sapo", id, "começou a corrida!")
    print("Sapo", id, "pode saltar até", salto_maximo, "cm por salto")

    
    while distancia_percorrida < distancia_maxima:
   
        salto = random.randint(0, salto_maximo)   
        distancia_percorrida = distancia_percorrida + salto
        print("Sapo", id, "saltou", salto, "cm")
        print("Sapo", id, "percorreu", distancia_percorrida, "cm")

        time.sleep(0.2)

   
    print("Sapo", id, "CHEGOU AO FIM")


def main():

   
    distancia_maxima = 30
    threads = []
    for i in range(5):
        thread = threading.Thread(target=corrida,   args=(i + 1, distancia_maxima))
        threads.append(thread)
        thread.start()

   
    for thread in threads:
        thread.join()

    print("TODOS OS SAPOS CHEGARAM AO FIM DO PERCURSO")


if __name__ == '__main__':
    main()
