#Buat program yang meminta input password dari pengguna, dan akan terus meminta sampai password benar ("python123"). Gunakan while.

password_benar = "python123"
password = ""

while password != password_benar:
    password = input("Masukkan password: ")
    if password != password_benar:
        print("Password nya salah bang, coba lagi!")
print("Nice password, okaeri")