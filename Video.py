def create_video(hex_string, output_video_path):
    import cv2
    import numpy as np
    # Calculate the dimensions of the final image (720x1080)
    image_width = 1080
    image_height = 720
    block_size = 4
    fps = 10

    # Calculate the number of blocks needed based on the length of the hex string
    num_blocks = len(hex_string) // 3
    blocks_per_row = image_width // block_size

    # Calculate the maximum number of blocks per image
    max_blocks_per_image = (image_width // block_size) * (image_height // block_size)

    # Counter for output file naming
    output_counter = 0

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (image_width, image_height))

    for i in range(0, num_blocks, max_blocks_per_image):
        # Create an array of RGB values for all blocks and fill with white
        all_blocks = np.full((image_height, image_width, 3), 255, dtype=np.uint8)

        # Paint each 4x4 block with the hex values sequentially
        for j in range(min(max_blocks_per_image, num_blocks - i)):
            r_value = int(hex_string[(i + j) * 3], 16) * 15
            g_value = int(hex_string[(i + j) * 3 + 1], 16) * 15
            b_value = int(hex_string[(i + j) * 3 + 2], 16) * 15

            row = j // blocks_per_row
            col = j % blocks_per_row

            # Calculate the coordinates for each block in the image
            block_start_x = col * block_size
            block_end_x = (col + 1) * block_size
            block_start_y = row * block_size
            block_end_y = (row + 1) * block_size

            # Paint the block with the RGB values
            all_blocks[block_start_y:block_end_y, block_start_x:block_end_x, :] = [r_value, g_value, b_value]

        # Convert the NumPy array to BGR format (OpenCV's default)
        bgr_image = cv2.cvtColor(all_blocks, cv2.COLOR_RGB2BGR)

        # Write the frame to the video file
        video_writer.write(bgr_image)

        # Increment the output counter
        output_counter += 1

    # Release the video writer
    video_writer.release()