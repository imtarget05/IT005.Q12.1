import base64

def rsa_key(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)        
    return n, phi, d

print("\nPHẦN 1: Xác định khóa công khai PU và khóa riêng tư PR")

print("\n1.1 Khóa 1 (p=11, q=17, e=7):")
p1, q1, e1 = 11, 17, 7
n1, phi1, d1 = rsa_key(p1, q1, e1)
print(f"   p  = {p1}")
print(f"   q  = {q1}")
print(f"   e  = {e1}")
print(f"   n  = p × q = {n1}")
print(f"   φ(n) = (p-1)×(q-1) = {phi1}")
print(f"   Khóa công khai  PU = ({e1}, {n1})")
print(f"   Khóa riêng tư   PR = ({d1}, {n1})")

print("\n1.2 Khóa 2:")
p2 = 2007999387284322116151219
q2 = 676717145751736242170789
e2 = 17
n2, phi2, d2 = rsa_key(p2, q2, e2)
print(f"   Khóa công khai  PU = ({e2}, {n2})")
print(f"   Khóa riêng tư   PR = ({d2}, {n2})")

print("\n1.3 Khóa 3 (dạng hex):")
p3 = int("F7E75FDC469067FFDC4E847C51F452DF", 16)
q3 = int("E85CED54AF57E53E092113E62F436F4F", 16)
e3 = int("0D88C3", 16)
n3, phi3, d3 = rsa_key(p3, q3, e3)
print(f"   Khóa công khai  PU = ({e3}, {n3})")
print(f"   Khóa riêng tư   PR = ({d3}, {n3})")

print("\nPHẦN 2: Mã hóa và giải mã bản rõ M = 5 với khóa 1")

M = 5

print("\n2.1 Mã hóa cho tính bảo mật (Confidentiality):")
C_conf = pow(M, e1, n1)
M_dec_conf = pow(C_conf, d1, n1)
print(f"   Bản mã C = M^e mod n = {M}^{e1} mod {n1} = {C_conf}")
print(f"   Giải mã   = C^d mod n = {M_dec_conf} \n")

print("2.2 Mã hóa cho tính xác thực (Authentication):")
C_auth = pow(M, d1, n1)
M_dec_auth = pow(C_auth, e1, n1)
print(f"   Bản mã C = M^d mod n = {M}^{d1} mod {n1} = {C_auth}")
print(f"   Xác minh  = C^e mod n = {M_dec_auth} ")

print("\nPHẦN 3: Mã hóa thông điệp 'The University of Information Technology'")

message = "The University of Information Technology"
M_msg = int.from_bytes(message.encode('utf-8'), 'big')

C_msg = pow(M_msg, e3, n3)
cipher_base64 = base64.b64encode(C_msg.to_bytes((C_msg.bit_length() + 7) // 8, 'big')).decode('utf-8')

print(f"Thông điệp gốc: {message}")
print(f"Bản mã dưới dạng Base64:\n{cipher_base64}")

print("\nPHẦN 4: Giải mã các bản mã cho sẵn")

ct1 = "raUcesUIOkx/8ZhgodMod0Uu18sC20yXIQFevSu7W/FDxIy0YRHMyXcHdD9PBvIT2aUtt5fCQEGomjVVPv4I"
pt1 = pow(int.from_bytes(base64.b64decode(ct1), 'big'), d3, n3)
print(f"1. Bản mã Base64 dài     → Giải bằng khóa 3: {pt1}")

ct2 = "C87F570FC4F699CEC24020C6F54221ABAB2CE0C3"
pt2 = pow(int(ct2, 16), d2, n2)
print(f"2. Bản mã Hex            → Giải bằng khóa 2: {pt2}")

ct3 = "Z2BUSkJcg0w4XEpgm0JcMExEQmBlVH6dYEpNTHpMHptMQ7NgTHlgQrNMQ2BKTQ=="
pt3 = pow(int.from_bytes(base64.b64decode(ct3), 'big'), d3, n3)
print(f"3. Bản mã Base64 thứ 3   → Giải bằng khóa 3: {pt3}")

binary_str = "001010000001010011111111101101110010111011001010111011000110011110111111001111110110100011001111001100001001010001010100111101010100110011101110111011110101101100000100"
C_bin = int(binary_str.replace(" ", "").replace("\n", ""), 2)
pt_bin = pow(C_bin, d3, n3)
print(f"4. Bản mã Binary         → Giải bằng khóa 3: {pt_bin}")
