def convert_oct(file_path):
    import os
    with open(file_path, 'rb') as file:
        file_content = file.read()
        file_name, file_extension = os.path.splitext(os.path.basename(file_path))
        buffer = "BufFq"# 102125106106105122061062063
        encStr = str(file_content)+buffer+file_name+file_extension+buffer
        octal_string = ''.join(format(ord(char), '03o') for char in encStr)
        
        return octal_string

def octToFile(oct_str):
    pieces = oct_str.split("102165146106161")[0:2]
    
    # Extract octal data and convert it to ASCII
    octal_data = pieces[0]
    ascii_data = ''.join([chr(int(chunk, 8)) for chunk in [octal_data[i:i + 3] for i in range(0, len(octal_data), 3)]])

    # Extract file name from the second piece
    print(pieces[1])
    octal_chunks = [pieces[1][i:i + 3] for i in range(0, len(pieces[1]), 3)]
    file_name = ''.join([chr(int(chunk, 8)) for chunk in octal_chunks])

    # Create a file with the extracted file name and write the ASCII data
    with open(file_name, 'w') as file:
        file.write(ascii_data[2:len(ascii_data)-1])
    print(f"File '{file_name}' successfully created and written.")