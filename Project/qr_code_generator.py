import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

if __name__ == "__main__":
    data = input("Enter the data to be encoded in the QR code: ")
    file_name = input("Enter the file name for the QR code image with the file extension (.png,.jpg,..) : ")
    generate_qr_code(data, file_name)
    print("QR code generated successfully!")

"""
This Python script generates a QR code image based on user input using the `qrcode` library. Let's go through the script step by step:

1. **Importing the `qrcode` Module**:
   ```python
   import qrcode
   ```
   This line imports the `qrcode` module, which provides functionality for generating QR codes.

2. **Defining the `generate_qr_code` Function**:
   ```python
   def generate_qr_code(data, file_name):
       qr = qrcode.QRCode(version=1, box_size=10, border=5)
       qr.add_data(data)
       qr.make(fit=True)

       img = qr.make_image(fill_color="black", back_color="white")
       img.save(file_name)
   ```
   - This function takes two parameters: `data` (the information to be encoded in the QR code) and `file_name` (the name of the file to save the QR code image).
   - It creates a QRCode object with specified parameters such as version, box size, and border.
   - The `add_data` method adds the provided data to the QR code.
   - The `make` method generates the QR code, with `fit=True` ensuring that the QR code adjusts its size according to the amount of data provided.
   - It then creates an image of the QR code using the `make_image` method, specifying the fill color (black) and background color (white).
   - Finally, it saves the generated QR code image to a file using the specified file name.

3. **Executing the `generate_qr_code` Function**:
   ```python
   if __name__ == "__main__":
       data = input("Enter the data to be encoded in the QR code: ")
       file_name = input("Enter the file name for the QR code image with the file extension (.png, .jpg, etc.): ")
       generate_qr_code(data, file_name)
       print("QR code generated successfully!")
   ```
   - This conditional statement checks if the script is being run as the main program (`__name__` equals `"__main__"`).
   - If it is, it prompts the user to enter the data to be encoded in the QR code and the file name for the QR code image.
   - It then calls the `generate_qr_code` function with the provided data and file name, generating the QR code image.
   - Finally, it prints a message indicating that the QR code has been generated successfully.

This script provides a simple way for users to generate QR code images based on their input data, allowing them to encode various types of information into QR codes.
"""
