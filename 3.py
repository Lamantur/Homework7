class Worker:
    name: str
    surname: str
    position: str
    income_list = {30000: 5000, 40000: 7000, 50000: 8000,
                   60000: 9000, 70000: 10000, 80000: 11000, 100000: 15000}
    _income = income_list

    def __init__(self, name, surname, income, position) -> None:
        self.name = name
        self.surname = surname
        self.income = income
        self.position = position


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self, income):

        return self.income_list.get(income) + income

    def __str__(self) -> str:
        return f"{self.name} {self.surname}, {self.position}: {self.income + self.income_list.get(self.income)}"


ivanivanov = Position("Иван", "Иванов", 30000, "Директор")


print(ivanivanov.get_total_income(ivanivanov.income))
print(ivanivanov)
