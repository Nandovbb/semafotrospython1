import multiprocessing
import time
import random


def sapo0(colocacao, lock):
    distancia = 0
    while distancia < 50:
        salto = random.randint(1, 5)
        distancia += salto
        print("\nSapo 0 saltou", salto, "cm - Total:", distancia, "cm")
        time.sleep(random.uniform(0.1, 0.3))

    with lock:
        print("\nSapo 0 chegou em", colocacao.value, "lugar")
        colocacao.value += 1


def sapo1(colocacao, lock):
    distancia = 0
    while distancia < 50:
        salto = random.randint(1, 5)
        distancia += salto
        print("\nSapo 1 saltou", salto, "cm - Total:", distancia, "cm")
        time.sleep(random.uniform(0.1, 0.3))

    with lock:
        print("\nSapo 1 chegou em", colocacao.value, "lugar")
        colocacao.value += 1


def sapo2(colocacao, lock):
    distancia = 0
    while distancia < 50:
        salto = random.randint(1, 5)
        distancia += salto
        print("\nSapo 2 saltou", salto, "cm - Total:", distancia, "cm")
        time.sleep(random.uniform(0.1, 0.3))

    with lock:
        print("\nSapo 2 chegou em", colocacao.value, "lugar")
        colocacao.value += 1


def sapo3(colocacao, lock):
    distancia = 0
    while distancia < 50:
        salto = random.randint(1, 5)
        distancia += salto
        print("\nSapo 3 saltou", salto, "cm - Total:", distancia, "cm")
        time.sleep(random.uniform(0.1, 0.3))

    with lock:
        print("\nSapo 3 chegou em", colocacao.value, "lugar")
        colocacao.value += 1


def sapo4(colocacao, lock):
    distancia = 0
    while distancia < 50:
        salto = random.randint(1, 5)
        distancia += salto
        print("\nSapo 4 saltou", salto, "cm - Total:", distancia, "cm")
        time.sleep(random.uniform(0.1, 0.3))

    with lock:
        print("\nSapo 4 chegou em", colocacao.value, "lugar")
        colocacao.value += 1


def main():
    colocacao = multiprocessing.Value('i', 1)
    lock = multiprocessing.Lock()

    p0 = multiprocessing.Process(target=sapo0, args=(colocacao, lock))
    p1 = multiprocessing.Process(target=sapo1, args=(colocacao, lock))
    p2 = multiprocessing.Process(target=sapo2, args=(colocacao, lock))
    p3 = multiprocessing.Process(target=sapo3, args=(colocacao, lock))
    p4 = multiprocessing.Process(target=sapo4, args=(colocacao, lock))

    p0.start()
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p0.join()
    p1.join()
    p2.join()
    p3.join()
    p4.join()


if __name__ == '__main__':
    main()
