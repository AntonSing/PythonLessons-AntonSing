#Task 1
def find_elements_by_index(values, indices):

    result = []
    try:
        for index in indices:
            if not isinstance(index, int):
                raise TypeError(f"Индекс должен быть целым числом, получено {type(index)}")
            
            result.append(values[index])
        
        return result
    
    except IndexError as e:
        return f"Ошибка: индекс {index} выходит за границы списка (длина списка: {len(values)})"
    except TypeError as e:
        return f"Ошибка типа: {e}"

if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    valid_indices = [0, 2, 4]
    invalid_indices = [1, 3, 5]
    mixed_indices = [0, 'a', 2]
    
    print("Список чисел:", numbers)
    print("\n1. Корректные индексы:", valid_indices)
    print("Результат:", find_elements_by_index(numbers, valid_indices))
    
    print("\n2. Некорректные индексы:", invalid_indices)
    print("Результат:", find_elements_by_index(numbers, invalid_indices))
    
    print("\n3. Смешанные индексы:", mixed_indices)
    print("Результат:", find_elements_by_index(numbers, mixed_indices))

#Task 2
import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self._radius = radius  # Используем защищенный атрибут

    @property
    def radius(self):
        """Возвращает радиус круга"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Устанавливает радиус круга с проверкой"""
        if value <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self._radius = value

    @property
    def diameter(self):
        """Вычисляет диаметр круга"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        """Устанавливает диаметр (автоматически изменяя радиус)"""
        if value <= 0:
            raise ValueError("Диаметр должен быть положительным числом")
        self.radius = value / 2

    def area(self):
        """Вычисляет площадь круга"""
        return math.pi * self.radius ** 2

    def circumference(self):
        """Вычисляет длину окружности"""
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"


# Пример использования
if __name__ == "__main__":
    try:
        circle = Circle(5)
        print(circle)
        print(f"Площадь: {circle.area():.2f}")
        print(f"Длина окружности: {circle.circumference():.2f}")

        circle.diameter = 12
        print("\nПосле изменения диаметра:")
        print(circle)

        bad_circle = Circle(-1)
    except ValueError as e:
        print(f"\nОшибка: {e}")

#Task 3
class Employee:
    def __init__(self):
        self._employees = []

    def add_employee(self, name, salary):
        """Добавляет сотрудника с указанной зарплатой"""
        self._employees.append({"name": name, "salary": salary})

    @property
    def average_salary(self):
        """Вычисляет среднюю зарплату сотрудников"""
        if not self._employees:
            return 0
        total_salary = sum(emp["salary"] for emp in self._employees)
        return total_salary / len(self._employees)

    def get_sorted_employees(self):
        """Возвращает список сотрудников, отсортированный по зарплате (по возрастанию)"""
        return sorted(self._employees, key=lambda emp: emp["salary"])

# Пример использования
if __name__ == "__main__":
    company = Employee()
    company.add_employee("Иван", 50000)
    company.add_employee("Мария", 60000)
    company.add_employee("Петр", 45000)

    print("Средняя зарплата:", company.average_salary)
    print("Сотрудники по зарплате (по возрастанию):")
    for emp in company.get_sorted_employees():
        print(emp["name"], "-", emp["salary"])