import subprocess
import random
import time
import pyautogui
import numpy as np
import cv2

ADB_PATH = r"C:\ADB\platform-tools\adb.exe"
DEVICE_ID = "emulator-5554"
PACKAGE_NAME = "com.ncvgames.lineage2msa"
PREF_FILE = f"/data/data/{PACKAGE_NAME}/shared_prefs/ncmop.preferences.xml"
image_dir = r"C:\Users\Administrator\source\repos\zaq111\Game"
nama1 = r"C:\Users\Administrator\source\repos\zaq111\Game\nama1.txt"
nama2 = r"C:\Users\Administrator\source\repos\zaq111\Game\nama2.txt"

def adb_command(command, use_su=False):
    if use_su:
        # Kutip tunggal luar, kutip ganda dalam
        full_cmd = f'"{ADB_PATH}" -s {DEVICE_ID} shell su -c \'"{command}"\''
    else:
        full_cmd = f'"{ADB_PATH}" -s {DEVICE_ID} shell "{command}"'
    try:
        result = subprocess.check_output(full_cmd, shell=True, stderr=subprocess.STDOUT)
        return result.decode().strip()
    except subprocess.CalledProcessError:
        return None

def adb_tap(x, y):
    """Kirim input tap ke emulator via ADB."""
    subprocess.run(f'"{ADB_PATH}" -s {DEVICE_ID} shell input tap {x} {y}', shell=True)

def is_app_running():
    result = adb_command(f"pidof {PACKAGE_NAME}")
    return bool(result)

def preferences_file_exists():
    result = adb_command(f'ls "{PREF_FILE}"', use_su=True)
    return bool(result)

def rename_preferences_file():
    random_number = random.randint(100000, 999999)
    new_name = f"/data/data/{PACKAGE_NAME}/shared_prefs/ncmop.preferences_{random_number}.xml"
    mv_command = f"mv {PREF_FILE} {new_name}"
    result = adb_command(mv_command, use_su=True)
    if result is not None:
        print(f"✅ File berhasil di-rename ke: {new_name}")
    else:
        print("❌ Gagal rename file (mungkin tidak ada atau permission ditolak).")

def adb_screenshot():
    result = subprocess.run(
        [f"{ADB_PATH}", "exec-out", "screencap", "-p"],
        stdout=subprocess.PIPE
    )
    img_array = np.frombuffer(result.stdout, np.uint8)
    screenshot = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return screenshot



def find_template_on_screen(template_path, threshold=0.75):
    screen = adb_screenshot()
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_path, 0)
    if template is None:
        print(f"❌ Template {template_path} tidak ditemukan.")
        return None
    result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        h, w = template.shape
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        #print(f"✅ {template_path} ditemukan di ({center_x}, {center_y}) dengan confidence {max_val:.2f}")
        return (center_x, center_y)
    return None


def wait_and_tap_image(image_path, delay=1, max_wait=15):
    for _ in range(max_wait):
        pos = find_template_on_screen(image_path)
        if pos:
            adb_tap(*pos)
            return True
        time.sleep(delay)
    print(f"❌ {image_path} tidak ditemukan dalam {max_wait * delay} detik.")
    return False

def get_random_name(file1, file2):
    try:
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
            list1 = [line.strip() for line in f1 if line.strip()]
            list2 = [line.strip() for line in f2 if line.strip()]
    except FileNotFoundError as e:
        print(f"❌ File tidak ditemukan: {e}")
        return None

    if not list1 or not list2:
        print("❌ Salah satu file kosong.")
        return None

    return f"{random.choice(list1)}{random.choice(list2)}"

def launch_app():
    launch_cmd = f"monkey -p {PACKAGE_NAME} -c android.intent.category.LAUNCHER 1"
    result = adb_command(launch_cmd)
    if result is not None:
        print("🚀 Aplikasi berhasil dijalankan.")
    else:
        print("❌ Gagal menjalankan aplikasi.")

    print("⌛ Menunggu game loading dan masuk ke halaman awal...")
    time.sleep(5)
    # Langkah 1: Tap di posisi (300, 300) sampai guest.png muncul
    #print("🔄 Tap (1000, 1000) sampai muncul guest.png...")

    #
    # 1. TUNGGU guest.png
    #
    for _ in range(50):  # max 90 detik
        #print("🔄 Tunggu")
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\guest.png")
        if pos:
            print("🔄 Tap Guest")
            adb_tap(*pos)
            break
        #print("🔄 Tap Continue")
        #adb_tap(300, 300)
        time.sleep(1) #def 3 ---------------------------------------------------------------------------------------
    else:
        print("❌ guest.png tidak ditemukan.")
        subprocess.run(f'{ADB_PATH} shell am force-stop {PACKAGE_NAME}', shell=True)
        return

    for _ in range(30):  # max 90 detik
        #print("🔄 Tunggu")
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\lokasi.png")
        if pos:
            time.sleep(0.8)
            print("🔄 Tap Lokasi")
            adb_tap(*pos)
            break
        time.sleep(1) #def 2 ---------------------------------------------------------------------------------------
    else:
        print("❌ lokasi.png tidak ditemukan.")
        return

    for _ in range(10):  # max 90 detik
        #print("🔄 Tunggu")
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\lokasi_indo.png")
        if pos:
            time.sleep(0.8)
            print("🔄 Tap Lokasi Indo")
            adb_tap(*pos)
            break
        time.sleep(1.5)
    else:
        print("❌ lokasi_indo.png tidak ditemukan.")
        adb_tap(1000,25)
        print("🔄 manual tap lokasi.")
        return
    
    #
    # 2. Centang TOS
    #

    for _ in range(10):  # max 90 detik
        #print("🔄 Tunggu")
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\centang.png")
        if pos:
            print("🔄 Tap TOS")
            adb_tap(*pos)
            break
        time.sleep(1) #def 2 ---------------------------------------------------------------------------------------
    else:
        print("❌ centang.png tidak ditemukan.")
        return

    for _ in range(30):  # max 90 detik
        #print("🔄 Tunggu")
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\confirm.png")
        if pos:
            print("🔄 Tap Confirm")
            adb_tap(*pos)
            break
        time.sleep(1) #def 2 ---------------------------------------------------------------------------------------
    else:
        print("❌ confirm.png tidak ditemukan.")
        return

    for _ in range(30):  # max 90 detik
        #print("🔄 Tunggu")
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\start.png")
        if pos:
            print("🔄 Tap Start")
            adb_tap(*pos)
            break
        time.sleep(2)
    else:
        print("❌ start.png tidak ditemukan.")
        return
    #
    #
    #
    for _ in range(20):  # max 40 detik
        # pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\recomended.png")
        print("🖱️ Pencarian Server Leona5")
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\leona05.png")
        if pos:
            print("🖱️ Lanjut ke Pemilihan Server")
            adb_tap(*pos)
            # lanjut ke langkah berikutnya
            break
        else:
            #print("✅ Gambar talking isle Belum Muncul, SKIP")
            print("🖱️ Sewrver belum ketemu, berarti klik select server")
            pos2 = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\select_server.png")
            if pos2:
                #print("🖱️ Tap 'select_server.png'")
                adb_tap(*pos2)
            time.sleep(2) #def 2 ---------------------------------------------------------------------------------------
   

    # for _ in range(30):  # max 90 detik
    #     print("🔄 Pilih Server")
    #     pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\leona04.png")
    #     if pos:
    #         print("🔄 Tap Leona04")
    #         adb_tap(*pos)
    #         break
    #     time.sleep(2)
    # else:
    #     print("❌ leona03.png tidak ditemukan.")
    #     return


    #masuk ke Game
    for _ in range(30):  # max 90 detik
        print("🔄 Menunggu Enter Game")
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\enter_game.png")
        if pos:
            print("🔄 Tap Enter Game")
            adb_tap(*pos)
            break
        time.sleep(2)
    else:
        print("❌ enter_game.png tidak ditemukan.")
        return


    pos_captcha = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\please.png")
    if pos_captcha:
        print("🔒 Captcha terdeteksi. Mohon input manual.")
    
        # Fokus ke emulator agar user bisa langsung mengetik
        adb_tap(*pos_captcha)  # klik area captcha untuk aktifkan input

        # Minta input dari user
        captcha_text = input("Ketik isi captcha (manual): ").strip()

        # Kirim input via ADB (misalnya emulator langsung menerima input keyboard)
        subprocess.run(f'{ADB_PATH} shell input text "{captcha_text}"', shell=True)
        pos_confirm = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\capcha.png")
        if pos_confirm:
            adb_tap(*pos_confirm)
        
        print("✅ Captcha diinput. Melanjutkan...")
    # while True:
    #     print("✅ Mencari Captcha2 ")
    #     pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\cancel_dicapcha.png")
    #     print("✅ Captcha2 di cek")
    #     if pos:
    #         print("✅ Cancel Ketemu")
    #         while True:
    #             print("✅ Masuk While")
    #             pos_captcha = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\please.png")
    #             if not pos_captcha:
    #                 print("✅ Captcha sudah hilang. Melanjutkan...")
    #                 break  # Captcha selesai
    #             else:
    #                 print("🔒 Captcha terdeteksi. Mohon input manual.")

    #                 adb_tap(*pos_captcha)  # Fokuskan input ke captcha

    #                 captcha_text = input("Ketik isi captcha (manual): ").strip()
    #                 subprocess.run(f'{ADB_PATH} shell input text "{captcha_text}"', shell=True)
    #                 pos_confirm = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\capcha.png")
    #                 if pos_confirm:
    #                     adb_tap(*pos_confirm)
    #                 time.sleep(2)

    #                 # Coba klik confirm jika ada
    #                 pos_confirm = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\confirm2.png")
    #                 if pos_confirm:
    #                     adb_tap(*pos_confirm)
    #                     time.sleep(2)

    #                 print("⏳ Menunggu captcha validasi...")
    #         break
    #     else:
    #         time.sleep(2)
    #         print("✅ Ulangi")



    #
    # 3. Pemilihan Karakter, klo 
    #

    for _ in range(30):  # max 90 detik
        print("🔄 Menunggu Menu Pemilihan Karakter")
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\dark_elf.png")
        if pos:
            print("🔄 Tap Dark Elf")
            adb_tap(*pos)
            break
        time.sleep(1) #def 2 ---------------------------------------------------------------------------------------
    else:
        print("❌ Menu Karakter tidak Muncul, kemungkinan server full.")
        subprocess.run(f'{ADB_PATH} shell am force-stop {PACKAGE_NAME}', shell=True)
        
        return
    
    for _ in range(30):  # max 90 detik
        print("🔄 Pilih Dark Elf - Archer")
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\archer.png")
        if pos:
            print("🔄 Tap Archer logo")
            adb_tap(*pos)
            break
        time.sleep(2)
    else:
        print("❌ archer.png tidak ditemukan.")
        return


    #
    # 4. Pembuatan Karakter
    #

    for _ in range(30):  # max 90 detik
        print("🔄 Wait Select")
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\select.png")
        if pos:
            print("🔄 Tap Select")
            adb_tap(*pos)
            break
        time.sleep(2)
    else:
        print("❌ select.png tidak ditemukan.")
        return

    #
    # 5. Pembuatan Nama
    #
    
    for _ in range(30):  # max 90 detik
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\klik_nama.png")
        if pos:
            print("🔄 Tap Select")
            time.sleep(2)
            adb_tap(*pos)
            time.sleep(2)
            #random_name = get_random_name("nama1.txt", "nama2.txt")
            random_name = get_random_name(nama1, nama2)
            if random_name:
                print(f"✅ Nama acak yang dipilih: {random_name}")
                subprocess.run(f'{ADB_PATH} shell input text "{random_name}"', shell=True)
                time.sleep(2)
                break
            time.sleep(2)  

    for _ in range(20):  # max 90 detik
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\confirm2.png")
        if pos:
            print("🔄 Tap Confirm")
            adb_tap(*pos)
            break
        time.sleep(2)

    for _ in range(20):  # max 90 detik
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\create.png")
        if pos:
            print("🔄 Tap Create")
            adb_tap(*pos)
            break
        time.sleep(2)


    #
    # 5. Menunggu gambar leah yaitu setelah masuk ke game
    #

    #############################################################################################################################################
    for _ in range(30):  # max 40 detik
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\leah.png")
        if pos:
            print("✅ Gambar 'leah.png' ditemukan, lanjut ke langkah berikutnya.")
            time.sleep(2)
            adb_tap(1250,118)
            break
        else:
            print("✅ SKIP VIDEO")
            adb_tap(1440,135)
            time.sleep(2)
        for _ in range(30):
            pos_skip = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\skip.png")
            if pos_skip:
                print("🔄 Try Skip")
                adb_tap(*pos_skip)
                break
    


    for _ in range(20):  # max 90 detik
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\accept.png")
        if pos:
            print("🔄 Tap Accept")
            adb_tap(*pos)
            break
        time.sleep(2)
    
    for _ in range(20):  # max 90 detik
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\skip.png")
        if pos:
            print("🔄 Tap Skip")
            adb_tap(*pos)
            break
        time.sleep(2)
    
    #
    # 6. Proses Mail
    #

    for _ in range(20):  # max 40 detik
        pos = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\mail.png")
        if pos:
            print("✅ Gambar 'mail.png' ditemukan, lanjut ke langkah berikutnya.")
            adb_tap(*pos)
            time.sleep(2)
            #adb_tap(1300,510) #mail
            time.sleep(2)
            adb_tap(1500,800) #claim_all
            time.sleep(2)
            adb_tap(1550,23) #keluar mail
            time.sleep(2)
            adb_tap(1250,20) #bag
            for _ in range(20):
                pos_agi = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\agi.png")
                if pos_agi:
                    adb_tap(*pos_agi)
                    adb_tap(*pos_agi)
                    time.sleep(2)
                    for _ in range(20):
                        pos_see_all =  find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\see_all.png")
                        if pos_see_all:
                            adb_tap(*pos_see_all)  
                            time.sleep(2)
                            adb_tap(900,800)
                            break
                        pos_skip_to_result =  find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\skip_to_result.png")
                        if pos_skip_to_result:
                            adb_tap(*pos_skip_to_result)
                            while True:
                                jawaban = input("Lanjutkan? (y/n): ").strip().lower()
                                if jawaban in ['y', 'n']:
                                    break
                            break
                        
                    #break
            #break
        else:
            print("🔄 Gambar belum ditemukan, tekan ~")
            #subprocess.run(f'{ADB_PATH} shell input text "~"', shell=True)
            adb_tap(1500,20)

            time.sleep(2)
            
    for _ in range(20):  # max 40 detik
        pos_hero = find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\hero_class.png")
        if pos_hero:
            adb_tap(*pos_hero)
            adb_tap(*pos_hero)
            time.sleep(2)
            for _ in range(20):
                pos_see_all =  find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\see_all.png")
                if pos_see_all:
                    adb_tap(*pos_see_all)   
                    break
                pos_skip_to_result =  find_template_on_screen(r"C:\Users\Administrator\source\repos\zaq111\Game\skip_to_result.png")
                if pos_skip_to_result:
                    adb_tap(*pos_skip_to_result)
                    while True:
                        jawaban = input("Lanjutkan? (y/n): ").strip().lower()
                        if jawaban in ['y', 'n']:
                            break
                    break

    print("✅ Proses awal selesai. Siap lanjut ke fase berikutnya.")





if __name__ == "__main__":
    print("🔁 Memulai loop pengecekan setiap 5 detik...\n")
    while True:
        if not is_app_running():
            print("🛑 Aplikasi tidak berjalan.")
            
            if preferences_file_exists():
                print("🗂️ File preferences ditemukan. Melakukan rename...")
                rename_preferences_file()
            else:
                print("❌ File preferences tidak ditemukan. Lewati rename.")

            print("🚀 Menjalankan aplikasi...")
            launch_app()
        else:
            print("✅ Aplikasi sedang berjalan. Tidak melakukan apa-apa.")
        
        time.sleep(5)  # Delay 5 detik

