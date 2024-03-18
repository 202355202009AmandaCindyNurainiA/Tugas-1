# Deklarasi variabel
suhu_celsius =float(input("Input Suhu Celsius: "))

# Konversi suhu celsius ke fahrenheit
suhu_fahrenheit = (suhu_celsius * 9/5) + 32

# Konversi suhu celsius ke kelvin
suhu_kelvin = suhu_celsius + 273.15

# Konversi suhu celsius ke reamur
suhu_reamur = (suhu_celsius * 4/5)

# Cetak hasil konversi
print(f"{suhu_celsius} derajat Celsius = {suhu_fahrenheit} derajat Fahrenheit")
print(f"{suhu_celsius} derajat Celsius = {suhu_kelvin} derajat Kelvin")
print(f"{suhu_celsius} derajat Celsius = {suhu_reamur} derajat Reamur")

def cek_angka_prima(angka):
  if angka == 1:
      return False
  elif angka == 2:
      return True
  else:
      for i in range(2, angka):
          if angka % i == 0:
              return False
      return True

# Input angka bulat
angka_bulat = int(input("Input satu angka bulat: "))

# Cek apakah angka bulat adalah angka prima
if cek_angka_prima(angka_bulat):
  print(f"{angka_bulat} adalah angka prima")
else:
  print(f"{angka_bulat} bukan angka prima")

import cmath

a = float(input("Input nilai a: "))
b = float(input("Input nilai b: "))
c = float(input("Input nilai c: "))

# menghitung diskriminan
D = (b**2) - (4*a*c)

# menghitung akar persamaan
sol1 = (-b-cmath.sqrt(D))/(2*a)
sol2 = (-b+cmath.sqrt(D))/(2*a)

print("Diskriminan 4 (akar real dan berbeda)")
print("x1 = {:.2f}".format(sol1.real))
print("x2 = {:.2f}".format(sol2.real))