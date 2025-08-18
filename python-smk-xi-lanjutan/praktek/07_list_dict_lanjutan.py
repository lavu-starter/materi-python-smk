nilai = [70, 80, 90, 85]
nilai_kuadrat = [x**2 for x in nilai]
print("Nilai kuadrat:", nilai_kuadrat)
matrik = [[1,2],[3,4]]
print("Matrik[0][1]:", matrik[0][1])
siswa = {"nama":"Ani","umur":16,"nilai":[80,90,85]}
siswa["kelas"] = "XI"
del siswa["umur"]
for key, value in siswa.items():
    print(f"{key}: {value}")
