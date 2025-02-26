Image Steganography - Hide Secret Messages in Images
Introduction
This project implements image steganography, a technique to hide secret messages inside images by modifying pixel values. The hidden message can only be retrieved using the correct password, ensuring secure communication.

Features
Hide text inside an image without noticeable changes.
Secure the hidden message with a password.
Retrieve the hidden message only with the correct password.
Works with any standard image format (PNG, JPG, etc.).
Lightweight, fast, and easy to use.
Technologies Used
Programming Language:
Python
Libraries:
OpenCV (cv2): For image processing.
OS: For file handling and opening images.
NumPy: Used internally by OpenCV for pixel manipulation.
Platform:
Windows, Linux, macOS
Hardware Requirements:
Standard PC/Laptop with at least 4GB RAM.
Intel Core i3 or higher (or equivalent AMD).
Minimum 500MB free storage.
Installation & Setup
Install Python (if not installed) from python.org.
Install the required libraries using the following command:
bash
Copy
Edit
pip install opencv-python
Download or clone this repository.
Usage
Place the image (e.g., normalImage.png) in the project folder.
Run the script:
bash
Copy
Edit
python st.py
Enter the secret message and a password for encryption.
The message will be hidden inside the image, and a new encrypted image (encryptedImage.jpg) will be saved.
To decrypt, enter the correct password to reveal the hidden message.
End Users
Students & Researchers
Journalists & Activists
Cybersecurity Enthusiasts
Corporate Professionals
General Users who need secure communication
Future Improvements
Support for longer messages.
Improved encryption techniques for added security.
GUI-based implementation for user-friendly interaction.
Contributors
Shubhangi Sundriyal
License
This project is open-source and free to use for educational purposes.
