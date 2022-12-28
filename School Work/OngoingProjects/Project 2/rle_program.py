#This is a function that prints out the menu of options available to the user
def menu():
    print("RLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")

#This function converts a list of RLE data and converts it into a hexidecimal string
def to_hex_string(data):
    dic = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",  10: "a", 11: "b", 12: "c", 13: "d",  14: "e", 15: "f"}
    for i in range(len(data)):
        data[i] = dic[data[i]]
    string = "".join(data)
    return string

#This function determines how many unique numbers there are in the set of raw uncompressed data
def count_runs(flat_data):
    temp = encode_rle(flat_data)
    print(temp)
    counter = 0
    for c in range(len(temp)):
        if c % 2 == 0:
            counter += 1
    return counter

#This function compresses raw data and turns it into a compressed RLE format
def encode_rle(flat_data):
    list2 = []
    current = flat_data[0]
    count = 1
    i = 0
    #For loop keeps track of how many numbers occur consequetively; the number being tracked and the amt of times that number
    #occurs in a row get appended to list2
    for item in flat_data[1:]:
        if current == item:
            count += 1
            i += 1
    #if the number occurs more than 15 time consequitively, the total occurances of that number are split and begins recounting again
    #everytime the counter hits the 15 mark
            if count == 15:
                list2.append(count)
                list2.append(flat_data[i])
                count = 0
        else:
            list2.append(count)
            list2.append(flat_data[i])
            current = item
            count = 1
            i += 1
    list2.append(count)
    list2.append(flat_data[i])
    return list2

#This function counts how many numbers there are in total in the decompressed RLE data set
def get_decoded_length(rle_data):
    length = 0
    for c in range(len(rle_data)):
        if c % 2 == 0:
            length += rle_data[c]
    return length

#This function decompresses RLE data into raw data
def decode_rle(rle_data):
    list3 = []
    for c in range(len(rle_data)):
        if c % 2 == 0:
            for i in range(rle_data[c]):
                (list3.append(rle_data[c + 1]))
    return list3

#This function converts a a hexidecimal string to a list of RLE data
def string_to_data(data_string):
    list4 = []
    dic2 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12,
            "d": 13, "e": 14, "f": 15}
    for item in data_string:
        CorrectDigit = dic2[item]
        list4.append(CorrectDigit)
    return list4

#This function translates RLE data into a human-readable representation
def to_rle_string(rle_data):
    list5 = []
    dic = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "a", 11: "b", 12: "c",
           13: "d", 14: "e", 15: "f"}
    for c in range(len(rle_data)):
        if c % 2 != 0:
            rle_data[c] = dic[rle_data[c]]
        rle_data[c] = str(rle_data[c])
    for i in range(0, len(rle_data) - 1, 2):
        list5.append(rle_data[i] + rle_data[i + 1])
    list5 = ":".join(list5)
    return list5

#Translates a string in human-readable RLE format (with delimiters) into RLE byte data.
def string_to_rle(rle_string):
    list = []
    list6 = []
    dic2 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12,
            "d": 13, "e": 14, "f": 15}
    for item in rle_string:
        if item in dic2:
            item = dic2[item]
        list.append(item)
    for i in range(len(list)):
        if i < len(list) - 3:
            if list[i + 3] == ":" and list[i] != ":":
                list[i] = int(str(list[i]) + str(list[i + 1]))
    for i in range(len(list)):
        if i < len(list) - 3:
            if list[i + 3] == ":" and list[i] != ":":
                del list[i + 1]
    for i in range(len(list)):
        if list[i] != ":":
            list6.append(list[i])
    return list6


if __name__ == "__main__":
    #importing libraries, information, making variables, etc
    from console_gfx import ConsoleGfx
    import console_gfx
    cg = ConsoleGfx
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    cg.display_image(cg.test_rainbow)
    print("")
    image_data = None
    KeepGoing = True

    while KeepGoing:
        #Prints out the menu and prompts the user to choose an input
        menu()
        option = int(input("\nSelect a Menu Option:"))

        #Ends the program
        if option == 0:
            break

        elif option == 1: #load image data from file
            # read the image data from file
            # assign cg.load_file(filename) to image data #filename is user input testfiles/fsu.gfx
            # store the image data in the image_data variable
            image_data = cg.load_file(input("Enter name of file to load: "))
            print("")

        elif option == 2: #load image data from test_image
            # assign cg.text_image to image_data
            image_data = cg.test_image
            print("Test image data loaded.")
            print("")

        #Reads RLE data from the user in decimal notation with delimiters
        elif option == 3:
            op3var = input("Enter an RLE string to be decoded: ")
            string_to_rle(op3var)

        #Reads RLE data from the user in hexadecimal notation without delimiters
        elif option == 4:
            op4var = input("Enter the hex string holding RLE data: ")
            string_to_data(op4var)


        #Reads raw (flat) data from the user in hexadecimal notation
        elif option == 5:
            op5var = input("Enter the hex string holding flat data: ")
            string_to_data(op5var)


        # display the image
        elif option == 6:
            print("Displaying image...")
            cg.display_image(image_data)
            print("")

        #Converts the current data into a human-readable RLE representation
        elif option == 7:
            print("RLE representation:", to_rle_string(string_to_data(op4var)))

        #Converts the current data into RLE hexadecimal representation
        elif option == 8:
            print("RLE hex values:", to_hex_string(string_to_rle(op3var)))

        #Displays the current raw (flat) data in hexadecimal representation
        elif option == 9:
            print("Flat hex values:", to_hex_string(decode_rle(string_to_rle(op3var))))






