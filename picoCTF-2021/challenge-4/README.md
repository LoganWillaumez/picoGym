# Wave a Flag

## <u>🎯 Challenge Information</u>

**📚 Challenge Category:**  
General Skills

---
**📝 Challenge Description:**  
Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

---
**🏅 Challenge Points:**  
10 points

---
**🗓 Challenge Event:**  
picoCTF 2021

## <u> ✍️ Write-up </u>

### 🚀 Introduction
This challenge had me invoking help flags with a given binary program. The task was to find some useful information hidden in the help section of the program.

---
### 📝 Detailed Steps

1. **Step 1**  
Firstly, I attempted to run the provided binary on my local Mac system. However, the binary was incompatible with my system.

2. **Step 2**  
Given the incompatibility, I decided to use the webshell provided by the CTF platform (in this case, picoCTF). In the webshell, I navigated to the directory containing the binary file named 'warm'.

3. **Step 3**  
I used the chmod command to make the binary executable:

```bash
chmod +x ./warm
```
4. **Step 4**  

I then executed the binary with the -h flag to invoke the help information:

```bash
./warm -h
```

The output revealed the flag: 

---
### 🎈 Conclusion
This challenge involved invoking the help flags of a binary to uncover hidden information. It served as a useful exercise in understanding and working with binary files, employing command-line tools, and leveraging the help flags.

---
### 📚 What I Learned / Difficulties
Through this challenge, I learned about handling binary files, using help flags effectively, and troubleshooting compatibility issues. I also got to experience the power of webshells in overcoming local system constraints.
