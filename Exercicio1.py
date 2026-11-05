import multiprocessing
import time

def paralelo(id):
    print("Thread #", id, 'começou')
    time.sleep(0.5)
    print("Thread #", id, 'terminou')

def main():
    identificador: int = 0 
    j: int = 0
    parametros: int = [0]*6 
    for j in range (0, 6, 1):
        identificador = j
        parametros[j] = identificador

    with multiprocessing.Pool(processes=5) as threads:
        threads.map(paralelo, parametros)


if (__name__=='__main__'):
        main()
