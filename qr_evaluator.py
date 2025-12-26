import cv2
from pyzbar.pyzbar import decode
from skimage.metrics import structural_similarity as ssim
import numpy as np
from .qr_processor import QRProcessor  # Import từ file cùng thư mục

class QREvaluator:
    def __init__(self):
        self.processor = QRProcessor()

    def decode_qr(self, image):
        """Giải mã QR bằng pyzbar (ưu tiên) và OpenCV (dự phòng)."""
        try:
            decoded_objects = decode(image)
            if decoded_objects:
                return decoded_objects[0].data.decode('utf-8')
            
            detector = cv2.QRCodeDetector()
            data, _, _ = detector.detectAndDecode(image)
            if data:
                return data
            return None
        except Exception:
            return None

    def calculate_metrics(self, img_gt, img_processed):
        """Tính PSNR và SSIM so với ground truth."""
        if img_gt is None:
            return 0, 0
            
        if img_processed.shape != img_gt.shape:
            img_processed = cv2.resize(img_processed, (img_gt.shape[1], img_gt.shape[0]))
        
        mse = np.mean((img_gt - img_processed) ** 2)
        psnr = 100 if mse == 0 else 20 * np.log10(255.0 / np.sqrt(mse))
        score, _ = ssim(img_gt, img_processed, full=True)
        return psnr, score