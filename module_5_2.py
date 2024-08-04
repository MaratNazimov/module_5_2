class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if self.number_of_floors > new_floor > 1:
                print(i)
            else:
                print("Такого этажа не существует")
                break

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return self.name


House_1 = House('ЖК Горский', 18)
House_2 = House('Домик в деревне', 2)
House_3 = House('ТК "Северный"', 4)

House_1.go_to(5)
House_2.go_to(10)
House_3.go_to(3)

print(str(House_1))
print(str(House_2))
print(str(House_3))

print(len(House_1))
print(len(House_2))
print(len(House_3))

print(f'Название: {str(House_1)}, количество этажей: {len(House_1)} ')
print(f'Название: {str(House_2)}, количество этажей: {len(House_2)} ')
print(f'Название: {str(House_3)}, количество этажей: {len(House_3)} ')
