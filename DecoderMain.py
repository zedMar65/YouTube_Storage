from Core.FIleOct import octToFile
from Core.Video import vidToOct
    
if __name__ == "__main__":
    try:
        print("Input Video Path:")
        input_video_path = input()
        print("Processing...")
        oct_str = vidToOct(input_video_path)
        octToFile(oct_str)
    except KeyboardInterrupt:
        print("\nExecution interrupted by user.")

    # except Exception as ex:
    #     print(f"An unexpected error occurred: {ex}")
