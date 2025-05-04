# Task 5

class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    def __init__(self, value):
        if not self._initialized:
            self._value = value
            self._initialized = True
s1 = Singleton(10)
s2 = Singleton(20)
print(s1._value)
print(s1 is s2)

# Task 6
class DynamicAttrs:
    def __setattr__(self, name, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Значение атрибута {name} должно быть числом int/float, получено: {type(value)}")
        super().__setattr__(name, value)
    def __getattr__(self, name):
        return 0
obj = DynamicAttrs()
obj.x = 5
print(obj.x)
print(obj.z)
obj.y = "text"