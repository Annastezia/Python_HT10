class Worker:
    def __init__(
            self,
            name: str,
            surname: str,
            position: str,
            wage: float = 0,
            bonus: float = 0
    ):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self, reverse=False):
        return ' '.join(sorted([self.name, self.surname], reverse=reverse))

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    position_data = [
        {
            'name': 'Людмила',
            'surname': 'Сергеева',
            'position': 'Project manager',
            'wage':  90000,
            'bonus': 0
        },
        {
            'name': 'Алексей',
            'surname': 'Синицын',
            'position': 'DevOps',
            'wage':  120000,
            'bonus': 60000
        },
        {
            'name': 'Мария',
            'surname': 'Кузнецова',
            'position': 'Team-lead',
            'wage':  80000,
            'bonus': 30000
        },
    ]

    for item in position_data:
        position = Position(**item)

        print('#######################################')
        print('Full name: ', position.get_full_name())
        print('Total income: ', position.get_total_income())
        print('#######################################\n\n')