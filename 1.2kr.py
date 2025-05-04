#Task 1.2
list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
total_players = len(list_players)
print(f"Общее количество игроков: {total_players}")
middle_index = total_players // 2
first_team = list_players[:middle_index]
second_team = list_players[middle_index:]
print(f"Игроки в первой команде: {first_team}")
print(f"Игроки во второй команде: {second_team}")