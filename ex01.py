import multiprocessing
import time

sentido = None
sem = None


def init(memoria, semaforo):
    global sentido
    global sem
    sentido = memoria
    sem = semaforo


def op(direcao):
    global sentido
    global sem

    # Bloqueia o cruzamento
    with sem:
        sentido[0] = direcao

        # Carro passa pelo cruzamento
        print("Passando no sentido:", sentido[0])
        time.sleep(0.5)

        print("\nCruzamento liberado.")
        time.sleep(0.5)
        print("Cruzamento fechado.\n")


def main():
    # Direções dos 4 carros
    setas = [
        "Cima",
        "Baixo",
        "Esquerda",
        "Direita"
    ]

    with multiprocessing.Manager() as manager:
        memoria = manager.list([""])
        semaforo = manager.Semaphore(1)

        # Inicia o Pool de processos
        with multiprocessing.Pool(processes=4, initializer=init, initargs=(memoria, semaforo)) as pool:
            pool.map(op, setas)


if __name__ == '__main__':
    main()
