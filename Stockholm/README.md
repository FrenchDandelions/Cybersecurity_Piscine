# **Stockholm Ransomware (Educational Purpose Only)**  

⚠ **WARNING:**  
This program is **malware**, designed **strictly for educational purposes**. Do **not** use, modify, or redistribute this program for **malicious activities**. Unauthorized use of ransomware is illegal and punishable by law.  

## **Version & Release Date**  
- **Version:** 1.0  
- **Release Date:** March 2024  

## **Overview**  
Stockholm is a ransomware simulation that encrypts files **inside the `infection/` directory** located in the user's home directory. The encryption targets **files with extensions previously affected by WannaCry**.  

### **Functionality**  
- **Encryption:** Affected files are renamed with a `.ft` extension (unless they already have one).  
- **Decryption:** Use the `-r` option along with the provided **key** to restore encrypted files.  
- **Silent Mode:** The `-s` option runs the program without producing any output.  
- **Help Menu:** Use `-h` to display usage instructions.  
- **Version Display:** Use `-v` to check the program version.  
- **Key Management:** The decryption key is displayed upon execution and saved in a `key.txt` file.  

## **Setup & Execution**  
This program **must** be run inside a specific **containerized environment**.  

### **Installation Steps:**  
1. **Build the container:**  
   ```bash
   make
   ```  
2. **Enter the container:**  
   ```bash
   make enter
   ```  
3. **Run the program using the following command:**  
   ```bash
   ./stockholm [-h | -v | -r {key} | -s]
   ```  
   - `-h` or `-help` → Show help menu  
   - `-v` or `-version` → Display version information  
   - `-r {key}` or `-reverse {key}` → Decrypt files using the provided key  
   - `-s` or `-silent` → Run in silent mode without output  

## **Author & Contact**  
- **Author:** thole  
- **GitHub:** [FrenchDandelions](https://github.com/FrenchDandelions)  