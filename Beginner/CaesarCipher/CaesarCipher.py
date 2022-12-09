from base64 import decode
from turtle import position
from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, direction):
    end_text=""

    if(direction == "decode"):
            shift_amount *= -1

    for letter in start_text:
        if letter in start_text:
            position = alphabet.index(letter)
            new_letter = alphabet[position + shift_amount]
            end_text += new_letter
        else:
            end_text += letter
        
    print(f"The {direction}d text is {end_text}")

print(logo)
program = True

while program:
    type = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    message = input("Type your message: \n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=message, shift_amount=shift, direction=type)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if(again == "yes"):
        program = True
    elif(again == "no"):
        program = False
        print("Goodbye!")