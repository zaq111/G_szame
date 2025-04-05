import cv2
import numpy as np
import pyautogui
import time

REF_IMAGE = "ref.png"

def find_and_show_ref_images(template_path, threshold=0.7):
    """Menemukan dan menampilkan lokasi ref.png di layar LDPlayer secara realtime."""
    while True:
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)
        
        template = cv2.imread(template_path, 0)
        if template is None:
            print(f"Gambar {template_path} tidak ditemukan!")
            return

        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        positions = list(zip(*loc[::-1]))

        if positions:
            print(f"Ditemukan {len(positions)} ref.png di {positions}")

            # Gambar bounding box di sekitar ref.png
            h, w = template.shape
            for pos in positions:
                cv2.rectangle(screenshot_np, pos, (pos[0] + w, pos[1] + h), (0, 255, 0), 2)

            # Simpan hasil deteksi ke file
            cv2.imwrite("hasil_deteksi.png", cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB))

            # Tampilkan hasil deteksi secara realtime
            cv2.imshow("Deteksi ref.png (Realtime)", cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB))
        
        else:
            print("Tidak ada ref.png yang ditemukan!")
        
        # Tekan 'q' untuk keluar
        if cv2.waitKey(1000) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    find_and_show_ref_images(REF_IMAGE)
