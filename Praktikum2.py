#Task 1

class Saus:
    OSNOVA = 'Майонез'
    def __init__(self, dobavka=OSNOVA):
        self.dobavka=dobavka
    def show_my_souce(self):
        print('Соус', self.dobavka)
    
pt = Saus()
pt.show_my_souce()

#Task 2

class Employee:
    SALARY = 50000
    def __init__(self, name, age):
        self.name = name         
        self._age = age          
        self.__salary = Employee.SALARY
        self.__bonus = 0
            

    def get_name(self):
        print( self.name)
    
    def get_age(self):
        print( self._age)
    
    def get_salary(self):
        print( self.__salary)
    
    def get_bonus(self):
        print( self.__bonus)
    
    def set_bonus(self, x):
        self.__bonus = x

    def get_total_salary(self):
        print( self.__salary + self.__bonus)
    
pt = Employee('Max',19)
pt.get_name()
pt.get_age()
pt.get_salary()
pt.get_bonus()
pt.set_bonus(99999)
pt.get_total_salary()



#Task 3

class Recipe:
    def __init__(self, name,ingredients):
        self.name = name         
        self.ingredients = ingredients         

    def print_ingredients(self):
        print(f'Ингредиенты для {self.name}:')
        for i in self.ingredients:
            print(f'- {i}')
    
    def cook(self):
        print( f'Сегодня мы готовим {self.name}.')
        print( f'Выполняем инструкцию по приготовлению блюда {self.name}...')
        print( f'Блюдо {self.name} готово!')

spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
spaghetti.print_ingredients()
spaghetti.cook()  
cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
cake.print_ingredients()
cake.cook()