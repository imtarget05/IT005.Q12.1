# Lab02 Modern Cryptography

Bài thực hành các thuật toán mã hóa hiện đại bằng Python, bao gồm Feistel Network, AES, DES, và RSA.

---

## Yêu cầu

- Python 3.x
- **Thư viện cần cài đặt:**
  - `pycryptodome` — Thư viện mã hóa cho AES, DES
  - `sympy` — Thư viện cho số học (sinh số nguyên tố, kiểm tra tính nguyên tố)

### Cài đặt thư viện

```bash
pip install pycryptodome sympy
```

Hoặc trên một số hệ thống:

```bash
pip3 install pycryptodome sympy
```

---

## Cấu trúc thư mục

```
Lab02_Modern_Cryptography/
└── src/
    ├── task2_1.py           # Feistel Network — Hiệu ứng Avalanche
    ├── task2_2.py           # AES — ECB và CBC modes
    ├── task2_3.py           # DES — Kiểm tra Avalanche Effect
    ├── task2_4.py           # AES — Phân tích ảnh hưởng của bit flip (CBC mode)
    ├── task2_5.py           # (Dành cho mở rộng)
    └── task2_6.py           # RSA Basics — Sinh số nguyên tố và Miller-Rabin test
```

---

## Hướng dẫn chạy

Mở terminal, di chuyển vào thư mục `src/`:

```bash
cd src
```

---

### Task 2.1 — Feistel Network (Avalanche Effect)

**File:** `task2_1.py`

```bash
python task2_1.py
```

**Mô tả:**
- Cài đặt một Feistel Network cơ bản với 4 vòng mã hóa
- Theo dõi cách các bit thay đổi qua từng vòng (Avalanche effect)
- Cách một thay đổi nhỏ ở input (từ 0xAB thành 0xAC) ảnh hưởng đến output

---

### Task 2.2 — AES (ECB & CBC Modes)

**File:** `task2_2.py`

```bash
python task2_2.py
```

**Mô tả:**
- So sánh hai chế độ mã hóa AES phổ biến:
  - **ECB (Electronic Codebook):** Mã hóa từng block độc lập, không an toàn với dữ liệu lặp
  - **CBC (Cipher Block Chaining):** Sử dụng IV, block trước ảnh hưởng đến block sau, an toàn hơn
- Hiển thị ciphertext ở dạng hex của cả hai chế độ

---

### Task 2.3 — DES (Avalanche Effect)

**File:** `task2_3.py`

```bash
python task2_3.py
```

**Mô tả:**
- Thực hiện kiểm tra **Avalanche Effect** trên DES
- So sánh mã hóa của hai plaintexts gần giống nhau (`STAYHOME` vs `STAYHOMA`)
- Tính toán số bit khác nhau giữa hai ciphertexts
- Một thuật toán mã hóa tốt cần có tỉ lệ avalanche gần 50%

---

### Task 2.4 — AES Bit Flip Analysis

**File:** `task2_4.py`

```bash
python task2_4.py
```

**Mô tả:**
- Phân tích ảnh hưởng của việc thay đổi các bit trong ciphertext khi dùng AES ở chế độ CBC
- Thay đổi ngẫu nhiên một bit ở một vị trí nào đó trong ciphertext
- Giải mã và so sánh plaintext bị hỏng với plaintext gốc
- Chỉ ra các block bị ảnh hưởng bởi sự thay đổi đó

---

### Task 2.6 — RSA Basics (Prime Generation & Miller-Rabin)

**File:** `task2_6.py`

```bash
python task2_6.py
```

**Mô tả:**
- Sinh số nguyên tố ngẫu nhiên với số bit được chỉ định
- Tìm 10 số nguyên tố lớn nhất dưới Mersenne số (2^89 - 1)
- Kiểm tra tính nguyên tố bằng thuật toán **Miller-Rabin Primality Test** (xác suất chính xác cao)
- Kiến thức nền tảng cho RSA public key cryptography

---

## Ghi chú

- Các task có thể chạy độc lập, không phụ thuộc vào nhau
- Cần đảm bảo Python 3.x và các thư viện được cài đặt trước khi chạy

 
 
