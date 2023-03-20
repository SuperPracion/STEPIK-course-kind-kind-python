# считывание строки и разбиение ее по пробелам
def value_validator(value):
    try:
        return int(value)
    except:
        try:
            return float(value)
        except:
            return str(value)


lst_in = input().split()
print([value_validator(value) for value in lst_in])
