import time


class TraficLigth:
    # атрибуты класса

    __color = "red"

    # методы класса
    def running(c):
        while c > 0:
            color = "red"
            print(color)
            time.sleep(7)
            color = "yellow"
            print(color)
            time.sleep(2)
            color = "green"
            print(color)
            time.sleep(7)
            c = c-1


a = TraficLigth.running
a(2)
