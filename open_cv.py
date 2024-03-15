import cv2
import numpy as np

# Load your image
image = cv2.imread('normal.png')

# Define starting and ending positions
start_position = (0, 0)
end_position = (300, 300)

# Determine the maximum movement range
max_range_x = max(start_position[0], end_position[0]) + image.shape[1]
max_range_y = max(start_position[1], end_position[1]) + image.shape[0]

# Create a canvas large enough to accommodate the entire movement range
canvas = np.zeros((max_range_y, max_range_x, 3), dtype=np.uint8)

# Define number of frames
num_frames = 10


# Define easing function (quadratic ease-in-out)
def easeInOutQuad(t):
    return t * t * (3 - 2 * t)


# Loop through frames
for i in range(num_frames):
    # Calculate current time normalized between 0 and 1
    t = i / (num_frames - 1)

    # Apply easing function to time
    eased_t = easeInOutQuad(t)

    # Calculate current position based on eased time
    current_x = int(start_position[0] + (end_position[0] - start_position[0]) * eased_t)
    current_y = int(start_position[1] + (end_position[1] - start_position[1]) * eased_t)

    # Clear the canvas
    canvas.fill(0)

    # Add the image to the canvas at the current position
    canvas[current_y:current_y + image.shape[0], current_x:current_x + image.shape[1]] = image

    # Display the frame
    cv2.imshow('Moving Image', canvas)
    cv2.waitKey(30)  # Adjust waitKey duration for desired frame rate
    # Set window to fullscreen
    cv2.namedWindow('Moving Image')
    cv2.setWindowProperty('Moving Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2
# import os
#
#
# def display_images(image_list, transition_time=100, fps=50):
#     """Display images from a list with smooth transitions.
#
#     Args:
#         image_list (list): List of NumPy arrays representing the images.
#         transition_time (float, optional): Time duration of the transition between images (in seconds). Defaults to 1.0.
#         fps (int, optional): Frames per second for displaying images. Defaults to 30.
#     """
#     # Calculate number of frames for the transition
#     num_transition_frames = int(transition_time * fps)
#     while True:
#         # Iterate over pairs of consecutive images
#         for i in range(len(image_list) - 1):
#             # Extract the current and next images
#             current_image = image_list[i]
#             next_image = image_list[i + 1]
#
#             # Perform smooth transition between images
#             for j in range(num_transition_frames + 1):
#                 alpha = j / num_transition_frames
#                 blended_image = cv2.addWeighted(current_image, 1 - alpha, next_image, alpha, 0)
#                 cv2.imshow('Smooth Transition', blended_image)
#                 cv2.waitKey(1)
#
#     # Display the last image without transition
#     cv2.imshow('Smooth Transition', image_list[-1])
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#
# # Example usage
# image_names = ["happy.png", 'angry.png', 'normal.png']  # List of image names
# image_paths = [os.path.join(os.getcwd(), name) for name in image_names]  # Convert image names to absolute paths
# images = [cv2.imread(path) for path in image_paths]  # Load images
#
# # Display images with a smooth transition
# display_images(images, transition_time=1.0, fps=30)
#
