# Information

## <u>🎯 Challenge Information</u>

**📚 Challenge Category:**  
Forensics

---
**📝 Challenge Description:**  
Files can always be changed in a secret way. Can you find the flag? cat.jpg

---
**🏅 Challenge Points:**  
10 points

---
**🗓 Challenge Event:**  
picoCTF 2021

## <u> ✍️ Write-up </u>

### 🚀 Introduction
This challenge focused on the extraction of hidden information from an image file. It involved understanding and using the Exif metadata in the JPEG image and utilizing basic encoding techniques to uncover the hidden flag.

---
### 📝 Detailed Steps

1. **Step 1**  
I first downloaded the provided image file cat.jpg and inspected its Exif metadata using the exiftool command:

```bash
exiftool cat.jpg
```

2. **Step 2**  
Upon inspecting the metadata output, I noticed a suspicious base64 string under the License field.

3. **Step 3**  
Recognizing the base64 string, I proceeded to decode it.

The output revealed the flag: 

---
### 🎈 Conclusion
This challenge served as a good introduction to the concept of steganography, where secret data can be hidden within the metadata of image files. It was also a practical exercise in using command-line tools for metadata inspection and base64 decoding.

---
### 📚 What I Learned / Difficulties
Through this challenge, I learned about the use of Exif metadata in JPEG images and the possibility of hiding data within it. I also reinforced my skills in recognizing and decoding base64 encoded strings.
