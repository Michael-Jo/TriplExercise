print("<<<\t\tLatihan\t\t>>>")
print("Berikut akan tampil list dengan kondisi :")
print("1. range(1, 100)")
print("2. Value/item : genap ( i >= 10 dan i <= 20 )")
print("3. Value/item : ganjil ( i >= 90 dan i <= 100 )")
# DataBase = [i for i in range (1, 100)]
# print(f"{DataBase}") range(1,100)
DataEven = [i for i in range (1, 100) if i % 2 == 0 and i >= 10 and i <= 20]
# print(f"{DataEven}")
DataOdd = [ i for i in range (1, 100) if i % 2 == 1 and i >= 90 and i <= 100]
print(f"{DataEven + DataOdd}")