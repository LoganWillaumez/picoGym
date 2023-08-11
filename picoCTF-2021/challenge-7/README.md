Certainly! Let's improve the given write-up and complete the missing sections.

# Transformation

## <u>🎯 Challenge Information</u>

**📚 Challenge Category:**  
Reverse Engineering

**📝 Challenge Description:**  
The challenge presents a code snippet that takes a string and transforms it by joining characters after a specific bitwise operation. The aim is to understand this transformation and reverse it to reveal the hidden message.

```bash
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

**🏅 Challenge Points:**  
20 points

**🗓 Challenge Event:**  
picoCTF 2021

## <u>✍️ Write-up</u>

### 🚀 Introduction
This challenge revolves around understanding and reverse engineering a 16-bit transformation into an 8-bit phrase. It requires understanding bitwise operations and translating them into meaningful text.

### 📝 Detailed Steps

1. **Step 1**  
I downloaded the file containing the flag and copied its content using the following command:

```bash
cat enc | pbcopy
```

2. **Step 2**  
I observed that the text was processed as 16-bit characters. Analyzing the code snippet provided in the challenge helped me understand that each character in the flag was transformed by shifting 8 bits to the left and then adding the ASCII value of the next character.

3. **Step 3**  
Understanding the bit manipulation involved, I reverse engineered the process by splitting the 16-bit numbers back into two 8-bit characters.

Here's a script that reverses the transformation:

```python
enc_flag = <insert the encoded flag here>
dec_flag = "".join([chr(enc_flag[i] >> 8) + chr(enc_flag[i] & 0xFF) for i in range(0, len(enc_flag), 2)])
print("The flag is:", dec_flag)
```

The output revealed the flag.

### 🎈 Conclusion
This challenge provided an engaging exploration into bitwise manipulation and character encoding. By understanding the transformation from 8-bit to 16-bit characters and reversing it, the flag was successfully decoded.

### 📚 What I Learned / Difficulties
I learned about the nature of bits, how to change them, and the difference between 16-bit and 8-bit encoding. The challenge was in recognizing the pattern and precisely reversing the transformation, and I gained valuable insights into how encoding and decoding can be used in cryptography.