import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# hien len thong tin trong bang
df = pd.read_csv('Housing.csv')
df.columns = ["price", "area", "bedrooms", "bathrooms", "stories", "mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "parking", "prefarea", "furnishingstatus"]
print(df.head())
# hien len bang thong tin truc quan hoa du lieu
sns.scatterplot(x='area', y='price', data=df)
plt.title('price vs area')
plt.xlabel('area')
plt.ylabel('price')
plt.show()

# lay x va y
x = df['area'].values
y = df['price'].values

# tim m and b
N = x.shape[0]
m = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / (N * np.sum(x ** 2) - (np.sum(x) ** 2))
b = (np.sum(y) - m * np.sum(x)) / N
print(f"m : {m}")
print(f"b : {b}")
# ve duong thang hoi quy tuyen tinh
x_min = np.min(x)
y_min = m * x_min + b
x_max = np.max(x)
y_max = m * x_max + b

fig, ax = plt.subplots()
sns.scatterplot(x='area', y='price', data=df, alpha=0.5)
sns.lineplot(x=[x_min, x_max], y=[y_min, y_max],linewidth=1.5, color='red')
plt.show()