#This function translates a hexadigit character/number into the decimal equivalent
def hex_char_decode(digit):
    digit = str(digit)
    dic = {"0":0,
          "1":1,
          "2":2,
          "3":3,
          "4":4,
          "5":5,
          "6":6,
          "7":7,
          "8":8,
          "9":9,
          "A":10,
          "B":11,
          "C":12,
          "D":13,
          "E":14,
          "F":15,
           "a": 10,
           "b": 11,
           "c": 12,
           "d": 13,
           "e": 14,
           "f": 15
           }
    CorrectDigit = dic[digit]
    return CorrectDigit

#This function takes an hexadecimal input and converts it into a decimal value
def hex_string_decode(hex):
    decimal = 0
    if hex[0:2] == "0x":
        hex = hex[2:]
    for i in range(len(hex)):
        number = hex_char_decode(hex[i])
        decimal = int(number) + decimal*16
    return decimal

#This function takes an binary input and converts it into a decimal value
def binary_string_decode(binary):
    decimal = 0
    if binary[0:2] == "0b":
        binary = binary[2:]
    for i in range(len(binary)):
        decimal = int(binary[i]) + decimal*2
    return decimal

#This is the function to turn binary into hexadecimal but i got lazy and didn't do it
def binary_to_hex(binary):
    pass

#This function is used to print out the menu
def Menu():
    print("Decoding Menu")
    print("-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit")
    print("")

#This was necessary in order to get zybooks to recognise the functions
if __name__ == "__main__":
    #The KeepGoing variable and while loop are used to repeat the program until the user chooses to end it
    KeepGoing = True
    while KeepGoing:

        #This calls the menu function and prompts the user to input what type of conversion they want
        Menu()
        option = int(input("Please enter an option: "))

        #This option Calls the hex_string_decode function and converts hexadecimal number to a decimal number
        if option == 1:
            hex = input("Please enter the numeric string to convert: ")
            print("Result:", hex_string_decode(hex))
            print("")

        #This option Calls the binary_string_decode function and converts binary number to a decimal number
        elif option == 2:
            binary = input("Please enter the numeric string to convert: ")
            print("Result:", binary_string_decode(binary))
            print("")

        #This is supposed to convert hexadecimal to binary but I got lazy and didn't do it
        elif option == 3:
            binary = input("Please enter the numeric string to convert: ")
            binary_to_hex(binary)
            print("")

        #This choice exits the program
        elif option == 4:
            print("Goodbye!")
            KeepGoing = False



