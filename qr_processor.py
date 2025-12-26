import cv2
import numpy as np

class QRProcessor:
    def __init__(self):
        pass

    def dynamic_illumination_equalization(self, img_gray):
        """[Chen 2023] Cân bằng sáng động sử dụng Morphological Closing."""
        kernel_size = 25
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        background = cv2.morphologyEx(img_gray, cv2.MORPH_CLOSE, kernel)
        
        img_float = img_gray.astype(np.float32)
        bg_float = background.astype(np.float32)
        bg_float[bg_float == 0] = 1
        
        result = cv2.divide(img_float, bg_float, scale=255)
        result = np.clip(result, 0, 255).astype(np.uint8)
        return result

    def apply_clahe(self, img_gray):
        """[Cao 2019] CLAHE tăng cường tương phản cục bộ."""
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        return clahe.apply(img_gray)

    def fusion_binarization(self, img_gray):
        """[Yao 2018] Nhị phân hóa lai giữa Otsu và Adaptive."""
        _, binary_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        binary_adaptive = cv2.adaptiveThreshold(
            img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 21, 10
        )
        fusion = cv2.bitwise_and(binary_otsu, binary_adaptive)
        return fusion

    def process_pipeline(self, image):
        """Pipeline xử lý tổng hợp."""
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        denoised = cv2.medianBlur(gray, 3)
        equalized = self.dynamic_illumination_equalization(denoised)
        enhanced = self.apply_clahe(equalized)
        binary = self.fusion_binarization(enhanced)
        return binary