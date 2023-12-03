from Core.FIleOct import convertToBin
from Core.Video import create_video

if __name__ == "__main__":
    try:
        print("Input Path:")
        file_path = input()
        output_video_path = r'OutputVideo.mp4'
        
        Bin_String = convertToBin(file_path)
        if Bin_String is not None:
            print("Processing...")
            print(Bin_String)
            create_video(Bin_String, output_video_path)
            print("Success, file saved as", output_video_path)
        else:
            print("Canceling...")
    
    except KeyboardInterrupt:
        print("\nExecution interrupted by user.")

    except Exception as ex:
        print(f"An unexpected errQor occurred: {ex}")