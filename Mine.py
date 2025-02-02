import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris_data=pd.read_csv("D:\ALL DOWNLOADS\Study material\iris.data.csv")
fig=plt.gcf()
fig.set_size_inches(10,7)
fig=sns.boxplot(x="Species",y="SepalLengthCm",data=iris_data)

plt.show()
