import cv2
import os

def quantize_image(image_path, target_bpp, brightness, contrast):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Calculate the number of levels
    num_levels = 2 ** target_bpp

    # Define the quantization step size
    step_size = 256 // num_levels

    # Perform quantization
    quantized_image = (image // step_size) * step_size

    adjusted_image = cv2.add(cv2.multiply(quantized_image, contrast), brightness)

    # Save the adjusted image
    adjusted_image_path = os.path.join('uploads', f'quantized_{target_bpp}bpp_brightness_{brightness}_contrast_{contrast}.png')
    cv2.imwrite(adjusted_image_path, adjusted_image)

    return adjusted_image_path