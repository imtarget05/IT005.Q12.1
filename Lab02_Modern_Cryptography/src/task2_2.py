from Crypto.Cipher import AES

key = b'1234567890123456'
plaintext = b"UIT_LAB_UIT_LAB_UIT_LAB_UIT_LAB_" 

cipher_ecb = AES.new(key, AES.MODE_ECB)
ct_ecb = cipher_ecb.encrypt(plaintext)

iv = b'\x00' * 16
cipher_cbc = AES.new(key, AES.MODE_CBC, iv=iv)
ct_cbc = cipher_cbc.encrypt(plaintext)

print(f"--- KẾT QUẢ NHIỆM VỤ 2.2 ---")
print(f"ECB Hex: {ct_ecb.hex()}")
print(f"CBC Hex: {ct_cbc.hex()}\n")

print("Phân tích khối ECB (Mỗi khối 32 ký tự hex):")
print(f"Khối 1: {ct_ecb.hex()[:32]}")
print(f"Khối 2: {ct_ecb.hex()[32:]}")
print("=> NHẬN XÉT: Hai khối giống hệt nhau do bản rõ lặp lại.")

print("\nPhân tích khối CBC:")
print(f"Khối 1: {ct_cbc.hex()[:32]}")
print(f"Khối 2: {ct_cbc.hex()[32:]}")
print("=> NHẬN XÉT: Hai khối khác hẳn nhau nhờ cơ chế xâu chuỗi (Chaining).")