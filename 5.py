class NotNumber(ValueError):
    def __init__(self, txt):
        self.txt = txt

    def is_number(self):
        try:
            float(self)
            return True
        except ValueError:
            return False


my_list = []
while True:
    try:
        value = input(
            'Введите число для добавления в список, для выхода <stop>')
        if value == 'stop':
            break
        if not NotNumber.is_number(value):
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as ex:
        print(f"{ex} - Это не число!")
print(my_list)
