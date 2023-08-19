import numpy as np
import pandas as pd
import scipy.stats as sps

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# чтение данных из excel
def read_excel(name):
    return pd.read_excel(name, skiprows=0, usecols='A:B')


# данные, которые хотим отобразить
data = read_excel('data.xlsx')
x = data['A'][0:12]
y = data['B'][0:12]
x = np.array(pd.to_numeric(x))
y = np.array(pd.to_numeric(y))
# настройка параметров графика
# размер
plt.figure(figsize=(8, 6))
# выбор контекста ('notebook', 'paper', 'talk', 'poster')
sns.set(context = 'notebook')
# выбор стиля ('darkgrid', 'whitegrid', 'dark', 'white', 'ticks')
sns.set(style = 'whitegrid')
# название графика
plt.title(r'Название графика', fontsize=16)
# подпись оси x
plt.xlabel('Подпись оси x', fontsize=14)
# подпись оси y
plt.ylabel('Подпись оси y', fontsize=14)
# текст на графике
plt.text(x.min()+0.1*(x.max()-x.min()), y.min()+0.9*(y.max()-y.min()), r'$e=\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n$', fontsize=18, bbox=dict(edgecolor='w', color='w'))

# построение графика
# фиттинг линейной зависимостью
coef, V = np.polyfit(x, y, 1, cov=True)
a, b = coef[0], coef[1]
fit_x = np.linspace(x.min(), x.max(), 100)
fit_y = a*fit_x + b
plt.plot(fit_x, fit_y, '--', linewidth = 1.5, color = 'b', label = str(r'$y = ax + b$' +'\n'+'$a=$'+ str(round(a, 3)) +'\n'+ '$b=$' + str(round(b, 3))))
print(r'Уравнение прямой: y = ax + b, a =', a, ', b =', b)
print('sigma a:', np.sqrt(V[0][0]), ', sigma b:', np.sqrt(V[1][1]))
# нанесение точек с крестами погрешностей
plt.errorbar(x, y, fmt = 'o-r', xerr = np.sqrt(V[0][0]), yerr = np.sqrt(V[1][1]), linewidth = 0, elinewidth = 1)
# добавляем легенду
plt.legend()
# сохраняем в pdf
plt.savefig('sample.pdf')

# сохраняем в png с выбранным dpi
plt.savefig('sample.png', dpi = 400)
# смотрим на результат
plt.show()