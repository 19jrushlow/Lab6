# Joshua Rushlow


# Encoder
def encode(password):
    password = list(password)
    encoded_password = ''
    for x in password:
        encoded_password += str(int(x)+3)[-1]
    return encoded_password


# Decoder
def decode(password):
    password = list(password)
    encoded_password = ''
    for x in password:
        encoded_password += str(int(x) + 7)[-1]
    return encoded_password


# main code
print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
while True:
    choice = int(input('Please enter an option: '))
    if choice == 1:
        encoded_pw = encode(input('Please enter your password to encode: '))
        print('Your password has been encoded and stored!')
    elif choice == 2:
        print('The encoded password is ' + encoded_pw + ', and the original password is ' + decode(encoded_pw) + '.')
    elif choice == 3:
        exit()
