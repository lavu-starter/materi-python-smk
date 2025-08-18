import math
import random
from datetime import datetime
import statistics
print("Pangkat 3^4:", math.pow(3,4))
print("Angka acak 1-100:", random.randint(1,100))
data = [80,90,70,85,95]
print("Rata-rata:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Modus:", statistics.mode(data))
print("Sekarang:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
