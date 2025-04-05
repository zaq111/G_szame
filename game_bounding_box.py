import cv2
import numpy as np
import mss
import time

# Fungsi untuk mencari gambar pada layar
def find_image_on_screen(template_path):
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Ambil monitor pertama (sesuaikan jika perlu)
        screenshot = sct.grab(monitor)

    # Konversi screenshot ke format numpy array untuk diproses oleh OpenCV
    img = np.array(screenshot)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    # Load template gambar (boss_button.png)
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    # Ubah screenshot ke grayscale untuk pencocokan template
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Temukan lokasi gambar di layar
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)

    # Ambil lokasi threshold yang cocok
    threshold = 0.8  # Sesuaikan threshold sesuai dengan kebutuhan
    locations = np.where(result >= threshold)

    # Gambar bounding box di setiap lokasi yang ditemukan
    for pt in zip(*locations[::-1]):  # zip locations, terbalikkan untuk (x, y) format
        cv2.rectangle(img, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0, 255, 0), 2)

    return img

# Fungsi untuk menampilkan gambar
def display_image_with_bounding_box(template_path):
    img_with_box = find_image_on_screen(template_path)

    # Tampilkan gambar dengan bounding box
    cv2.imshow('Bounding Box on Boss Button', img_with_box)

    # Tunggu sampai user menekan tombol
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Ganti dengan path ke gambar boss_button.png
    display_image_with_bounding_box("tier.png")
