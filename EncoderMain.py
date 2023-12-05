from mutagen.mp4 import MP4, MP4Cover

def write_metadata(input_bytes, output_file):
    # Create an MP4 instance
    mp4_file = MP4()

    # Set the metadata tag with the input bytes
    mp4_file["\xa9day"] = [input_bytes]

    # Save the MP4 file with the metadata
    mp4_file.save(output_file)

# Example usage
input_bytes = b'Your string of bytes here'
output_file = 'output.mp4'

write_metadata(input_bytes, output_file)
