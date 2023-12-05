from Core.FIleOct import convertToBin
from Core.Video import write_metadata


if __name__ == "__main__":
    try:
        print("Input Path:")
        file_path = input()
        print("Mask Video input path:")
        output_file = input()
        
        input_bytes = convertToBin(file_path)
        if input_bytes is not None:
            print("Processing...")
            write_metadata(input_bytes, output_file)
            print("Wrote to: ",output_file)
    except KeyboardInterrupt:
        print("Canceled")