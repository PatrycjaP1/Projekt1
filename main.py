import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
bmi = pd.read_csv("bmi2")
palette_dict = {x: "gray" for x in bmi.imie.unique()}
palette_dict["wygłodzenie"] = "navy"
palette_dict["wychudzenie"] = "blue"
palette_dict["niedowaga"] = "palegreen"
palette_dict["pożądana masa ciała"] = "green"
palette_dict["nadwaga"] = "yellow"
palette_dict["otyłość pierwszego stopnia"] = "orange"
palette_dict["otyłość drugiego stopnia"] = "red"
palette_dict["otyłość trzeciego stopnia"] = "darkred"
g = sns.catplot(
    data=bmi,
x="imie", y="bmi", hue="kategoria", s=15, palette=palette_dict,
)

g.despine(left=True)
g.set_axis_labels("Osoba", "Wartość Bmi")
plt.show()