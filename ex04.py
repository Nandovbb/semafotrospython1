
import multiprocessing
import time
import random

sem_pista = None
sem_equipes = None


def init(pista, equipes):
    global sem_pista
    global sem_equipes

    sem_pista = pista
    sem_equipes = equipes


def carro(id):
    global sem_pista
    global sem_equipes

    equipe = id // 2

    print("\nCarro", id + 1, "da equipe", equipe + 1,
          "aguardando para entrar na pista")

    with sem_equipes[equipe]:

        with sem_pista:
            print("\nCarro", id + 1, "da equipe", equipe + 1,
                  "ENTROU NA PISTA")

            for volta in range(1, 4):
                tempo_volta = random.uniform(80, 120)

                time.sleep(tempo_volta / 20)

                print("\nCarro", id + 1,
                      "| Equipe:", equipe + 1,
                      "| Volta:", volta,
                      "| Tempo:", round(tempo_volta, 2), "segundos")

            print("\nCarro", id + 1, "da equipe", equipe + 1,
                  "TERMINOU O TREINO")

        print("\nCarro", id + 1, "saiu da pista")


def main():
    params = list(range(14))

    with multiprocessing.Manager() as manager:

        pista = manager.Semaphore(5)

        equipes = [
            manager.Semaphore(1)
            for i in range(7)
        ]

        with multiprocessing.Pool(
            processes=14,
            initializer=init,
            initargs=(pista, equipes)
        ) as pool:

            pool.map(carro, params)


if __name__ == '__main__':
    main()
