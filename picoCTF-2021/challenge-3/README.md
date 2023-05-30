# Python Wrangling

## <u>🎯 Challenge Information</u>

**📚 Challenge Category:**  
General Skills

---
**📝 Challenge Description:**  
Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?

---
**🏅 Challenge Points:**  
10 points

---
**🗓 Challenge Event:**  
picoCTF 2021

## <u> ✍️ Write-up </u>

### 🚀 Introduction
This CTF challenge had me working with a Python decryption script, an encrypted file (flag.txt.en), and a password file (pw.txt). The goal was to run the Python script and decrypt the encrypted file using the password.

---
### 📝 Detailed Steps

1. **Step 1**  
First, I made sure to locate the Python script, the encrypted file, and the password file.

2. **Step 2**  
Then, I copied the password from the password file to my clipboard. On my Mac, I used the cat command in combination with pbcopy in the Terminal:

```bash
cat pw.txt | pbcopy
```

3. **Step 3**  
Next, I ran the Python script from the Terminal. I navigated to the directory that contained the script and executed the following command:

```bash
python ende.py -d flag.txt.en
```

The output revealed the flag

---
### 🎈 Conclusion
This challenge involved running a Python decryption script from the terminal and decrypting a file using a provided password. It was a good exercise in using the terminal, working with file, and carrying out decryption.

---
### 📚 What I Learned / Difficulties
This challenge was a great practice in using Python scripts for decryption, understanding the importance of secure password handling, and dealing with file operations.
