import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Encrypting/decrypting function
def caeser(start_text, shift_amount, cipher_direction):
    shifted_text = "" 
    if direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            relative_position = len(alphabet) - position
            new_position = position + shift_amount
            if new_position < len(alphabet):
                shifted_letter = alphabet[new_position]
                shifted_text += shifted_letter
            else:
                shifted_letter = alphabet[(shift_amount - relative_position)]
                shifted_text += shifted_letter
        else:
            shifted_text += letter
    print(f"The {cipher_direction}d text is {shifted_text}")

# Display logo
print(art.logo)

# Run program as many times as user wants
repeat = True
while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Modify shift value to fit within alphabet and then run caeser() function
    shift = shift % 26
    caeser(text, shift, direction)
        
    # End program when user is finished
    go_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
    if go_again == "no":
        repeat = False
        print("Goodbye!")