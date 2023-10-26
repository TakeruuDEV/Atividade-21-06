import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tabela_alunos.xlsx")

print(df.head())

print(df.describe())

print(df.shape[0])

print(len(df[df["saída"] == ""]))

print(len(df) - len(df[df["saída"] == ""])

print(df[df["saída"] == ""].sort_values(by="entrada", ascending=False).head(1))

print(df[df["saída"] == ""].sort_values(by="entrada").head(1))

plt.bar(["Presentes", "Ausentes"], [len(df[df["saída"] == ""]), len(df) - len(df[df["saída"] == ""])])
plt.show()
