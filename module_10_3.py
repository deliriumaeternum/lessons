import threading
from time import sleep
from random import randint
from threading import Thread, Lock

class Bank(Thread):

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        transaction_count = 100
        for i in range(transaction_count):
            rand_num = randint(50, 500)
            self.balance += rand_num
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {rand_num}. Баланс: {self.balance}')
            sleep(0.001)


    def take(self):
        transaction_count = 100
        for i in range(transaction_count):
            rand_num = randint(50, 500)
            print(f'Запрос на {rand_num}')
            if rand_num <= self.balance:
                self.balance -= rand_num
                print(f'Снятие: {rand_num}. Баланс: {self.balance}')
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')