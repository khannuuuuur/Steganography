from PIL import Image
import numpy as np
#test change

#Image IO
def openImage(name):
    return np.array(Image.open(name))

def saveImage(imageArray, name):
    Image.fromarray(imageArray).save(name)


#Binary, string, decimal conversions
def stringToBinary(string):
    output = ""
    for c in string:
        num = ''.join(format(ord(c), 'b'))

        num = '0'*(7-len(num)) + num
        output += num
    return output

def binaryToString(binary):
    str_data =''
    for i in range(0, len(binary), 7):

        temp_data = int(binary[i:i + 7])

        decimal_data = binaryToDecimal(temp_data)

        str_data = str_data + chr(decimal_data)
    return str_data

def binaryToDecimal(binary):
    binary = int(binary)
    decimal, i = 0, 0
    while binary != 0:
        decimal += binary%10 * pow(2, i)
        binary //= 10
        i += 1
    return decimal

def decimalToBinary(n):
    return bin(n).replace("0b", "")



def encodeImage(image, message, name, removeBlanks=False):
    binary = stringToBinary(message)
    index = 0
    for row in range(len(image)):
        for col in range(len(image[row])):
            if index < len(binary):

                #if the least significant bit in the green value is the different than the bit in the binary message, adds 1 or -1
                if image[row][col][1]%2 != int(binary[index]):
                    image[row][col][1] += int(binary[index]) - image[row][col][1]%2


                index += 1
            elif removeBlanks: #sets all the rest to zero.
                if image[row][col][1]%2 != 0:
                    image[row][col][1] -= 1
            else:
                break
        if not removeBlanks and index >= len(binary):
            break

    saveImage(image, name)

def decodeImage(image, length):
    binary = ''
    index = 0
    for row in range(len(image)):
        for col in range(len(image[row])):

            binary += str(image[row][col][1]%2)

            length -= 1
            if length == 0:
                return binaryToString(binary)
    return binaryToString(binary)

def main():
    while True:
        option = int(input("Steganographic Processing:\n\t(1) Encode image\n\t(2) Decode image\n\t(3) Exit\nEnter an option: "))
        if option == 1:
            inFile = input("\nEnter an input file name: ")
            outFile = input("Enter an output file name: ")
            textFile = open(input("Enter a text file name to read from: "), 'r')
            removeGarbage = True if input("Remove garbage characters? (y/n) ") == 'y' else False
            encodeImage(openImage(inFile), textFile.read(), outFile, removeBlanks = removeGarbage)
            print("\nDone.\n")
        elif option == 2:
            inFile = input("\nEnter an input file name: ")
            length = int(input("Enter in how many characters to print out (-1 for all characters): "))
            print()
            print("="*60)
            print()
            print(decodeImage(openImage(inFile), length))
            print()
            print("="*60)
            print()
        else:
            print("\n"*2)
            break

if __name__ == "__main__":
    main()
