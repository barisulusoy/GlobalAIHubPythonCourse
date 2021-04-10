"""
HOMEWORK1
BARIŞ ULUSOY
baris.ulusy@gmail.com
"""

print("######################################################################")
print("############################## 1. KISIM ##############################")
print("######################################################################")

##=> Dizinin oluşturulması ve terminal'e yazdırılması
###############################################################################
my_array = [1, 8, 3, 13, 97, 128, 6, 88, 91, 2021]
print("Oluşturulan Dizi:", my_array)

##=> Dizinin kaça bölüneceğinin belirlenmesi
###############################################################################
number = 2
average = len(my_array) / float(number)
last_number = 0.0

##=> Bölünmüş dizinin tutulacağı dizinin oluşturulması
###############################################################################
out_array = []

##=> Dizinin bölünmesi işlemi
###############################################################################
while last_number < len(my_array):
    out_array.append(my_array[int(last_number):int(last_number + average)])
    last_number = last_number + average

##=> Bölünen dizinin iki farklı dizide saklanması
###############################################################################
first_half = out_array[0]
second_half = out_array[1]

##=> Oluşturulan dizinin tüm elemanlarının silinmesi
###############################################################################
for i in range(len(my_array)):
    my_array.pop()

##=> Dizinin istenilen formatta yeniden oluşturulması
###############################################################################
for i in range(len(second_half)):
    my_array.append(second_half[i])
for i in range(len(first_half)):
    my_array.append(first_half[i])

##=> Oluşturulan yeni diznin ekranda gösterilmesi
###############################################################################
print("Değiştirilen Dizi:", my_array)

print("######################################################################")
print("############################## 2. KISIM ##############################")
print("######################################################################")

##=> Sonsuz döngü sayesinde kullanıcı hatalı giriş yaparsa, uyarılır
##=> ve yeniden değer girmesi sağlanır:
###############################################################################
while True:

    ##=> Kullanıcının değer girmesi işlemi
    n = (input("Tek basamaklı bir tamsayı giriniz!:"))

    try:
        ##=> Kullanıcı 0 veya tek basamaklı pozitif tam sayı girmiş ise:
        if len(str(n)) == 1 and int(n) >= 0:
            even_numbers = []
            for i in range(0, int(n)+1, 1):
                if i % 2 == 0:
                    even_numbers.append(i)
            print(str(n)+"'e kadar olan çift sayılar:", even_numbers)
            break

        ##=> Kullanıcı tek basamaklı negatif tam sayı girmiş ise:
        elif len(str(n)) == 2 and int(n) < 0:
            even_numbers = []
            for i in range(0, int(n)-1, -1):
                if i%2 == 0:
                    even_numbers.append(i)
            print(str(n)+"'e kadar olan çift sayılar:", even_numbers)
            break

        ##=> Kullanıcı hatalı bir giriş yapmış ise:
        else:
            print("Lütfen tek basamaklı bir tam sayı giriniz!")

    except:
        print("Lütfen tek basamaklı bir tam sayı giriniz!")