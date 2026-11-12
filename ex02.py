import multiprocessing
import time
import random

vetor = None
sem = None


def init(vet, s):
    global vetor
    global sem
    vetor = vet
    sem = s


def pessoa(id):
    global vetor
    global sem

    velocidade = random.uniform(4, 6)
    tempo_caminhada = 200 / velocidade
    print("Pessoa", id, "Tempo de caminhada:", tempo_caminhada, "s")
    time.sleep(tempo_caminhada/20)
    print("\nPessoa", id, "chegou na porta")

    with sem:
        print("\nPessoa", id, "passando pela porta")

        tempo_porta = random.uniform(1, 2)
        time.sleep(tempo_porta)

        vetor[id] = 1

        print("\nPessoa", id, "terminou")

        todos_passaram = True
        for i in range(4):
            if vetor[i] == 0:
                todos_passaram = False
                break

        if todos_passaram == True:
            print("\nTodos passaram pela porta")


def main():
    params = [0, 1, 2, 3]
    vet_inicial = [0] * 4

    vet_valores = multiprocessing.Array('i', vet_inicial)

    with multiprocessing.Manager() as manager:
        semaforo = manager.Semaphore(1)

        with multiprocessing.Pool(processes=4, initializer=init, initargs=(vet_valores, semaforo)) as pool:
            pool.map(pessoa, params)


if __name__ == '__main__':
    main()
