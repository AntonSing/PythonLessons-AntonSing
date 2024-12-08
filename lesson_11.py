#Task 1
import pandas as pd
data = {
    'sex': ['male', 'female', 'female', 'male', 'female', 'male', 'female', 'male'],
    'vaccinated': [1, 1, 1, 1, 1, 1, 1, 1],  # 1 - вакцинирован, 0 - не вакцинирован
    'contracted_chickenpox': [1, 0, 1, 0, 0, 1, 0, 0]  # 1 - заболел, 0 - не заболел
}

df = pd.DataFrame(data)
def chickenpox_by_sex(df):
    result = {}
    for sex in ['male', 'female']:
        df_sex = df[df['sex'] == sex]
        vaccinated_and_sick = df_sex[(df_sex['vaccinated'] == 1) & (df_sex['contracted_chickenpox'] == 1)].shape[0]
        vaccinated_and_healthy = df_sex[(df_sex['vaccinated'] == 1) & (df_sex['contracted_chickenpox'] == 0)].shape[0]
        if vaccinated_and_healthy != 0:
            ratio = vaccinated_and_sick / vaccinated_and_healthy
        else:
            ratio = 0
        result[sex] = ratio
    return result
print(chickenpox_by_sex(df))