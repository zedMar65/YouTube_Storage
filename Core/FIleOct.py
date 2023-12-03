def convertToBin(file_path):
    import os
    with open(file_path, 'rb') as file:
        file_content = file.read()
        file_name, file_extension = os.path.splitext(os.path.basename(file_path))
        buffer = b"BufFq"
        
        encStr = file_content + buffer + file_name.encode() + file_extension.encode() + buffer
        binary_string = ''.join(format(char, '08b') for char in encStr)
        
        return binary_string

def binaryToFile(binary_str):
    # Find the binary separator in the input
    separator = "0100001001110101011001100100011001110001"
    pieces = binary_str.split(separator)[0:2]
    
    # Extract binary data and convert it to ASCII
    binary_data = pieces[0]
    
    binary_chunks = [pieces[1][i:i + 8] for i in range(0, len(pieces[1]), 8)]
    file_name = ''.join([chr(int(chunk, 2)) for chunk in binary_chunks])

    with open(file_name, 'wb') as file:
        file.write(bytes([int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8)]))
    
    print(f"File '{file_name}' successfully created and written.")
