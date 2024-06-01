from random import *


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''


print('Добро пожаловать в генератор паролей, пожалуйста введите допускаемые ответы: [да, lf, yes, ДА, Да]')
kol = int(input('Количество паролей для генерации: '))
lenght = int(input('Длина одного пароля: '))
chif = input('Включать ли цифры 0123456789? ').strip()
propis = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ').strip()
strok = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ').strip()
sim = input('Включать ли символы !#$%&*+-=?@^_? ').strip()
neod = input('Исключать ли неоднозначные символы il1Lo0O? ').strip()


if chif.lower() == 'да' or 'lf' or 'yes' or 'ДА' or 'Да':
    chars += digits
if propis.lower() == 'да' or 'lf' or 'yes' or 'ДА' or 'Да':
    chars += uppercase_letters
if strok.lower() == 'да' or 'lf' or 'yes' or 'ДА' or 'Да':
    chars += lowercase_letters
if sim.lower() == 'да' or 'lf' or 'yes' or 'ДА' or 'Да':
    chars += punctuation


for i in 'il1Lo0O':
    if neod.lower() == 'да' or 'lf' or 'yes' or 'ДА' or 'Да':
        chars.replace(i, '')

print('*'*100)
def generate_password():
    passw = ''
    count = 1
    for i in range(lenght):
        passw += choice(chars)
    return passw
for g in range(kol):
    print(generate_password())




print(generate_password())
print('*'*100)
