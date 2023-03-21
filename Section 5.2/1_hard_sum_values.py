a, b = input().split()
try:
    res = int(a) + int(b)
except:
    try:
        res = float(a) + float(b)
    except:
        res = f'{a}{b}'
finally:
    print(res)
