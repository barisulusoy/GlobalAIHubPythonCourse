"""
FINAL PROJECT
BARIŞ ULUSOY
baris.ulusy@gmail.com
"""

print("######################################################################")
print("##################### BİLGİ YARIŞMASI UYGULAMASI #####################")
print("######################################################################")

##=> Cevapların tutulduğu sözlük
###############################################################################
answer_keys = {
                "question_1" : "katı",
                "question_2" : "mars",
                "question_3" : "everest",
                "question_4" : "kayı",
                "question_5" : "kokpit",
                "question_6" : "bakü",
                "question_7" : "kırılma",
                "question_8" : "rize",
                "question_9" : "simograf",
                "question_10" : "ısparta"
}

##=> Kullanıcının verdiği cevapların tutulduğu dizinin oluşturulması
###############################################################################
user_responses = []

##=> Soruların kullanıcıya sorulması, cevapların "user_responses" dizisine atılması
###############################################################################
user_responses.append(input("1. SORU: Ses en hızlı hangi ortamda yayılır?:").
                      replace("I", "ı").replace("İ", "i").lower())  ##=> Katı
user_responses.append(input("2. SORU: 'Kızıl Gezegen' olarak adlandırılan gezegen hangisidir?:").
                      replace("I", "ı").replace("İ", "i").lower()) ##=> Jupiter
user_responses.append(input("3. SORU: Dünyanın en yüksek dağı?:").
                      replace("I", "ı").replace("İ", "i").lower())  ##=> Everest
user_responses.append(input("4. SORU: Osmanlı Devletinin kurucusu olan Osmanlı ailesi hangi Türk boyuna mensuptur?:").
                      replace("I", "ı").replace("İ", "i").lower())  ##=> Kayı
user_responses.append(input("5. SORU: Uçaklarda pilot kabinine ne ad verilir?:").
                      replace("I", "ı").replace("İ", "i").lower())  ##=> Kokpit
user_responses.append(input("6. SORU: Azerbaycan'ın başkenti neresidir?:").
                      replace("I", "ı").replace("İ", "i").replace("I", "ı").replace("İ", "i").lower())  ##=> Bakü
user_responses.append(input("7. SORU: Mercekler ışığın hangi özelliği kullanılarak yapılmıştır?:").
                      replace("I", "ı").replace("İ", "i").lower())  ##=> Kırılma
user_responses.append(input("8. SORU: Türkiye'nin en fazla yağış alan ili hangisidir?:").
                      replace("I", "ı").replace("İ", "i").lower())  ##=> Rize
user_responses.append(input("9. SORU: Depremin büyüklüğünü ve süresini ölçen alete ne ad verilir?:").
                      replace("I", "ı").replace("İ", "i").lower())  ##=> Simograf
user_responses.append(input("10. SORU: Gülü ile meşhur olan ilimiz hangisidir?:").
                      replace("I", "ı").replace("İ", "i").lower())  ##=> Isparta

##=> Kullanıcı cevaplarının kontrol edilmesi:
###############################################################################
i = 0
total_score = 0
for key,value in answer_keys.items():
    if value == user_responses[i]:
        total_score += 10
    i += 1

print("######################################################################")
print("############################## SONUÇ #################################")
print("######################################################################")

##=> Kullanıcı başarısının belirlenmesi:
###############################################################################
if total_score > 50:
    print(str(total_score)+" puan alarak sınavda BAŞARILI oldunuz!")
else:
    print(str(total_score)+" puan alarak sınavda BAŞARISIZ oldunuz!")

print("######################################################################")
print("######################### CEVAP ANAHTARI #############################")
print("######################################################################")

##=> Cevapların kullanıcıya gösterilmesi
###############################################################################
print("Cevap Anahtarı:", answer_keys.values())
print("Kullanıcı Cevapları:",user_responses)