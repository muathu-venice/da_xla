# Đồ Án Xử Lý Ảnh: Phát Hiện và Giải Mã QR Code Trong Điều Kiện Khó Khăn

**Môn học**: Xử Lý Ảnh  
**Nhóm sinh viên**:- Nguyễn Vũ Dũng
                   - Khuất Trung Hiếu
                   - Nguyễn Huy Hoàng
**Giảng viên hướng dẫn**: Đào Việt Cường 
**Năm học**: 2025-2026  

## Giới thiệu
Đồ án xây dựng một hệ thống hoàn chỉnh để phát hiện và giải mã QR code từ các ảnh thực tế trong điều kiện khó khăn như: ánh sáng không đều, nhiễu, góc chụp nghiêng, nền phức tạp, mờ, v.v.  
Hệ thống sử dụng các kỹ thuật xử lý ảnh nâng cao (dựa trên các nghiên cứu gần đây) kết hợp với thư viện pyzbar và OpenCV để đạt tỷ lệ nhận dạng cao.

## Các tính năng chính
- Tiền xử lý ảnh mạnh mẽ: cân bằng sáng động, tăng cường tương phản cục bộ, nhị phân hóa lai.
- Giải mã QR code bằng pyzbar (ưu tiên) và OpenCV (dự phòng).
- Đánh giá tự động trên hàng loạt ảnh: tính tỷ lệ thành công, thời gian xử lý, PSNR/SSIM (nếu có ground truth).
- Xuất báo cáo chi tiết dưới dạng file Excel.
- Lưu ảnh sau xử lý để phân tích.

## Cấu trúc projectda_xla/
```
da_xla/
├── qr_processor.py          # Module xử lý ảnh QR (pipeline tiền xử lý)
├── qr_evaluator.py          # Module giải mã và đánh giá hiệu suất
├── main.py                  # Chương trình chính - chạy thực nghiệm
├── Bài báo tham khảo/              # Thư mục chứa các bài báo/tài liệu tham khảo (PDF)
│   ├── Chen2023.pdf
│   ├── yao2018.pdf
│   ├── cao2019.pdf
│   └── hao2019.pdf
├── ket_qua_xu_ly/           # Thư mục tự động tạo - chứa ảnh đã xử lý
├── Bao_cao_ket_qua_QR.xlsx  # File báo cáo Excel (tự động sinh sau khi chạy)
├── anh_dau_vao/             # (Tùy chọn) Thư mục bạn copy ảnh cần test vào
└── README.md                # File hướng dẫn 
```



## Yêu cầu môi trường
- Python 3.8 trở lên
- Các thư viện:
opencv-python
numpy
pyzbar
scikit-image
pandas

Cài đặt nhanh:
pip install opencv-python numpy pyzbar scikit-image pandas

Cách sử dụng

Clone repository:

Bash
git clone https://github.com/muathu-venice/da_xla.git
cd da_xla

Chuẩn bị dữ liệu:
Tạo thư mục chứa ảnh QR cần xử lý (hoặc sửa đường dẫn trong main.py).
Ví dụ: sửa biến INPUT_FOLDER trong main.py thành đường dẫn thư mục chứa ảnh của bạn.

Chạy chương trình:

python main.py

Kết quả:
Ảnh sau xử lý được lưu trong thư mục ket_qua_xu_ly/
Báo cáo chi tiết: Bao_cao_ket_qua_QR.xlsx
Thông tin tổng kết (tỷ lệ thành công, thời gian trung bình) sẽ hiển thị trên terminal.


Bộ dữ liệu thực nghiệm

526 ảnh thực tế từ dataset công khai: Barcode & QR Codes trên Kaggle
600 ảnh synthetic do nhóm tự tạo thêm để đa dạng hóa điều kiện thử nghiệm.

Tài liệu tham khảo chính :

1. S. Yao et al., "Uneven illumination two-dimensional code image recognition algorithm research," IMCEC, 2018.
2. R. Chen et al., "A Fast Adaptive Binarization Method for QR Code Images Based on Dynamic Illumination Equalization," Electronics, 2023.
3. Z. Cao et al., "Robust Hazy QR Code Recognition based on Dehazing and Improved Adaptive Thresholding Method," IEEE CASE, 2019.
4. P. Hao et al., "Low-Light Image Enhancement Based On Retinex and Saliency Theories," IEEE, 2019.


