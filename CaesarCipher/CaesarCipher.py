from base64 import decode
from turtle import position
from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(message, shift):
    encrypted_message = ""
    for letter in message:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        encrypted_message += new_letter
    print(f"The encoded text is {encrypted_message}")

def decrypt(message, shift):
    dencrypted_message = ""
    for letter in message:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        dencrypted_message += new_letter
    print(f"The decided text is {dencrypted_message}")

def caesar(type):
    message = input("Type your message: \n").lower()
    shift = int(input("Type the shift number:\n"))
    if(type == "encode"):
        encrypt(message, shift)
    elif(type == "decode"):
        decrypt(message, shift)
    else:
        print("Error")

print(logo)
type = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
caesar(type)