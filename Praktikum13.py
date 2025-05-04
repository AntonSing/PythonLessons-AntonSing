#Task 1
import json

class UserProfile:
    def __init__(self, name: str, age: int, interests: list):
        self.name = name
        self.age = age
        self.interests = interests

    def to_dict(self) -> dict:
        """Преобразует объект UserProfile в словарь."""
        return {
            "name": self.name,
            "age": self.age,
            "interests": self.interests
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'UserProfile':
        """Создает объект UserProfile из словаря."""
        return cls(data["name"], data["age"], data["interests"])

def save_profile(user: UserProfile, filename: str) -> None:
    """Сохраняет профиль пользователя в JSON-файл."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(user.to_dict(), file, ensure_ascii=False, indent=4)
    except (IOError, json.JSONEncodeError) as e:
        print(f"Ошибка при сохранении файла: {e}")

def load_profile(filename: str) -> UserProfile:
    """Загружает профиль пользователя из JSON-файла."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return UserProfile.from_dict(data)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except json.JSONDecodeError:
        print("Ошибка: Файл содержит невалидный JSON.")
    except KeyError as e:
        print(f"Ошибка: В файле отсутствует обязательное поле - {e}.")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
    return None

# Пример использования
user = UserProfile("Alice", 25, ["Python", "AI"])
save_profile(user, "profile.json")
new_user = load_profile("profile.json")

if new_user:
    print(f"Загружен пользователь: {new_user.name}, {new_user.age}, {new_user.interests}")

#Task 2
import pickle
import os

class Task:
    def __init__(self, name: str, priority: int, is_completed: bool = False):
        self.name = name
        self.priority = priority
        self.is_completed = is_completed

    def __repr__(self):
        status = "✓" if self.is_completed else "✗"
        return f"{self.name} (Приоритет: {self.priority}, Статус: {status})"

def load_tasks(filename: str) -> list[Task]:
    """Загружает список задач из файла. Если файла нет, возвращает пустой список."""
    if not os.path.exists(filename):
        return []
    
    try:
        with open(filename, "rb") as file:
            tasks = pickle.load(file)
            return tasks
    except EOFError:
        print("Файл пуст. Будет создан новый список задач.")
        return []
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return []

def save_tasks(tasks: list[Task], filename: str) -> None:
    """Сохраняет список задач в файл."""
    try:
        with open(filename, "wb") as file:
            pickle.dump(tasks, file)
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

def add_task(tasks: list[Task], name: str, priority: int) -> None:
    """Добавляет новую задачу в список."""
    tasks.append(Task(name, priority))

def delete_task(tasks: list[Task], index: int) -> None:
    """Удаляет задачу по индексу."""
    if 0 <= index < len(tasks):
        tasks.pop(index)
    else:
        print("Ошибка: Некорректный индекс.")

def mark_task_completed(tasks: list[Task], index: int) -> None:
    """Помечает задачу как выполненную."""
    if 0 <= index < len(tasks):
        tasks[index].is_completed = True
    else:
        print("Ошибка: Некорректный индекс.")

def print_tasks(tasks: list[Task]) -> None:
    """Выводит список задач."""
    if not tasks:
        print("Список задач пуст.")
        return
    
    for i, task in enumerate(tasks):
        print(f"{i}. {task}")

# Пример использования
filename = "tasks.pickle"
tasks = load_tasks(filename)

add_task(tasks, "Закончить проект", 3)
add_task(tasks, "Купить продукты", 1)
add_task(tasks, "Позвонить другу", 2)

mark_task_completed(tasks, 1)
delete_task(tasks, 0)
save_tasks(tasks, filename)
print_tasks(tasks)

#Task 3
import json
from typing import List, Dict, Optional

class UserValidator:
    @staticmethod
    def validate_user(user_data: Dict) -> Optional[Dict]:
        """Проверяет корректность данных пользователя"""
        try:
            # Проверка обязательных полей
            if not all(key in user_data for key in ['id', 'name', 'email']):
                raise ValueError("Отсутствуют обязательные поля")
            
            # Проверка типов
            if not isinstance(user_data['id'], int):
                raise ValueError("Поле id должно быть целым числом")
            if not isinstance(user_data['name'], str):
                raise ValueError("Поле name должно быть строкой")
            if not isinstance(user_data['email'], str):
                raise ValueError("Поле email должно быть строкой")
            
            # Проверка email
            if '@' not in user_data['email']:
                raise ValueError("Email должен содержать @")
            
            return user_data
        
        except ValueError as e:
            print(f"Ошибка в пользователе {user_data.get('id', 'N/A')}: {e}")
            return None

def load_users(filename: str) -> tuple[List[Dict], int]:
    """Загружает и проверяет пользователей из JSON-файла"""
    valid_users = []
    invalid_count = 0
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            users_data = json.load(file)
            
            if not isinstance(users_data, list):
                raise ValueError("Файл должен содержать список пользователей")
            
            for user in users_data:
                validated = UserValidator.validate_user(user)
                if validated:
                    valid_users.append(validated)
                else:
                    invalid_count += 1
    
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    except json.JSONDecodeError:
        print("Ошибка: Невалидный JSON")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
    
    return valid_users, invalid_count

# Пример использования
if __name__ == "__main__":
    valid_users, invalid_count = load_users("users.json")
    print(f"\nУспешно загружено пользователей: {len(valid_users)}")
    print(f"Пропущено некорректных пользователей: {invalid_count}")
    print("\nЗагруженные пользователи:")
    for user in valid_users:
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
