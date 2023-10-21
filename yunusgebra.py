# Kütüphaneleri içe aktarma
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import tkinter as tk
import time

# Fonksiyonu tanımlama
def f(x):
    return x**2 - 2*x + 1

# x değerlerini oluşturma
x = np.linspace(-5, 5, 100)

# y değerlerini hesaplama
y = f(x)

# Grafiği çizme
plt.plot(x, y, label="f(x)")

# x sembolünü tanımlama
x = sp.Symbol("x")

# Fonksiyonun köklerini bulma
roots = sp.solve(f(x), x)
print("Fonksiyonun kökleri:", roots)

# Fonksiyonun tepe noktasını bulma
vertex_x = -sp.diff(f(x), x) / (2 * sp.diff(f(x), x, x))
vertex_y = f(vertex_x)
print("Fonksiyonun tepe noktası:", (vertex_x, vertex_y))

# Fonksiyonun y-kesişim noktasını bulma
y_intercept = f(0)
print("Fonksiyonun y-kesişim noktası:", y_intercept)

# Grafiğe kökleri, tepe noktasını ve y-kesişim noktasını ekleme
plt.scatter(roots, [0, 0], color="red", label="kökler") # Burada x ve y yerine roots ve [0, 0] verdim.
plt.scatter(vertex_x, vertex_y, color="green", label="tepe noktası")
plt.scatter(0, y_intercept, color="blue", label="y-kesişim noktası")

# Fonksiyonun türevini bulma
derivative = sp.diff(f(x), x)
print("Fonksiyonun türevi:", derivative)

# Fonksiyonun türevinin grafiğini çizme
x = np.linspace(-5, 5, 100)
y = derivative.subs(sp.Symbol("x"), x)
plt.plot(x, y, label="f'(x)")

# Fonksiyonun integralini bulma
integral = sp.integrate(f(x), x)
print("Fonksiyonun integrali:", integral)

# Fonksiyonun integralinin grafiğini çizme
x = np.linspace(-5, 5, 100)
y = integral.subs(sp.Symbol("x"), x)
plt.plot(x, y, label="F(x)")

# Grafiği düzenleme
plt.xlabel("x")
plt.ylabel("y")
plt.title("Bir Fonksiyonun Grafiği")
plt.grid()
plt.legend()

# Açılış ekranını oluşturma
window = tk.Tk()
window.title("Matematik Uygulaması")
window.geometry("300x200")
label = tk.Label(window, text="Yapımcı: 11shellbee11\nSürüm: 0.35.1", font=("Arial", 20))
label.pack()
button = tk.Button(window, text="Grafiği Göster", command=window.destroy)
button.pack()

# Açılış ekranını gösterme
window.mainloop()

# Grafiği gösterme
plt.show()
