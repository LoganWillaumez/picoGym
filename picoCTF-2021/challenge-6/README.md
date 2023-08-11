# Nice netcat...

## <u>🎯 Challenge Information</u>

**📚 Challenge Category:**  
General Skills
---
**📝 Challenge Description:**  
There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 21135, but it doesn't speak English...

---
**🏅 Challenge Points:**  
15 points

---
**🗓 Challenge Event:**  
picoCTF 2021

## <u> ✍️ Write-up </u>

### 🚀 Introduction
This challenge focused on the decoding of random number received.

---
### 📝 Detailed Steps

1. **Step 1**  
I first launch the command given to the description of the CTF

```bash
nc mercury.picoctf.net 21135
```

2. **Step 2**  
It give me a lot of numbers, I thinked about Ascii letters and tried one of it to be sure
3. **Step 3**  
To decode these numbers into a meaningful string, I crafted a Python script that handles the connection, data fetching, and decoding. A detailed breakdown can be found within the script file placed in the same directory as this challenge:

---
### 🎈 Conclusion
This challenge served as a good introduction to the concept of steganography, where secret data can be hidden within the metadata of image files. It was also a practical exercise in using command-line tools for metadata inspection and base64 decoding.

---
### 📚 What I Learned / Difficulties
Through this challenge, I learned about the use of Exif metadata in JPEG images and the possibility of hiding data within it. I also reinforced my skills in recognizing and decoding base64 encoded strings.
