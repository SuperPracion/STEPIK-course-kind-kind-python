class Model:
    def __init__(self):
        self.model = {}

    def query(self, **kwargs):
        self.model.update(kwargs)

    def __str__(self):
        res = 'Model'
        if self.model:
            res += ':' + ','.join(f'{key}={value}' for key, value in self.model.items())
        return res

model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)