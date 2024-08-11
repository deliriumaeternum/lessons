calls = 0
def count_calls():
    global calls
    calls += 1

word = input('Введите слово: ')
def string_info():
    a = int(len(word))
    b = word.upper()
    c = word.lower()
    info = (a, b, c)
    count_calls()
    return info
info = string_info()
print(info)

word1 = input('Введите слово: ')
list = input('Введите список: ')
def is_contains():
    string = word1.lower()
    list_to_search = list
    for i in range(len(list_to_search)):
        if word1.lower() in list:
            result = True
            break
        else:
            result = False
            continue
    count_calls()
    return result
result = is_contains()
print(result)
print(calls)