from PIL import Image
# import matplotlib.pyplot as plt

def generate_mirror_image(input_image_path):
    # Open the input image
    with Image.open(input_image_path) as img:
        # Create a new image with the same size
        mirror_img = Image.new('RGB', img.size)

        # Iterate over each pixel in the input image
        for x in range(img.width):
            for y in range(img.height):
                # Get the pixel value from the input image
                pixel = img.getpixel((x, y))

                # Set the pixel value in the mirror image
                mirror_x = img.width - 1 - x
                mirror_img.putpixel((mirror_x, y), pixel)

        mirror_img.show()

        # # Display the mirror image
        # plt.figure(figsize=(8, 8))
        # plt.subplot(1, 2, 1)
        # plt.imshow(img)
        # plt.title('Original Image')

        # plt.subplot(1, 2, 2)
        # plt.imshow(mirror_img)
        # plt.title('Mirror Image')

        # plt.show()

# Example usage
input_image_path = r'C:\Users\HP\Desktop\Untitled10.png'
generate_mirror_image(input_image_path)