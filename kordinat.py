import pyautogui
import time

print("Arahkan mouse ke posisi yang diinginkan, koordinat akan muncul setiap 0.5 detik.")
print("Tekan Ctrl + C untuk keluar.\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Koordinat Mouse: ({x}, {y})", end="\r")  # Menampilkan di baris yang sama
        time.sleep(0.5)  # Update setiap 0.5 detik
except KeyboardInterrupt:
    print("\nProgram dihentikan.")
