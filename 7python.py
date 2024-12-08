#Task 1
def read_last(lines, file):
    if not isinstance(lines, int) or lines <= 0:
        print("Количество строк должно быть положительным целым числом.")
        return

    try:
        with open(file, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
            
            last_lines = all_lines[-lines:]
            
            for line in last_lines:
                print(line.strip())  
    except FileNotFoundError:
        print(f"Файл {file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

read_last(3, 'article.txt')

#Task 2
import os

def print_docs(directory):
    if not os.path.exists(directory):
        print(f"Папка {directory} не существует.")
        return
    
    if not os.path.isdir(directory):
        print(f"{directory} не является директорией.")
        return

    for root, dirs, files in os.walk(directory):
        print(f"Каталог: {root}")
        
        if dirs:
            print(f"  Вложенные папки: {', '.join(dirs)}")
        
        if files:
            print(f"  Файлы: {', '.join(files)}")
        print("-" * 40)

directory_path = "article.txt"
print_docs(directory_path)

#Task 3
def longest_words(file):
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
    import re
    words = re.findall(r"\b\w+\b", text)
    max_length = max(len(word) for word in words)
    longest = [word for word in words if len(word) == max_length]
    return longest
file_path = "article.txt"
result = longest_words(file_path)
print(result)