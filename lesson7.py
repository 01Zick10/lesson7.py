# lesson7.py

#3
print(' 1.Просмотр баланса \n 2.Внесение денег \n 3.Обналичивание денег \n 4.Оплата по реквезитам \n 0.Завершить оперпцию' )

balance = 0
account = {'balance': 0}

def replenishment_balance():
    deposit = int(input('Введите сумму: '))
    account['balance'] += deposit
    print(f' Вот это да! Зарплата пришла? Согласись приятно когда карта пополняется после '
          f'сложного рабочего месяца? \n Но ты так не радуйся ведь скоро (блогадоря Шахриёру) твои деньги'
          f' отправятся в небытие. А вот те деньги которые ты заработал -> {int(deposit)}$'
          f'\n P.S \n Тебе вообще повезло,что злобный дядька Джасур не скомуниздил твои деньги себе')


def output_money():
    output = int(input('Введите сумму: '))
    account['balance'] -= output
    print(f'Похоже,что твоя жена пошла по магазинам. Или это наш много уважаемые Шахриёр постарался?'
          f' Ведь только что целых {int(output)}$ отправелись в небытие')


def transfer_money():
    credit_card = int(input('Введите реквезиты карты: '))
    transfer_amount = int(input('Введите сумму для перевода: '))
    account['balance'] -= transfer_amount
    print(f'Вы перевели {int(transfer_amount)}$ по этим реквезитам -> {int(credit_card)} '
          f'\n P.S \n Хорошо,что вы додумались приобрести новую кредитную карту, но от Джасура вы её не скроете')




while 1:
    a = int(input(': '))

    if a == 1:
        print(account)
    elif a == 2:
         print(replenishment_balance())
    elif a == 3:
         output_money()
    elif a == 4:
        transfer_money()
    elif a == 0:
        print('Спасибо вам большое, что выбрали банкомат "Mate" академии.С вам Джасуру всегда есть, что по есть')
        break
        
        
     
    
    
    
    
  #2
  class Employee(): 
    def __init__(self, name, position, age, salary): 
        self.name = name 
        self.position = position 
        self.age = age 
        self.salary = salary 
    def information(self): 
        print("dimoooooooon","Employee", 20, 5500) 
    def increace(self): 
        print(self.salary) 
        self.salary = self.salary + self.salary * 0.1 
        print(self.salary) 
class Manager(Employee): 
    def increace(self): 
        print(self.salary) 
        self.salary = self.salary * 1.2 
        print(self.salary) 
 
 
dimoooooooon = Employee("dude", "Employee", 25, 5500) 
dude = Manager('dude', Manager, 28, 10000) 
dimoooooooon.information() 
dimoooooooon.increace()







1#
class Circle: 
    def __init__(self): 
        self.p = ' ' 
        self.s = '' 
 
perimeter = Circle() 
perimeter.p = 2 * 8 * 3.14 
print(perimeter.p) 
 
S = Circle 
S.s = 3.14 * 8 ** 2 
print(S.s)
