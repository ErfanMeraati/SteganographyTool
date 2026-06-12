# steganography_tool.py
import sys
from PIL import Image

DELIMITER = "<<<END>>>"

def encode(image_path: str, message: str, output_path: str):
    img = Image.open(image_path).convert("RGB")
    pixels = list(img.getdata())
    
    binary = ''.join(f'{ord(c):08b}' for c in message + DELIMITER)
    
    if len(binary) > len(pixels) * 3:
        print("❌ Error: Message too long for this image.")
        return
    
    new_pixels = []
    idx = 0
    for r, g, b in pixels:
        channels = [r, g, b]
        for i in range(3):
            if idx < len(binary):
                channels[i] = (channels[i] & ~1) | int(binary[idx])
                idx += 1
        new_pixels.append(tuple(channels))
    
    out = img.copy()
    out.putdata(new_pixels)
    out.save(output_path)
    print(f"✅ Message hidden in: {output_path}")

def decode(image_path: str):
    img = Image.open(image_path).convert("RGB")
    pixels = list(img.getdata())
    
    bits = []
    for r, g, b in pixels:
        bits += [r & 1, g & 1, b & 1]
    
    chars = []
    for i in range(0, len(bits) - 7, 8):
        char = chr(int(''.join(map(str, bits[i:i+8])), 2))
        chars.append(char)
        if ''.join(chars[-len(DELIMITER):]) == DELIMITER:
            print("🔍 Hidden message:")
            print(''.join(chars[:-len(DELIMITER)]))
            return
    
    print("❌ No hidden message found.")

def main():
    print("=== Steganography Tool ===\n")
    print("1. Hide message in image")
    print("2. Extract message from image")
    
    choice = input("\nChoice (1/2): ").strip()
    
    if choice == "1":
        img = input("Image path (PNG): ").strip().strip('"')
        msg = input("Message to hide: ").strip()
        out = input("Output path (PNG): ").strip().strip('"')
        encode(img, msg, out)
    
    elif choice == "2":
        img = input("Image path (PNG): ").strip().strip('"')
        decode(img)
    
    else:
        print("Invalid choice.")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
