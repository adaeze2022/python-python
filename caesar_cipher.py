from turtle import position


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
text = input("Type your message here: \n")
shift = int(input("Type the shift number below: \n"))
def caesar(start_text, shift_amount, shift_direction):
    end_text = ""
    if shift_direction == "decode":
            shift_amount *= -1
    for letter in start_text:
        positions = alphabet.index(letter)
        new_positions = positions + shift_amount
        end_text += alphabet[new_positions]
    print(f"The {direction}d text is {end_text}")
caesar(start_text=text, shift_amount=shift, shift_direction=direction)