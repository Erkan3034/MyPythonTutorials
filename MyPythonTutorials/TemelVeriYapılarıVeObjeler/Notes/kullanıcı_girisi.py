print("""

************************Kullanıcı Giriş Sistemi **********************
""")

username = "Erkan"  # User Name
user_password = "12052024"  # Password
entrance_right = 4  # Entrance right check

while True:
    user_name_input = input("Kullanıcı adı :")
    user_psw_input = input("Parola :")

    if (user_name_input == username and user_password != user_psw_input):
        print("Parola hatalı!")
        entrance_right -= 1
    elif (user_name_input != username and user_password == user_psw_input):
        print("Kullanıcı adı hatalı!")
        entrance_right -= 1
    elif (user_name_input != username and user_password != user_psw_input):
        print("Kullanıcı adı ve Parola hatalı!")
        entrance_right -= 1
    else:
        print("Sisteme başarılı bir şekilde giriş yapıldı.")
        break  # if conditional is True, break running
    if (entrance_right == 0):
        print("Giriş hakkı bitti, Güvenliğiniz için 1 saat sonra yeniden deneyiniz.")
        break
