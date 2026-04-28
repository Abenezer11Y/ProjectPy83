import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('Iris Dataset.csv')

sns.barplot(x=df["Species"], y=df["SepalLengthCm"], color="green")
plt.show()

sns.countplot(x=df['Species'], color="green")
plt.show()

sns.boxplot(x=df["Species"], y=df["SepalWidthCm"], color="green")
plt.show()

sns.swarmplot(x=df["Species"], y=df["SepalWidthCm"], color="green")
plt.show()

sns.displot(df['SepalWidthCm'], kde=False, rug=True)
plt.show()

sns.jointplot(df['SepalWidthCm'])
plt.show()

sns.pairplot(df, hue="Species")
plt.show()