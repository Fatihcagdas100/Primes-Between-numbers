import math

baslangicS = int(input("Başlangıç sayısını giriniz: "))
bitisS = int(input("Bitiş sayısını giriniz: "))

if baslangicS <= 1:
    baslangicS = 2

for i in range(bitisS, baslangicS - 1, -1):
    kok = int(math.sqrt(i))
    kontrol = True
    for j in range(2, kok + 1):
        if i % j == 0:
            kontrol = False
            break
    if kontrol:
        print(i)
