from Core.FIleOct import convert_oct
from Core.Video import create_video

if __name__ == "__main__":
    try:
        print("Input Path:")
        file_path = input()
        output_video_path = r'OutputVideo.mp4'
        
        hex_string = convert_oct(file_path)
        if hex_string is not None:
            print("Processing...")
            create_video(hex_string, output_video_path)
            print("Success, file saved as", output_video_path)
        else:
            print("Canceling...")
    
    except KeyboardInterrupt:
        print("\nExecution interrupted by user.")

    except Exception as ex:
        print(f"An unexpected errQor occurred: {ex}")