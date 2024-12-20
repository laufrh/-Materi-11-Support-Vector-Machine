# -*- coding: utf-8 -*-
"""Materi-11_support_vector_trapezoid_fungsi_Soal3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1m75Zy8chQOy1G3KPEaKrCkbdqVu30fpZ
"""

def Trapezoid(a, b, f):
    '''
        Fungsi untuk mencari integral trapezoid numerik.
        Parameter:
        a: batas bawah
        b: batas atas
        f: fungsi yang akan diintegralkan
    '''
    n = 100  # Jumlah segmen
    h = (b - a) / n
    sum = 0.0
    for i in range(1, n):
        x = a + i * h
        sum += f(x)
    integral = (h / 2) * (f(a) + 2 * sum + f(b))  # Rumus trapezoid
    return integral

# Looping untuk menghasilkan nilai tabel
print("a,b,Target")
for i in range(1, 6):
    a, b = i, i + 1
    target = Trapezoid(a, b, lambda x: 2 * x + 4 )
    print(f"{a},{b},{round(target, 2)}")