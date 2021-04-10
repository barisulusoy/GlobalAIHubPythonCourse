"""
HOMEWORK3
BARIŞ ULUSOY
baris.ulusy@gmail.com
"""

print("######################################################################")
print("################### DERS NOTU HESAPLAMA UYGULAMASI ###################")
print("######################################################################")

##=> Öğrenci bilgilerinin tutulduğu sözlük
###############################################################################
student_information = {}

##> Kullanıcı tarafından girilen verilerin yazıldığı dizilerin oluşturulması
###############################################################################
student_names = []
midterm_grades  = []
project_grades = []
final_grades = []

##=> Öğrenci notlarının ortalamasının tutulduğu dizi
###############################################################################
grade_point_averages = []
grade_point_averages_dict = {}

##=> Öğrenci notlarının hesaplandığı fonksiyonun oluşturulması
###############################################################################
def calculate_average(array):
    pass_grade = array[0]*(0.3) + array[1]*(0.3) + array[2]*(0.4)
    return pass_grade

##=> Kullanıcıdan gerekli bilgilerin alınması
###############################################################################
for i in range(5):
    student_names.append(input(str(i+1)+". öğrencinin ismini giriniz!:"))
    midterm_grades.append(input(str(i+1)+". öğrencinin ara sınav notunu giriniz!:"))
    project_grades.append(input(str(i+1) + ". öğrencinin proje notunu giriniz!:"))
    final_grades.append(input(str(i+1) + ". öğrencinin final notunu giriniz!:"))

    ##=> Öğrenci bilgilerinin "student_information" sözlüğüne atanması
    student_information[str(student_names[i])] = [int(midterm_grades[i]),
                                                  int(project_grades[i]), int(final_grades[i])]

    ##=> Not ortalamalarının hesaplanıp "grade_point_averages" dizisine atanması
    grade_point_averages.append(calculate_average(student_information[str(student_names[i])]))
    grade_point_averages_dict[str(student_names[i])] = grade_point_averages[i]

##=> Öğrenci notlarının büyükten küçüğe sıralanması
###############################################################################
grade_point_averages.sort()
grade_point_averages = grade_point_averages[::-1]

print("######################################################################")
print("################################# SONUÇ ##############################")
print("######################################################################")

##=> Gerekli bilgilerin kullanıcıya gösterilmesi
###############################################################################
print("Öğrenci Bilgileri:", student_information)
print("Öğrencilerin Geçme Notları:", grade_point_averages_dict)
print("Öğrencilerin Geçme Notlarının Sıralaması:", grade_point_averages)
