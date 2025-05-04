#Task 1


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)



    def __setattr__(self, key, value):
        print(key, value)
        if   key == 'name' and value == '' :
            raise ValueError('Name cannot be empty!')
        elif key == 'age' and value < 0:
            raise ValueError("Age must be a positive number!")
        else:
            return object.__setattr__(self, key, value)
p = Person("John", 25)  # Успешно
p.name = "Alice"         # Успешно
p.age = 30               # Успешно
p.name = ""              # ValueError: Name cannot be empty!
p.age = -5               # ValueError: Age must be a positive number!



#Task 2

class Counter:
    
    def __getattribute__(self, item):
        print(f'Доступ к атрибуту {item}')
        return object.__getattribute__(self, item)
    
    def __getattr__(self, item):
        return None
    
    
c = Counter()
c.value = 5         # Атрибут value будет добавлен
print(c.value)      # Доступ к атрибуту value → 5
print(c.name)       # Доступ к атрибуту name → None


#Task 3

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def __getattribute__(self, item):
        
        return object.__getattribute__(self, item)
    
    def __getattr__(self, item):
        return 'This attribute is not available'
    
c = Car("Toyota", "Corolla")
print(c.make)      # Toyota
print(c.color)     # This attribute is not available

#Task 4

class Rectangle:
    def __init__(self, width, height):
        self.__dict__["width"] = int(width)
        self.__dict__["height"] = int(height)
    
    def __setattr__(self, key, value):
        if key not in self.__dict__:
            raise AttributeError(f"Local attributes are not allowed")
        self.__dict__[key] = value

r = Rectangle(10, 20)
r.width = 15  # Успешно
r.height = 25 # Успешно
r.color = 'red'  # AttributeError: Local attributes are not allowed