import cv2
import matplotlib.pyplot as plt
def plot_image(image):
# Convert BGR to RGB color format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Create a new figure and plot the image
    plt.figure()
    plt.imshow(image)
    plt.axis('off')
    plt.show()
def split_image(image_path):
# Read the image using OpenCV
    image = cv2.imread(image_path)
# Get the dimensions of the image
    height, width, _ = image.shape
# Calculate the midpoint coordinates
    mid_x = width // 2
    mid_y = height // 2
# Split the image into quadrants
    up = image[0:mid_y, 0:width]
    down = image[mid_y:height, 0:width]
    left = image[0:height, 0:mid_x]
    right = image[0:height, mid_x:width]
# Plot each quadrant
    plot_image(image)
    plot_image(up)
    plot_image(down)
    plot_image(left)
    plot_image(right)
# Example usage
image_path = "i2.jpg"
split_image(image_path)