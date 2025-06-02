# Version 3.5 - Auto Click Boss Menu with Image Recognition
# Author: ChatGPT
# Date: 2025-04-04
# Description: Skrip ini membuka menu Boss, menjalankan 3 fase klik, dan menunggu setiap ref.png hilang sebelum lanjut.

import cv2
import numpy as np
import pyautogui
import subprocess
import time
capture_counter = 1  # Nomor urut untuk gambar yang disimpan
click_counter = 1 
#ADB_PATH = r"C:\Users\sin19\Downloads\platform-tools-latest-windows\platform-tools\adb.exe"
ADB_PATH = r"C:\ADB\platform-tools\adb.exe"
DEVICE_ID = "emulator-5554"  # Pastikan ID ini benar

PHASES = [
    (863, 672),
    (840, 804),
    (849, 895)
]
MAP_CLICK = (1701, 123)
REF_IMAGE = "ref.png"
BOSS_MENU_IMAGE = "boss_button.png"
FINAL_BOSS_CLICK = (529, 857)
CLOSE_BOSS_MENU = (1487, 885)

SWIPE_START = (512, 861)
SWIPE_END = (486, 404)
SWIPE_COUNT = 2

LEVEL_BOSS = (457, 210)
SUB_BOSS_COORDINATE = (1730, 220)  # Mengganti klik berdasarkan koordinat

def capture_bounding_box(template_path, positions):
    global capture_counter
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    
    for pos in positions:
        x, y = pos
        h, w = 40, 40  # Ukuran bounding box (bisa disesuaikan)

        # Gambar bounding box merah
        cv2.rectangle(screenshot, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    filename = f"capture_{capture_counter}.png"
    cv2.imwrite(filename, cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR))
    print(f"📸 Capture {capture_counter} disimpan: {filename}")
    capture_counter += 1

def adb_tap(x, y):
    print(f"Klik pada ({x}, {y})")
    subprocess.run([ADB_PATH, "-s", DEVICE_ID, "shell", "input", "tap", str(x), str(y)])
    time.sleep(1.5)

def adb_swipe(x1, y1, x2, y2):
    print(f"Swipe dari ({x1}, {y1}) ke ({x2}, {y2})")
    subprocess.run([ADB_PATH, "-s", DEVICE_ID, "shell", "input", "swipe", str(x1), str(y1), str(x2), str(y2), "500"])
    time.sleep(1.5)

def find_all_images_on_screen(template_path, threshold=0.8):
    screenshot = pyautogui.screenshot()
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
    template = cv2.imread(template_path, 0)
    
    if template is None:
        print(f"Gambar {template_path} tidak ditemukan!")
        return []
    
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    
    h, w = template.shape[:2]
    positions = [(pt[0] + w//2, pt[1] + h//2) for pt in zip(*loc[::-1])]
    
    if positions:
        print(f"Gambar {template_path} ditemukan di {positions}")
    return positions



# def wait_for_image_change_at_position(template_path, pos):
#     """Menunggu hingga gambar di posisi tertentu hilang (boss mati) sebelum pindah lokasi."""
#     while True:
#         current_positions = find_all_images_on_screen(template_path)

#         # Jika posisi gambar masih ada, berarti boss belum mati
#         if pos in current_positions:
#             print(f"Boss belum mati di {pos}, menunggu 10 detik sebelum cek ulang...")
#             time.sleep(10)  # Tunggu sebelum mengecek ulang
#             continue  # Ulangi cek lagi

#         # Jika gambar sudah hilang, berarti boss mati, lanjut ke koordinat berikutnya
#         print(f"Boss mati di {pos}, lanjut ke koordinat berikutnya...")
#         return True  

def wait_for_image_change_at_position(template_path, pos, timeout=120):
    """Menunggu hingga gambar di posisi tertentu hilang (boss mati), maksimal timeout detik."""
    start_time = time.time()

    while True:
        current_positions = find_all_images_on_screen(template_path)

        if pos in current_positions:
            elapsed = time.time() - start_time
            if elapsed > timeout:
                print(f"⏰ Timeout: Boss di {pos} tidak mati setelah {timeout} detik. Lewatkan boss ini.")
                return False  # Kasus gagal
            print(f"{elapsed} - Boss belum mati di {pos}, menunggu 10 detik sebelum cek ulang...")
            time.sleep(10)
        else:
            print(f"✅ Boss mati di {pos}, lanjut ke koordinat berikutnya...")
            return True



def open_boss_menu(i):
    while True:
        boss_pos = find_all_images_on_screen(BOSS_MENU_IMAGE)
        if boss_pos:
            adb_tap(*boss_pos[0])
            if wait_for_image_change_at_position(BOSS_MENU_IMAGE, boss_pos[0]):
                time.sleep(1.5)
                adb_tap(*SUB_BOSS_COORDINATE)  # Menggunakan koordinat tetap
                print(f"[{i}] - klik SUB BOSS")
                time.sleep(1.5)
                adb_tap(*LEVEL_BOSS)
                time.sleep(1.5)
                if wait_for_image_change_at_position(BOSS_MENU_IMAGE, boss_pos[0]):
                    for _ in range(SWIPE_COUNT):
                        adb_swipe(*SWIPE_START, *SWIPE_END)
                    
                    time.sleep(0.5)
                    final_click_adjusted = (FINAL_BOSS_CLICK[0], FINAL_BOSS_CLICK[1] - (130 * i))
                    adb_tap(*final_click_adjusted)
                    return True
        print("Menunggu tombol boss_button muncul...")
        time.sleep(1)
        
def capture_screen_with_bbox(template_path, pos, adjusted_pos, counter):
    """Mengambil screenshot dan menandai area yang diperiksa dengan bounding box."""
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # Konversi ke format OpenCV

    # Gambar bounding box di pos utama
    cv2.rectangle(screenshot, (pos[0], pos[1]), (pos[0] + 50, pos[1] + 50), (0, 255, 0), 2)
    cv2.putText(screenshot, f"Pos {counter}", (pos[0], pos[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Gambar bounding box di adjusted_pos
    cv2.rectangle(screenshot, (adjusted_pos[0], adjusted_pos[1]), (adjusted_pos[0] + 50, adjusted_pos[1] + 50), (0, 0, 255), 2)
    cv2.putText(screenshot, f"Adj {counter}", (adjusted_pos[0], adjusted_pos[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Simpan gambar
    filename = f"capture_{counter}.png"
    cv2.imwrite(filename, screenshot)
    print(f"Screenshot disimpan sebagai {filename}")

def capture_click_position(ref_pos, adjusted_pos, counter):
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # Kotak hijau: posisi ref.png
    cv2.rectangle(screenshot, (ref_pos[0]-20, ref_pos[1]-20), (ref_pos[0]+20, ref_pos[1]+20), (0, 255, 0), 2)
    cv2.putText(screenshot, "ref.png", (ref_pos[0]-20, ref_pos[1]-25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    # Kotak merah: posisi klik offset
    cv2.rectangle(screenshot, (adjusted_pos[0]-20, adjusted_pos[1]-20), (adjusted_pos[0]+20, adjusted_pos[1]+20), (0, 0, 255), 2)
    cv2.putText(screenshot, "click", (adjusted_pos[0]-20, adjusted_pos[1]-25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

    filename = f"click_{counter}.png"
    cv2.imwrite(filename, screenshot)
    print(f"📸 Posisi klik disimpan di: {filename}")


# def process_phase():
#     for phase in PHASES:
#         if not open_boss_menu():
#             print("Gagal membuka menu boss, mencoba lagi...")
#             continue
        
#         print(f"Menjalankan fase pada {phase}")
#         adb_tap(*phase)
#         time.sleep(1.5)
#         adb_tap(*MAP_CLICK)
#         time.sleep(1.5)
#         while True:
#             ref_positions = find_all_images_on_screen(REF_IMAGE)
#             if not ref_positions:
#                 print("Semua ref.png sudah hilang, lanjut ke fase berikutnya.")
#                 return_button_pos = find_all_images_on_screen("return_city.png")
#                 if return_button_pos:
#                     #adb_tap(return_button_pos[0], return_button_pos[1])
#                     adb_tap(*return_button_pos[0]) 
#                     print("Klik return_city.png berhasil.")
#                 else:
#                     print("⚠️ Gambar return_city.png tidak ditemukan. Tidak bisa kembali ke kota.")
#                 #adb_tap(*CLOSE_BOSS_MENU)
#                 time.sleep(2)
#                 break
            
#             print(f"Ditemukan {len(ref_positions)} ref.png: {ref_positions}")
#             # for ref_pos in ref_positions:
#             #     adjusted_pos = (ref_pos[0], ref_pos[1] + 33)  # Tambah offset ke bawah
#             #     adb_tap(*adjusted_pos)  # Klik pada titik baru
#             #     time.sleep(1)  # Beri jeda sebelum cek ulang
#             #     wait_for_image_change_at_position(REF_IMAGE, ref_pos)
#             global click_counter
#             for ref_pos in ref_positions:
#                 adjusted_pos = (ref_pos[0], ref_pos[1] + 33)
    
#                 # Ambil screenshot posisi klik
#                 capture_click_position(ref_pos, adjusted_pos, click_counter)
#                 click_counter += 1

#                 adb_tap(*adjusted_pos)
#                 time.sleep(1)
#                 wait_for_image_change_at_position(REF_IMAGE, ref_pos)
# def process_phase():
#     for i in range(4):  # Ulangi 4 kali dengan offset klik MAP_CLICK
        
#         print(f"\n📍 Pengulangan ke-{i+1}")

#         # if not open_boss_menu(i):
#         #     print(f"[{i}] - Gagal membuka menu boss, mencoba lagi...")
#         #     continue
#         while not open_boss_menu(i):
#             print(f"[{i}] - Gagal membuka menu boss, mencoba lagi...")
#             time.sleep(1.5)  # beri jeda biar ga terlalu cepat loop-nya

#         print(f"[{i}] - ✅ Berhasil buka boss menu!")

#         for phase in PHASES:
#             print(f"Menjalankan fase pada {phase}")
#             adb_tap(*phase)
#             time.sleep(1.5)
#             adb_tap(*MAP_CLICK)  # Pakai posisi MAP_CLICK yang digeser
#             time.sleep(1.5)

#             while True:
#                 ref_positions = find_all_images_on_screen(REF_IMAGE)
#                 if not ref_positions:
#                     print("Semua ref.png sudah hilang, lanjut ke fase berikutnya.")
#                     return_button_pos = find_all_images_on_screen("return_city.png")
#                     if return_button_pos:
#                         adb_tap(*return_button_pos[0])
#                         print("Klik return_city.png berhasil.")
#                     else:
#                         print("⚠️ Gambar return_city.png tidak ditemukan. Tidak bisa kembali ke kota.")
#                     time.sleep(2)
#                     break

#                 print(f"Ditemukan {len(ref_positions)} ref.png: {ref_positions}")
#                 global click_counter
#                 for ref_pos in ref_positions:
#                     adjusted_pos = (ref_pos[0], ref_pos[1] + 33)
#                     capture_click_position(ref_pos, adjusted_pos, click_counter)
#                     click_counter += 1
#                     adb_tap(*adjusted_pos)
#                     time.sleep(1)
#                     wait_for_image_change_at_position(REF_IMAGE, ref_pos)

def process_phase():
    for i in range(4):  # Ulangi 4 kali dengan offset klik MAP_CLICK
        print(f"\n📍 Pengulangan ke-{i+1}")

        while not open_boss_menu(i):
            print(f"[{i}] - Gagal membuka menu boss, mencoba lagi...")
            time.sleep(1.5)

        print(f"[{i}] - ✅ Berhasil buka boss menu!")

        for phase_index, phase in enumerate(PHASES):
            print(f"Menjalankan fase ke-{phase_index + 1} pada {phase}")
            adb_tap(*phase)
            time.sleep(1.5)
            adb_tap(*MAP_CLICK)
            time.sleep(1.5)

            while True:
                ref_positions = find_all_images_on_screen(REF_IMAGE)
                if not ref_positions:
                    print("✅ Semua ref.png sudah hilang, kembali ke kota.")
                    return_button_pos = find_all_images_on_screen("return_city.png")
                    if return_button_pos:
                        adb_tap(*return_button_pos[0])
                        print("🏙️ Klik return_city.png berhasil.")
                    else:
                        print("⚠️ Gambar return_city.png tidak ditemukan.")
                    time.sleep(2)

                    # ✅ Buka ulang boss menu untuk phase selanjutnya, kecuali setelah fase terakhir
                    if phase_index < len(PHASES) - 1:
                        print(f"🔁 Membuka kembali menu Boss untuk fase ke-{phase_index + 2}...")
                        while not open_boss_menu(i):
                            print(f"[{i}] - Gagal membuka ulang menu boss, coba lagi...")
                            time.sleep(1.5)

                    break  # lanjut ke fase berikutnya

                print(f"Ditemukan {len(ref_positions)} ref.png: {ref_positions}")
                global click_counter
                for ref_pos in ref_positions:
                    adjusted_pos = (ref_pos[0], ref_pos[1] + 33)
                    capture_click_position(ref_pos, adjusted_pos, click_counter)
                    click_counter += 1
                    adb_tap(*adjusted_pos)
                    time.sleep(1)
                    wait_for_image_change_at_position(REF_IMAGE, ref_pos)

if __name__ == "__main__":
    process_phase()
    print("Semua fase selesai!")
