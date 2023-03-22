class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')

        return super().__new__(cls, lst)


digits = list(map(float, input().split()))  # эту строчку не менять (коллекцию digits также не менять)
max_length = 5

tupleLimit = TupleLimit(digits, max_length)
try:
    print(tupleLimit)
except Exception as s:
    print('число элементов коллекции превышает заданный предел')