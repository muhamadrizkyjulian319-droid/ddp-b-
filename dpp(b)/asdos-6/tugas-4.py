#Buat program yang meminta user memasukkan **5 nama teman**, lalu tampilkan seluruh nama yang sudah dimasukkan.
teman = []

for i in range(5):
    nama = input(f"Masukkan nama teman ke-{i+1}")
    teman.append(nama)

print("\nDaftar nama teman saya: ")
for nama in teman:
    print("-", nama)