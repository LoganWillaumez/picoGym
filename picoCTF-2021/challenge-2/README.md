# Mod 26

## <u>🎯 Challenge Information</u>

**📚 Challenge Category:**  
Cryptography

---
**📝 Challenge Description:**  
Cryptography can be easy, do you know what ROT13 is? cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}

---
**🏅 Challenge Points:**  
10 points

---
**🗓 Challenge Event:**  
picoCTF 2021

## <u> ✍️ Write-up </u>

### 🚀 Introduction
In this Capture The Flag (CTF) challenge, we're introduced to a basic ROT13 cipher, a form of Caesar cipher, and command-line interface (CLI) decoding tools.

---
### 📝 Detailed Steps

1. **Step 1**  
To decrypt the ROT13-encoded flag, I utilize the 'tr' command in the Unix CLI. The command is as follows:

```bash
echo "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

This command effectively "shifts" each letter in the input string by 13 positions in the alphabet, wrapping around from 'z' to 'a' or 'Z' to 'A' as necessary.

The output revealed the flag

---
### 🎈 Conclusion
This challenge gave a hands-on introduction to CTF competitions, employing the ROT13 cipher and the Unix 'tr' command. Both elements are integral to understanding cryptographic puzzles commonly encountered in CTFs.

---
### 📚 What I Learned / Difficulties
Through this challenge, I reinforced my skills in using command-line utilities and understanding basic cryptographic techniques. 
