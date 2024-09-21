my_dict = {'Василий': 1991, 'Мария': 2004, 'Анна': 1989}
print('Словарь:',(my_dict))
print('Существующий ключ:', my_dict['Мария'])
print('Несуществующий ключ:', my_dict.get('Олег'))
my_dict.update({'Павел': 1990,
                'Валерия': 2007})
a = my_dict.pop('Валерия')
print('Удаленный ключ:', (a))
print ('Обновленный словарь:', (my_dict))

my_set = {1, 2, 3, "water", 1, True, False, True, "smile", 3, "water"}
print("Множество:",(my_set))
my_set.update(['eagle', 8])
my_set.remove('smile')
print("Обновленное множество:",(my_set))