def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += chr((ord(char) + s - 33) % 16 + 33)
    return result
def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += chr((ord(char) - s - 33) % 16 + 33)
    return result

key=input('enter the message: ')
print('Enter (E or e)for encryption / For decryption (D or d) ')
inp = input()
print('Enter the number to shift the letters')
num = int(input())
if inp == 'E' or inp == 'e':
    print('Encrypted Text:')
    s = encrypt(key, num)
    print(s)
elif inp == 'D' or inp == 'd':
    print('Decrypted Text:')
    k = decrypt(key, num)
    print(k)
else:
    print('enter the correct input')