# -*- coding: utf-8 -*-
"""Materi-11 Support Vector Machine conto svm.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KWRSomWUEHAQWhDZ9dfH17hVKDE28LpZ
"""

from sklearn import svm

#DAtabase : Gerbang Logika AND
#X=Data, y=Target
x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 0, 0, 1]

#Training and clasifiy
clf = svm.SVC()
clf.fit(x,y)

#Prediksi
print ("Logika AND Metode Support Vector Machine")
print ("Logika = Prediksi")
print ("0 0 = ",clf.predict([[0, 0]]))
print ("0 1 = ",clf.predict([[0, 1]]))
print ("1 0 = ",clf.predict([[1, 0]]))
print ("1 1 = ",clf.predict([[1, 1]]))