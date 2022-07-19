from base64 import decode
from turtle import position
from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    encrypted_message = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        encrypted_message += new_letter
    print(f"The encoded text is {encrypted_message}")

def decrypt(plain_text, shift_amount):
    dencrypted_message = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        dencrypted_message += new_letter
    print(f"The decided text is {dencrypted_message}")

def caesar(start_text, shift_amount, direction):
    end_text=""
    for letter in start_text:
        position = alphabet.index(letter)
        if(direction == "decode"):
            shift_amount *= -1
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        end_text += new_letter
    print(f"The {direction}d text is {end_text}")

print(logo)

type = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
message = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))

caesar(start_text=message, shift_amount=shift, direction=type)