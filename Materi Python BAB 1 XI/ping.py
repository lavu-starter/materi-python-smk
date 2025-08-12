import os

target = "google.com"
response = os.system(f"ping -n 1 {target}")  # Windows
# response = os.system(f"ping -c 1 {target}")  # Linux/Mac

if response == 0:
    print(f"{target} dapat dihubungi.")
else:
    print(f"{target} tidak dapat dihubungi.")
