text = input("Type your message here=")
shift = int(input("Give the shift value="))
encrypted =''
choice = input("Type 'encrypt' or 'decrypt'=")
for letter in text:
    if letter.isalpha():
        letter = letter.upper()
        number = ord(letter) - ord('A')
        if choice == "encrypt":
            shifted = (number + shift) % 26
        else:
            shifted = (number - shift) % 26
        encrypted += chr(shifted + ord('A'))
    else:
        encrypted += letter 
print("your encrypted message is=", encrypted)  

            

       
