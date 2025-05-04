#Task 1
class Animal:
    def speak(self):
        return "издает звук"

class MixinSwim:
    def swim(self):
        return "плавает"

class MixinFly:
    def fly(self):
        return "летает"

class Duck(Animal, MixinSwim, MixinFly):
    def speak(self):
        return "кря-кря"

class Penguin(Animal, MixinSwim):
    def speak(self):
        return "буль-буль"

animals = [Duck(), Penguin()]

for animal in animals:
    print(f"Животное: {animal.__class__.__name__}")
    print(f"Говорит: {animal.speak()}")
    print(f"Плавание: {animal.swim()}")
    
    # Проверяем, умеет ли животное летать
    if isinstance(animal, MixinFly):
        print(f"Полет: {animal.fly()}")
    
    print()  # Пустая строка для разделения

print("Дополнительная проверка:")
duck = Duck()
penguin = Penguin()

print(f"Утка умеет летать? {'Да' if isinstance(duck, MixinFly) else 'Нет'}")
print(f"Пингвин умеет летать? {'Да' if isinstance(penguin, MixinFly) else 'Нет'}")

#Task 2
class Writer:
    def write(self):
        return "пишет текст"

class Painter:
    def draw(self):
        return "рисует картину"

class CreativePerson(Writer, Painter):
    def write(self):
        return "творчески пишет стихотворение"
    
    def draw(self):
        return "выразительно рисует пейзаж"

creatives = [
    Writer(),
    Painter(),
    CreativePerson()
]

for person in creatives:
    print(f"\n{person.__class__.__name__}:")
    
    if hasattr(person, 'write'):
        print(f"- {person.write()}")
    
    if hasattr(person, 'draw'):
        print(f"- {person.draw()}")

print("\nДополнительная проверка:")
writer = Writer()
painter = Painter()
creative = CreativePerson()

print(f"Writer умеет рисовать? {'Да' if hasattr(writer, 'draw') else 'Нет'}")
print(f"Painter умеет писать? {'Да' if hasattr(painter, 'write') else 'Нет'}")
print(f"CreativePerson умеет и писать и рисовать? {'Да' if hasattr(creative, 'write') and hasattr(creative, 'draw') else 'Нет'}")