from Core.FileToHex import *
from Core.Video import *

if __name__ == "__main__":
    try:
        print("Input Path:")
        file_path = input()  # Use a raw string to avoid Unicode escape error
        output_video_path = r'OutputVideo.mp4'
        
        hex_string = convert_hex(file_path)

        if hex_string is not None:
            print("Processing...")
            create_video(hex_string, output_video_path)
            print("Success, file saved as", output_video_path)
        else:
            print("Canceling...")
    
    except KeyboardInterrupt:
        print("\nExecution interrupted by user.")

    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")