from Core.FIleOct import binaryToFile
from Core.Video import vidToOct
    
if __name__ == "__main__":
    try:
        print("Input Video Path:")
        input_video_path = input()
        print("Processing...")
        binStr = vidToOct(input_video_path)
        binaryToFile(binStr)
    except KeyboardInterrupt:
        print("\nExecution interrupted by user.")

    # except Exception as ex:
    #     print(f"An unexpected error occurred: {ex}")
