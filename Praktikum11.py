#Task 1
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    __slots__ = ('x', 'y', '_z')
    
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z
    
    @property
    def z(self):
        return self._z
    
    @z.setter
    def z(self, value):
        raise AttributeError("Изменение координаты z запрещено")

#Test
if __name__ == "__main__":
    pt3 = Point3D(10, 20, 30)
    
    print(f"x: {pt3.x}, y: {pt3.y}, z: {pt3.z}")
    
    try:
        pt3.z = 40
    except AttributeError as e:
        print(f"Ошибка при изменении z: {e}")
    
    try:
        pt3.extra = 100
    except AttributeError as e:
        print(f"Ошибка при добавлении атрибута: {e}") 
    
    try:
        print(pt3.__dict__)
    except AttributeError as e:
        print(f"Ошибка при обращении к __dict__: {e}")

#Task 2
import sys
import timeit

class NormalPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class SlotPoint:
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

normal_points = [NormalPoint(i, i) for i in range(1000)]
slot_points = [SlotPoint(i, i) for i in range(1000)]

normal_time = timeit.timeit(
    'for p in normal_points: p.move(1, 1)',
    setup='from __main__ import normal_points',
    number=1000
)

slot_time = timeit.timeit(
    'for p in slot_points: p.move(1, 1)',
    setup='from __main__ import slot_points',
    number=1000
)

normal_size = sys.getsizeof(normal_points[0])
slot_size = sys.getsizeof(slot_points[0])

# Вывод результатов
print("Результаты тестирования:")
print(f"NormalPoint время выполнения: {normal_time:.6f} сек")
print(f"SlotPoint время выполнения: {slot_time:.6f} сек")
print(f"Ускорение: {normal_time/slot_time:.2f}x")
print(f"\nРазмер объекта NormalPoint: {normal_size} байт")
print(f"Размер объекта SlotPoint: {slot_size} байт")
print(f"Экономия памяти: {normal_size - slot_size} байт на объект")

print("\nДемонстрация различий:")
normal_p = NormalPoint(1, 2)
slot_p = SlotPoint(1, 2)

try:
    normal_p.z = 3
    print("NormalPoint: успешно добавлен атрибут z")
except Exception as e:
    print(f"NormalPoint: ошибка при добавлении атрибута - {e}")

try:
    slot_p.z = 3
    print("SlotPoint: успешно добавлен атрибут z")
except Exception as e:
    print(f"SlotPoint: ошибка при добавлении атрибута - {e}")

print(f"\nNormalPoint имеет __dict__: {'__dict__' in dir(normal_p)}")
print(f"SlotPoint имеет __dict__: {'__dict__' in dir(slot_p)}")

#Task 3
class Student:
    __slots__ = ['name', 'age', 'grade']
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def calculate_average_grade(students):
    """Вычисляет среднюю оценку студентов"""
    if not students:
        return 0.0
    
    total = sum(student.grade for student in students)
    return total / len(students)

students = [
    Student("Иван Иванов", 20, 4.5),
    Student("Петр Петров", 21, 3.8),
    Student("Сидор Сидоров", 19, 4.2),
    Student("Мария Кузнецова", 20, 4.9),
    Student("Ольга Смирнова", 22, 3.5)
]

average_grade = calculate_average_grade(students)
print(f"Средняя оценка студентов: {average_grade:.2f}")

try:
    students[0].email = "ivan@example.com"
except AttributeError as e:
    print(f"\nОшибка при добавлении атрибута: {e}")

#Task 4
class Product:
    __slots__ = ['name', 'price', 'quantity']
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"


def get_products_above_price(products_dict, threshold_price):
    """Возвращает список названий товаров с ценой выше пороговой"""
    return [name for name, product in products_dict.items() if product.price > threshold_price]

products = {
    "Ноутбук": Product("Ноутбук", 1200.50, 15),
    "Смартфон": Product("Смартфон", 800.00, 30),
    "Наушники": Product("Наушники", 150.75, 50),
    "Планшет": Product("Планшет", 450.30, 20),
    "Монитор": Product("Монитор", 300.99, 25)
}

threshold = 400.00
expensive_products = get_products_above_price(products, threshold)

print(f"Товары дороже {threshold}:")
for product_name in expensive_products:
    print(f"- {product_name}: {products[product_name].price}")

try:
    products["Ноутбук"].discount = 0.1
except AttributeError as e:
    print(f"\nОшибка при добавлении атрибута: {e}")