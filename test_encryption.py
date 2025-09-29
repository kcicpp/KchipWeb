#!/usr/bin/env python3
"""
Test script for the encryption program
"""

import numpy as np
from main import TextEncoder

def test_caesar():
    print("🧪 Testing Caesar Cipher")
    encoder = TextEncoder()
    
    # Test case 1: Basic text
    text = "Hello World"
    shift = 3
    encrypted = encoder.caesar_encrypt(text, shift)
    decrypted = encoder.caesar_decrypt(encrypted, shift)
    print(f"Original: {text}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    assert text == decrypted, "Caesar decryption failed"
    print("✅ Caesar test passed\n")

def test_affine():
    print("🧪 Testing Affine Cipher")
    encoder = TextEncoder()
    
    # Test case: Basic text
    text = "Hello World"
    a, b = 3, 5
    encrypted = encoder.affine_encrypt(text, a, b)
    decrypted = encoder.affine_decrypt(encrypted, a, b)
    print(f"Original: {text}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    assert text == decrypted, "Affine decryption failed"
    print("✅ Affine test passed\n")

def test_vigenere():
    print("🧪 Testing Vigenere Cipher")
    encoder = TextEncoder()
    
    # Test case: Basic text
    text = "Hello World"
    key = "KEY"
    encrypted = encoder.vigenere_encrypt(text, key)
    decrypted = encoder.vigenere_decrypt(encrypted, key)
    print(f"Original: {text}")
    print(f"Key: {key}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    assert text == decrypted, "Vigenere decryption failed"
    print("✅ Vigenere test passed\n")

def test_hill():
    print("🧪 Testing Hill Cipher")
    encoder = TextEncoder()
    
    # Test case: Basic text with special characters
    text = "Hello World! 123"
    # Using a 2x2 matrix that has an inverse mod 26
    key_matrix = np.array([[3, 2], [5, 7]])
    
    encrypted = encoder.hill_encrypt(text, key_matrix)
    decrypted = encoder.hill_decrypt(encrypted, key_matrix)
    print(f"Original: {text}")
    print(f"Key matrix:\n{key_matrix}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    
    # Check if special characters and numbers are preserved
    print(f"Special chars preserved: {'!' in decrypted and '123' in decrypted}")
    print("✅ Hill test completed\n")

def test_special_characters():
    print("🧪 Testing Special Character Preservation")
    encoder = TextEncoder()
    
    text = "Hello World! 123 @#$"
    
    # Test Caesar
    encrypted = encoder.caesar_encrypt(text, 5)
    print(f"Caesar with special chars: {text} -> {encrypted}")
    
    # Test Vigenere
    encrypted = encoder.vigenere_encrypt(text, "KEY")
    print(f"Vigenere with special chars: {text} -> {encrypted}")
    
    # Test Hill
    key_matrix = np.array([[3, 2], [5, 7]])
    encrypted = encoder.hill_encrypt(text, key_matrix)
    print(f"Hill with special chars: {text} -> {encrypted}")
    print("✅ Special character tests completed\n")

if __name__ == "__main__":
    print("🔬 Running encryption tests...\n")
    
    try:
        test_caesar()
        test_affine()
        test_vigenere()
        test_hill()
        test_special_characters()
        
        print("🎉 All tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()