# put your python code here
def input_int_numbers():
    try:
        return ' '.join([*map(str, map(int, input().split()))])
    except:
        raise TypeError('все числа должны быть целыми')

while True:
    try:
        res = input_int_numbers()
    except:
        pass
    else:
        print(res)
        break
