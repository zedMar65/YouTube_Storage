def convertToBin(file_path):
    import os
    with open(file_path, 'rb') as file:
        file_content = file.read()
        file_name, file_extension = os.path.splitext(os.path.basename(file_path))
        buffer = "BufFq"  # 0100001001110101011001100100011001110001
        
        encStr = str(file_content) + buffer + file_name + file_extension + buffer
        binary_string = ''.join(format(char, '08b') for char in encStr.encode())
        
        return binary_string
def binaryToFile(binary_str):
    # Find the binary separator in the input
    separator = "0100001001110101011001100100011001110001"
    print(binary_str)
    pieces = binary_str.split(separator)[0:2]
    
    # Extract binary data and convert it to ASCII
    binary_data = pieces[0]
    ascii_data = ''.join([chr(int(chunk, 2)) for chunk in [binary_data[i:i + 8] for i in range(0, len(binary_data), 8)]])
    
    # Extract file name from the second piece
    binary_chunks = [pieces[1][i:i + 8] for i in range(0, len(pieces[1]), 8)]
    file_name = ''.join([chr(int(chunk, 2)) for chunk in binary_chunks])

    # Create a file with the extracted file name and write the ASCII data
    with open(file_name, 'w') as file:
        file.write(ascii_data[2:len(ascii_data)-1])
    print(f"File '{file_name}' successfully created and written.")
