import pandas as pd

url = "https://raw.githubusercontent.com/4GeeksAcademy/decision-tree-project-tutorial/main/diabetes.csv"

df = pd.read_csv(url)

df.to_csv('diabetes_database.csv', index=False)
print("Dataset saved as 'diabetes-database.csv'")