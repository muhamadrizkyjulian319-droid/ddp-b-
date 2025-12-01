# 1.Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
# print(celcius_ke_fahrenheit(0))    # Output: 32.0
# print(celcius_ke_fahrenheit(100))  # Output: 212.0

def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))


# 2.Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
# print(is_genap(4))  # Output: True
# print(is_genap(7))  # Output: False

def is_genap(bilangan_bulat):
    if bilangan_bulat % 2 == 0:
        return True
    else:
        return False
    
print(is_genap(4))
print(is_genap(7))


# 3.Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
# nilai (80) #lulus
# nilai(60) #gagal

def nilai(ipk):
    if ipk >= 80:
        return "lulus"
    else:
        return "gagal"
    
print(nilai(80))
print(nilai(60))

#atau

def nilai(ipk):
    if ipk >= 80:
        print("lulus")
    else:
        print("gagal")
    
nilai(80)
nilai(60)


# 4.Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
# bilangan(20) # 1,3,5,7,9,11,13,15,17,19

def bilangan(bil):
    for i in range(1, bil):
        if i % 2 != 0:
            print(i)

bilangan(20)