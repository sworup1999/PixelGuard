# PixelGuard: Simple Image Encryption Tool
PixelGuard is a lightweight image encryption tool that secures images through pixel manipulation techniques. This tool allows users to encrypt and decrypt images by altering pixel values with basic arithmetic operations, such as addition or subtraction using a key. It's perfect for educational purposes and introductory projects on image processing and encryption.

# Features:
Encrypt Images: Secure your images by adding a key value to each pixel.
Decrypt Images: Restore your images by reversing the encryption operation.
Simple and Lightweight: Easy to use with a minimalistic approach to image encryption.
How It Works:
# Encryption: Adjusts pixel values with a specified key, keeping values within valid RGB ranges.
Decryption: Reverses the pixel value adjustment using the same key to retrieve the original image.
Usage:
# Clone the repository.
Install required dependencies with pip install Pillow.
Use the encrypt_image() function to encrypt your image.
Use the decrypt_image() function to decrypt your encrypted image.
Example Code:
# Encrypt an image
encrypt_image('input_image.png', key=50)

# Decrypt the image
decrypt_image('encrypted_image.png', key=50)
