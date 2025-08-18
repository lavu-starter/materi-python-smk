with open("nilai_siswa.txt", "w") as file:
    file.write("Ani:80\nBudi:90\nCici:85\n")
with open("nilai_siswa.txt", "r") as file:
    data = file.readlines()
print("Isi file:")
for line in data:
    print(line.strip())
with open("nilai_siswa.txt", "a") as file:
    file.write("Dedi:95\n")
