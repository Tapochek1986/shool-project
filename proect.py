
from random import choice
import json
from shifr import encrypt, decrypt
from openpyxl import load_workbook
from cryptography.fernet import Fernet
from parse_excel import file_doc

doc="questions_from_excel.json"
with open('key.key', 'rb') as f:
    key= f.read()

data=decrypt(doc, key).decode('UTF-8')
data=json.loads(data)

def menu():
    print('1. Открыть файл')

vopros=[]

while True:
    menu()    
    vvod = int(input('Введите цифру: '))
    if vvod == 1:
        rand = choice(data)
        print(rand["Текст вопроса"])
        if rand['Тип вопроса'] != 'открытый':
            for i,el in enumerate(rand['Варианты ответа']):
                print(f'{i+1}.',el)
 
        

    elif vvod == 2:
        pass




        