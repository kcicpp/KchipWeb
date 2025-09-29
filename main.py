#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chương trình mã hóa văn bản
Hỗ trợ 4 loại mã hóa: Caesar, Affine, Vigenere, Hill
"""

import numpy as np
import string
import re
from math import gcd

class TextEncoder:
    def __init__(self):
        self.alphabet = string.ascii_lowercase
        self.alphabet_size = 26
    
    def gcd_extended(self, a, b):
        """Thuật toán Euclid mở rộng để tìm modular inverse"""
        if a == 0:
            return b, 0, 1
        gcd_val, x1, y1 = self.gcd_extended(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd_val, x, y
    
    def mod_inverse(self, a, m):
        """Tìm modular inverse của a modulo m"""
        gcd_val, x, _ = self.gcd_extended(a, m)
        if gcd_val != 1:
            return None
        return (x % m + m) % m
    
    def matrix_mod_inverse(self, matrix, mod):
        """Tìm inverse của ma trận modulo mod"""
        det = int(np.linalg.det(matrix))
        det = det % mod
        det_inv = self.mod_inverse(det, mod)
        if det_inv is None:
            return None
        
        # Tính adjugate matrix
        adj = np.array([[matrix[1,1], -matrix[0,1]], 
                       [-matrix[1,0], matrix[0,0]]])
        adj = adj % mod
        
        # Inverse matrix
        inv_matrix = (det_inv * adj) % mod
        return inv_matrix
    
    # 1. MÃ CAESAR (Substitution Cipher)
    def caesar_encrypt(self, text, shift):
        """Mã hóa Caesar"""
        result = ""
        for char in text:
            if char.lower() in self.alphabet:
                is_upper = char.isupper()
                char_index = self.alphabet.index(char.lower())
                encrypted_index = (char_index + shift) % self.alphabet_size
                encrypted_char = self.alphabet[encrypted_index]
                if is_upper:
                    encrypted_char = encrypted_char.upper()
                result += encrypted_char
            else:
                result += char  # Giữ nguyên ký tự đặc biệt
        return result
    
    def caesar_decrypt(self, text, shift):
        """Giải mã Caesar"""
        return self.caesar_encrypt(text, -shift)
    
    # 2. MÃ AFFINE
    def affine_encrypt(self, text, a, b):
        """Mã hóa Affine: E(x) = (ax + b) mod 26"""
        if gcd(a, self.alphabet_size) != 1:
            raise ValueError(f"Giá trị a={a} không hợp lệ. a phải nguyên tố cùng nhau với 26.")
        
        result = ""
        for char in text:
            if char.lower() in self.alphabet:
                is_upper = char.isupper()
                char_index = self.alphabet.index(char.lower())
                encrypted_index = (a * char_index + b) % self.alphabet_size
                encrypted_char = self.alphabet[encrypted_index]
                if is_upper:
                    encrypted_char = encrypted_char.upper()
                result += encrypted_char
            else:
                result += char  # Giữ nguyên ký tự đặc biệt
        return result
    
    def affine_decrypt(self, text, a, b):
        """Giải mã Affine: D(y) = a^(-1)(y - b) mod 26"""
        a_inv = self.mod_inverse(a, self.alphabet_size)
        if a_inv is None:
            raise ValueError(f"Không thể tìm inverse của a={a}")
        
        result = ""
        for char in text:
            if char.lower() in self.alphabet:
                is_upper = char.isupper()
                char_index = self.alphabet.index(char.lower())
                decrypted_index = (a_inv * (char_index - b)) % self.alphabet_size
                decrypted_char = self.alphabet[decrypted_index]
                if is_upper:
                    decrypted_char = decrypted_char.upper()
                result += decrypted_char
            else:
                result += char  # Giữ nguyên ký tự đặc biệt
        return result
    
    # 3. MÃ VIGENERE
    def vigenere_encrypt(self, text, key):
        """Mã hóa Vigenere"""
        key = key.lower()
        result = ""
        key_index = 0
        
        for char in text:
            if char.lower() in self.alphabet:
                is_upper = char.isupper()
                char_index = self.alphabet.index(char.lower())
                key_char_index = self.alphabet.index(key[key_index % len(key)])
                encrypted_index = (char_index + key_char_index) % self.alphabet_size
                encrypted_char = self.alphabet[encrypted_index]
                if is_upper:
                    encrypted_char = encrypted_char.upper()
                result += encrypted_char
                key_index += 1
            else:
                result += char  # Giữ nguyên ký tự đặc biệt
        return result
    
    def vigenere_decrypt(self, text, key):
        """Giải mã Vigenere"""
        key = key.lower()
        result = ""
        key_index = 0
        
        for char in text:
            if char.lower() in self.alphabet:
                is_upper = char.isupper()
                char_index = self.alphabet.index(char.lower())
                key_char_index = self.alphabet.index(key[key_index % len(key)])
                decrypted_index = (char_index - key_char_index) % self.alphabet_size
                decrypted_char = self.alphabet[decrypted_index]
                if is_upper:
                    decrypted_char = decrypted_char.upper()
                result += decrypted_char
                key_index += 1
            else:
                result += char  # Giữ nguyên ký tự đặc biệt
        return result
    
    # 4. MÃ HILL
    def hill_encrypt(self, text, key_matrix):
        """Mã hóa Hill với xử lý ký tự đặc biệt"""
        if key_matrix.shape[0] != key_matrix.shape[1]:
            raise ValueError("Ma trận key phải là ma trận vuông")
        
        # Kiểm tra tính khả nghịch của ma trận
        det = int(np.linalg.det(key_matrix)) % self.alphabet_size
        if gcd(det, self.alphabet_size) != 1:
            raise ValueError("Ma trận key không khả nghịch (determinant không nguyên tố cùng nhau với 26)")
        
        n = key_matrix.shape[0]
        
        # Tách các phần của text
        letters = []
        non_letters = []
        positions = []
        
        for i, char in enumerate(text):
            if char.lower() in self.alphabet:
                letters.append(char)
                positions.append(('letter', i))
            else:
                non_letters.append(char)
                positions.append(('non_letter', i))
        
        # Padding nếu cần thiết
        while len(letters) % n != 0:
            letters.append('x')
        
        # Mã hóa các chữ cái
        encrypted_letters = []
        for i in range(0, len(letters), n):
            block = letters[i:i+n]
            
            # Chuyển đổi thành số
            block_numbers = []
            case_info = []
            for char in block:
                case_info.append(char.isupper())
                block_numbers.append(self.alphabet.index(char.lower()))
            
            # Mã hóa block
            block_vector = np.array(block_numbers).reshape(n, 1)
            encrypted_vector = (key_matrix @ block_vector) % self.alphabet_size
            
            # Chuyển về chữ cái
            for j, num in enumerate(encrypted_vector.flatten()):
                encrypted_char = self.alphabet[num]
                if case_info[j]:
                    encrypted_char = encrypted_char.upper()
                encrypted_letters.append(encrypted_char)
        
        # Ghép lại kết quả với ký tự đặc biệt
        result = ""
        letter_index = 0
        non_letter_index = 0
        
        for pos_type, pos in positions:
            if pos_type == 'letter':
                if letter_index < len(encrypted_letters):
                    result += encrypted_letters[letter_index]
                    letter_index += 1
            else:
                if non_letter_index < len(non_letters):
                    result += non_letters[non_letter_index]
                    non_letter_index += 1
        
        return result
    
    def hill_decrypt(self, text, key_matrix):
        """Giải mã Hill với xử lý ký tự đặc biệt"""
        inv_matrix = self.matrix_mod_inverse(key_matrix, self.alphabet_size)
        if inv_matrix is None:
            raise ValueError("Ma trận key không thể nghịch đảo")
        
        return self.hill_encrypt(text, inv_matrix)

def display_menu():
    """Hiển thị menu chính"""
    print("\n" + "="*50)
    print("🔐 CHƯƠNG TRÌNH MÃ HÓA VĂN BẢN 🔐")
    print("="*50)
    print("1. 🔤 Mã Caesar (Substitution)")
    print("2. 🔢 Mã Affine")
    print("3. 🔑 Mã Vigenere")
    print("4. 🎯 Mã Hill")
    print("0. ❌ Thoát chương trình")
    print("="*50)

def get_valid_input(prompt, input_type="str", condition=None):
    """Lấy input hợp lệ từ người dùng"""
    while True:
        try:
            if input_type == "int":
                value = int(input(prompt))
            elif input_type == "float":
                value = float(input(prompt))
            else:
                value = input(prompt)
            
            if condition and not condition(value):
                print("❌ Giá trị không hợp lệ. Vui lòng thử lại.")
                continue
            
            return value
        except ValueError:
            print("❌ Định dạng không hợp lệ. Vui lòng thử lại.")

def caesar_cipher_menu():
    """Menu cho mã Caesar"""
    encoder = TextEncoder()
    print("\n🔤 MÃ CAESAR")
    print("-" * 30)
    
    text = input("Nhập văn bản: ")
    shift = get_valid_input("Nhập độ dịch chuyển (0-25): ", "int", 
                           lambda x: 0 <= x <= 25)
    
    choice = get_valid_input("Chọn (1-Mã hóa, 2-Giải mã): ", "int",
                            lambda x: x in [1, 2])
    
    try:
        if choice == 1:
            result = encoder.caesar_encrypt(text, shift)
            print(f"✅ Kết quả mã hóa: {result}")
        else:
            result = encoder.caesar_decrypt(text, shift)
            print(f"✅ Kết quả giải mã: {result}")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

def affine_cipher_menu():
    """Menu cho mã Affine"""
    encoder = TextEncoder()
    print("\n🔢 MÃ AFFINE")
    print("-" * 30)
    
    text = input("Nhập văn bản: ")
    
    # Các giá trị a hợp lệ (nguyên tố cùng nhau với 26)
    valid_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    print(f"Các giá trị a hợp lệ: {valid_a}")
    
    a = get_valid_input("Nhập a: ", "int", lambda x: x in valid_a)
    b = get_valid_input("Nhập b (0-25): ", "int", lambda x: 0 <= x <= 25)
    
    choice = get_valid_input("Chọn (1-Mã hóa, 2-Giải mã): ", "int",
                            lambda x: x in [1, 2])
    
    try:
        if choice == 1:
            result = encoder.affine_encrypt(text, a, b)
            print(f"✅ Kết quả mã hóa: {result}")
        else:
            result = encoder.affine_decrypt(text, a, b)
            print(f"✅ Kết quả giải mã: {result}")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

def vigenere_cipher_menu():
    """Menu cho mã Vigenere"""
    encoder = TextEncoder()
    print("\n🔑 MÃ VIGENERE")
    print("-" * 30)
    
    text = input("Nhập văn bản: ")
    key = get_valid_input("Nhập khóa (chỉ chữ cái): ", "str",
                         lambda x: x.isalpha() and len(x) > 0)
    
    choice = get_valid_input("Chọn (1-Mã hóa, 2-Giải mã): ", "int",
                            lambda x: x in [1, 2])
    
    try:
        if choice == 1:
            result = encoder.vigenere_encrypt(text, key)
            print(f"✅ Kết quả mã hóa: {result}")
        else:
            result = encoder.vigenere_decrypt(text, key)
            print(f"✅ Kết quả giải mã: {result}")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

def hill_cipher_menu():
    """Menu cho mã Hill"""
    encoder = TextEncoder()
    print("\n🎯 MÃ HILL")
    print("-" * 30)
    
    text = input("Nhập văn bản: ")
    
    # Chọn kích thước ma trận
    size = get_valid_input("Chọn kích thước ma trận (2 hoặc 3): ", "int",
                          lambda x: x in [2, 3])
    
    print(f"Nhập ma trận key {size}x{size}:")
    key_matrix = np.zeros((size, size), dtype=int)
    
    for i in range(size):
        for j in range(size):
            key_matrix[i][j] = get_valid_input(f"Nhập phần tử [{i+1}][{j+1}]: ", "int",
                                              lambda x: 0 <= x <= 25)
    
    print(f"Ma trận key:\n{key_matrix}")
    
    choice = get_valid_input("Chọn (1-Mã hóa, 2-Giải mã): ", "int",
                            lambda x: x in [1, 2])
    
    try:
        if choice == 1:
            result = encoder.hill_encrypt(text, key_matrix)
            print(f"✅ Kết quả mã hóa: {result}")
        else:
            result = encoder.hill_decrypt(text, key_matrix)
            print(f"✅ Kết quả giải mã: {result}")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

def main():
    """Hàm main của chương trình"""
    print("🔐 Chào mừng đến với chương trình mã hóa văn bản!")
    
    while True:
        display_menu()
        choice = get_valid_input("Chọn chức năng (0-4): ", "int",
                                lambda x: 0 <= x <= 4)
        
        if choice == 0:
            print("👋 Cảm ơn bạn đã sử dụng chương trình!")
            break
        elif choice == 1:
            caesar_cipher_menu()
        elif choice == 2:
            affine_cipher_menu()
        elif choice == 3:
            vigenere_cipher_menu()
        elif choice == 4:
            hill_cipher_menu()
        
        # Hỏi có muốn tiếp tục không
        continue_choice = input("\n🔄 Bạn có muốn tiếp tục? (y/n): ").lower()
        if continue_choice != 'y':
            print("👋 Cảm ơn bạn đã sử dụng chương trình!")
            break

if __name__ == "__main__":
    main()