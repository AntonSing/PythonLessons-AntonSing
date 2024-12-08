#Task 1
import re
def check_plate_type(plate):
    plate = plate.upper()
    private_car_pattern = r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$'
    taxi_pattern = r'^[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}$'
    if re.match(private_car_pattern, plate):
        return "Легковой автомобиль"
    elif re.match(taxi_pattern, plate):
        return "Такси"
    else:
        return "Некорректный номер"
plates = ["А123ВС77", "ТС45678", "М124ОП12", "ХХ123ХХ123", "А123ВВ123", "ТТ99999"]
for plate in plates:
    result = check_plate_type(plate)
    print(f"{plate}: {result}")

#Task 2
import re
text = input("Пример текста с дефис-словами и обычными:")
count_words = lambda text: len(re.findall(r'\b[а-яА-Яa-zA-Z]+(?:-[а-яА-Яa-zA-Z]+)*\b', text))
print(count_words(text))

#Task 3
import re
def replace_time_with_tbd(text):
    time_pattern = r'\b(?:[01]\d|2[0-3]):[0-5]\d(?::[0-5]\d)?\b'
    return re.sub(time_pattern, '(TBD)', text)
input_text = "Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю."
output_text = replace_time_with_tbd(input_text)
print(output_text)