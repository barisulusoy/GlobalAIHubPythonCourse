"""
HOMEWORK2
BARIŞ ULUSOY
baris.ulusy@gmail.com
"""

print("######################################################################")
print("################## KULLANICI OTURUM AÇMA UYGULAMASI ##################")
print("######################################################################")

##=> Kullanıcı adının ve şifresinin oluşturulması
###############################################################################
user_information = {
    "user_name": "GlobalAiHub",
    "user_password": "python",
}

##=> Oturum açma veya kayıt olma işleminin seçilmesi
###############################################################################
status_query = input("Oturum açmak için 1, kayıt olmak için 2 yazınız!:")

##=> Kullanıcının başarılı bir oturum açması için sonsuz döngü oluşturulması
###############################################################################
while True:

    ##=> Oturum Açma
    if status_query == "1":

        print("######################################################################")
        print("########################### OTURUM AÇMA  #############################")
        print("######################################################################")

        user_name = input("Lütfen kullanıcı adınızı giriniz!:")
        user_password = input("Lütfen kullanıcı şifrenizi giriniz!:")

        if (user_name != user_information["user_name"] and user_password == user_information["user_password"]):
            print("Kullanıcı adınız hatalıdır. Lütfen yeniden deneyiniz!")

        elif (user_name == user_information["user_name"] and user_password != user_information["user_password"]):
            print("Parolanız hatalıdır. Lütfen yeniden deneyiniz!")

        elif (user_name != user_information["user_name"] and user_password != user_information["user_password"]):
            print("Kullanıcı adınız ve parolanız hatalıdır. Lütfen yeniden deneyiniz!")

        else:
            print("Tebrikler, Başarıyla giriş yaptınız!")
            break

    ##=> Kayıt Olma
    elif status_query == "2":

        print("######################################################################")
        print("########################### KAYIT OLMA  ##############################")
        print("######################################################################")

        user_information["user_name"] = input("Kullanıcı Adı:")
        user_information["user_password"] = input("Kullanıcı Şifresi:")

        status_query = "1"

        print("Kayıt olma işlemi başarılı bir şekilde gerçekleşti! Giriş yapmak için kullanıcı bilgilerinizi yeniden giriniz:")

