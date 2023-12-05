from mutagen.mp4 import MP4
from Core.FIleOct import convertToBin

def write_metadata(input_bytes, output_file):
    # Create an MP4 instance
    mp4_file = MP4()

    # Set the metadata tag with the input bytes
    mp4_file["\xa9day"] = [input_bytes]

    # Save the MP4 file with the metadata
    mp4_file.save(output_file)

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