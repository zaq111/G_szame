import subprocess
import numpy as np
import cv2
import time

def adb_screenshot():
    result = subprocess.run(
        ["adb", "exec-out", "screencap", "-p"],
        stdout=subprocess.PIPE
    )
    img_array = np.frombuffer(result.stdout, np.uint8)
    screenshot = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return screenshot
##
def find_template_on_screen(template_path, threshold=0.8):
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
        print(f"✅ {template_path} ditemukan di ({center_x}, {center_y}) dengan confidence {max_val:.2f}")
        return (center_x, center_y)
    return None

def adb_tap(x, y):
    subprocess.run(["adb", "shell", "input", "tap", str(x), str(y)])

def wait_and_tap_image(image_path, delay=1, max_wait=15):
    for _ in range(max_wait):
        pos = find_template_on_screen(image_path)
        if pos:
            adb_tap(*pos)
            return True
        time.sleep(delay)
    print(f"❌ {image_path} tidak ditemukan dalam {max_wait * delay} detik.")
    return False

def launch_app():
    print("🔄 Tap (300,300) setiap 3 detik sampai muncul guest.png...")
    for _ in range(30):  # max 90 detik
        pos = find_template_on_screen("guest.png")
        if pos:
            adb_tap(*pos)
            break
        adb_tap(300, 300)
        time.sleep(3)
    else:
        print("❌ guest.png tidak ditemukan.")
        return

    print("🧭 Menunggu lokasi.png...")
    if not wait_and_tap_image("lokasi.png"):
        return

    print("🗺️ Menunggu lokasi_indo.png...")
    if not wait_and_tap_image("lokasi_indo.png"):
        return

    time.sleep(3)

    print("✅ Menunggu centang.png...")
    if not wait_and_tap_image("centang.png"):
        return

    time.sleep(2)

    print("🔒 Menunggu confirm.png...")
    if not wait_and_tap_image("confirm.png"):
        return

    print("🎉 Launch berhasil!")

# Panggil fungsi
launch_app()
