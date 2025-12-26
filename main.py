import os
import cv2
import pandas as pd
import time
from qr_evaluator import QREvaluator

if __name__ == "__main__":
    # === CẤU HÌNH THƯ MỤC ===
    INPUT_FOLDER = r"C:\Users\Dung\Downloads\QR_only_dataset"  # Thư mục ảnh đầu vào
    GT_FOLDER = ""                                              # Nếu có ground truth thì điền đường dẫn
    OUTPUT_FOLDER = "ket_qua_xu_ly"                             # Thư mục lưu ảnh đã xử lý

    evaluator = QREvaluator()
    evaluator.run_full_experiment(INPUT_FOLDER, GT_FOLDER, OUTPUT_FOLDER)