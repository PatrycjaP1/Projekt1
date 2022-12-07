import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
bmi = pd.read_csv("bmi2")

g = sns.relplot(
    data = bmi,
    hue="kategoria",
    x="imie", y="bmi",
    palette="dark",
    alpha=.6,
    height=7
)
g.despine(left=True)
g.set_axis_labels("Osoba","Wartość Bmi")
plt.show()