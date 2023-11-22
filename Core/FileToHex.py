
def convert_hex(file_path):
    import os
    try:
        with open(file_path, 'rb') as file:
            # Read the entire file into bytes
            file_content = file.read()

            # Convert bytes to hexadecimal string
            hex_string = file_content.hex()

            # Get the file name and extension
            file_name, file_extension = os.path.splitext(os.path.basename(file_path))

            # Convert file name and extension to hexadecimal string
            hex_file_name = file_name.encode('utf-8').hex()
            hex_file_extension = file_extension.encode('utf-8').hex()

            # Use a hexadecimal buffer (delimiter) between content and file name/extension
            hex_buffer = "4245464f525f313233"  # Hex representation of "BUFFER123"
            hex_string += hex_buffer + hex_file_name + hex_file_extension

            return hex_string

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None