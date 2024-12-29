import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

with open("tips.csv", "r") as csv_file:
    tips = pd.read_csv(csv_file, delimiter=",")


tips_pivoted = tips.pivot_table(
    values="tip",
    index=["size"],
    columns=["time"]
)

fig = sns.heatmap(tips_pivoted, annot=True, cmap="coolwarm")

fig.set_ylim(0,5)

plt.xlabel("Meal Eaten")
plt.ylabel("Party Size")
plt.title("When are the biggest tips?")

plt.savefig("time-tipsize.png")
