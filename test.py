import seaborn as sns
import matplotlib.pyplot as plt

# Load the example Titanic dataset
penguins = sns.load_dataset("penguins")  # 导入数据

# Draw a nested barplot to show survival for class and sex
g = sns.catplot(
    x="species",
    y="flipper_length_mm",
    hue="species",
    data=penguins,
    kind="bar",
    height=6,
    aspect=2,
)
g.despine(left=True)
g.set_ylabels("survival probability")

plt.show()

