# считывание строки и разбиение ее по пробелам
def int_validator(x):
    try:
        return int(x)
    except:
        return False


lst_in = input().split()

print(sum(map(int, filter(lambda x: int_validator(x), lst_in))))