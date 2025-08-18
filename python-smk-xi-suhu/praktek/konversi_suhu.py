# Praktik Konversi Suhu
def celcius_ke_fahrenheit(c):
    return (c * 9/5) + 32

def celcius_ke_kelvin(c):
    return c + 273.15

# Input suhu siswa
suhu_list = []
n = int(input("Jumlah pengukuran suhu: "))
for i in range(n):
    s = float(input(f"Suhu ke-{i+1} (Celcius): "))
    suhu_list.append(s)

print("\nHasil Konversi:")
for s in suhu_list:
    f = celcius_ke_fahrenheit(s)
    k = celcius_ke_kelvin(s)
    print(f"{s:.2f}C -> {f:.2f}F, {k:.2f}K")

# Statistik suhu
rata2 = sum(suhu_list)/len(suhu_list)
maks = max(suhu_list)
minim = min(suhu_list)
print(f"\nRata-rata suhu: {rata2:.2f}C")
print(f"Suhu maksimum: {maks:.2f}C")
print(f"Suhu minimum: {minim:.2f}C")
