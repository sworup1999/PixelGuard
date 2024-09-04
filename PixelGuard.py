from PIL import Image
import numpy as np
import random

def generate_mask(size, key):
    # Generate a random mask using a key for XOR operations
    np.random.seed(key)
    mask = np.random.randint(0, 256, size=(size[1], size[0], 3), dtype=np.uint8)
    return mask

def encrypt_image(input_path, output_path, key):
    # Open the input image
    img = Image.open(input_path)
    img = img.convert('RGB')
    pixels = np.array(img)
    
    # Generate a mask based on the key
    mask = generate_mask(pixels.shape[1::-1], key)
    
    # Apply XOR operation for encryption
    encrypted_pixels = np.bitwise_xor(pixels, mask)
    
    # Shuffle pixels
    flat_pixels = encrypted_pixels.flatten()
    indices = list(range(len(flat_pixels)))
    random.seed(key)
    random.shuffle(indices)
    
    # Reorder the pixels according to the shuffled indices
    shuffled_pixels = np.array([flat_pixels[i] for i in indices]).reshape(encrypted_pixels.shape)
    
    # Save the encrypted image
    encrypted_img = Image.fromarray(shuffled_pixels)
    encrypted_img.save(output_path)
    print(f"Image encrypted successfully and saved as {output_path}.")

def decrypt_image(input_path, output_path, key):
    # Open the encrypted image
    img = Image.open(input_path)
    img = img.convert('RGB')
    encrypted_pixels = np.array(img)
    
    # Generate the same mask based on the key
    mask = generate_mask(encrypted_pixels.shape[1::-1], key)
    
    # Unshuffle pixels
    flat_pixels = encrypted_pixels.flatten()
    indices = list(range(len(flat_pixels)))
    random.seed(key)
    shuffled_indices = indices.copy()
    random.shuffle(shuffled_indices)
    
    # Create a reverse index map for unshuffling
    reverse_indices = [shuffled_indices.index(i) for i in indices]
    unshuffled_pixels = np.array([flat_pixels[i] for i in reverse_indices]).reshape(encrypted_pixels.shape)
    
    # Reverse the XOR operation
    decrypted_pixels = np.bitwise_xor(unshuffled_pixels, mask)
    
    # Save the decrypted image
    decrypted_img = Image.fromarray(decrypted_pixels)
    decrypted_img.save(output_path)
    print(f"Image decrypted successfully and saved as {output_path}.")

if __name__ == "__main__":
    action = input("Do you want to (e)ncrypt or (d)ecrypt the image? ").lower()
    input_path = input("Enter the path to the input image: ")
    output_path = input("Enter the path to save the output image: ")
    key = int(input("Enter the encryption/decryption key: "))
    
    if action == 'e':
        encrypt_image(input_path, output_path, key)
    elif action == 'd':
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
