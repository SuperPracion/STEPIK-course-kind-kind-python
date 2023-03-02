class SoftList(list):
    def __init__(self, *args):
        super().__init__(*args)

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except:
            return False


sl = SoftList("python")
print(sl[0])  # 'p'
print(sl[-1])  # 'n'
print(sl[6])  # False
print(sl[-7])  # False
