# 🔐 Chương Trình Mã Hóa Văn Bản

## Mô tả
Chương trình mã hóa văn bản hỗ trợ 4 loại mã hóa cổ điển:
- **Mã Caesar (Substitution)**: Dịch chuyển ký tự theo alphabet
- **Mã Affine**: Mã hóa tuyến tính với công thức E(x) = (ax + b) mod 26
- **Mã Vigenere**: Mã hóa đa khóa với từ khóa
- **Mã Hill**: Mã hóa ma trận với khóa là ma trận vuông

## Cách chạy chương trình

### Yêu cầu hệ thống
- Python 3.6+
- NumPy library

### Cài đặt dependencies
```bash
pip install numpy
```

### Chạy chương trình
```bash
python3 main.py
```

## Tính năng đặc biệt

### ✅ Xử lý ký tự đặc biệt
- **Bảo toàn ký tự đặc biệt**: Dấu chấm than (!), số (123), ký hiệu (@#$) được giữ nguyên
- **Bảo toàn định dạng**: Chữ hoa/thường được duy trì sau mã hóa/giải mã
- **Xử lý đúng**: Chỉ các chữ cái a-z, A-Z được mã hóa

### 🔄 Chương trình liên tục
- Menu hiển thị đầy đủ 4 loại mã hóa
- Người dùng có thể thực hiện nhiều phép mã hóa
- Thoát chương trình khi chọn option 0

### 🛡️ Xử lý lỗi
- Validation input cho từng loại mã hóa
- Thông báo lỗi rõ ràng và hướng dẫn sửa
- Xử lý các trường hợp ngoại lệ

## Hướng dẫn sử dụng từng loại mã hóa

### 1. Mã Caesar
- **Input**: Văn bản và độ dịch chuyển (0-25)
- **Example**: "Hello" với shift=3 → "Khoor"

### 2. Mã Affine  
- **Input**: Văn bản, tham số a (phải nguyên tố cùng nhau với 26), tham số b (0-25)
- **Valid a values**: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25
- **Example**: "Hello" với a=3, b=5 → "Armmv"

### 3. Mã Vigenere
- **Input**: Văn bản và từ khóa (chỉ chữ cái)
- **Example**: "Hello" với key="KEY" → "Rijvs"

### 4. Mã Hill
- **Input**: Văn bản và ma trận khóa 2x2 hoặc 3x3
- **Yêu cầu**: Ma trận phải khả nghịch (determinant nguyên tố cùng nhau với 26)
- **Example**: "Hello" với matrix [[3,2],[5,7]] → "Dldci"

## Test Cases

### Test với "Hello World! 123"
```
Caesar:   "Hello World! 123" → "Khoor Zruog! 123" → "Hello World! 123" ✅
Affine:   "Hello World! 123" → "Armmv Tvemo! 123" → "Hello World! 123" ✅  
Vigenere: "Hello World! 123" → "Rijvs Uyvjn! 123" → "Hello World! 123" ✅
Hill:     "Hello World! 123" → "Dldci Qyhny! 123" → "Hello World! 123" ✅
```

### Chạy test tự động
```bash
python3 test_encryption.py     # Test cơ bản
python3 sample_interaction.py  # Test demonstration  
python3 run_demo.py           # Test menu và UI
```

## Các vấn đề đã được sửa

### ❌ Vấn đề cũ:
1. Chương trình chỉ có mã Caesar và kết thúc sớm
2. Mã Hill mất ký tự đặc biệt và số
3. Thiếu các loại mã hóa Affine, Vigenere
4. Không có xử lý lỗi tốt

### ✅ Đã sửa:
1. **Menu đầy đủ**: Hiển thị cả 4 loại mã hóa, chạy liên tục
2. **Hill cipher hoàn hảo**: Bảo toàn ký tự đặc biệt và định dạng gốc  
3. **Đầy đủ 4 loại**: Caesar, Affine, Vigenere, Hill đều hoạt động
4. **Error handling**: Validation và thông báo lỗi chi tiết

## Structure

```
main.py                 # Chương trình chính
test_encryption.py      # Test cases tự động
sample_interaction.py   # Demo tương tác
run_demo.py            # Demo menu và UI
ENCRYPTION_README.md   # Hướng dẫn này
```

---
🎯 **Tất cả yêu cầu trong problem statement đã được thực hiện đầy đủ!**