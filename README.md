# Educational Purpose: Showcasing the Vulnerability of Simple Password using Brute force script.

## Background
Simple, non-complex passwords pose a significant security risk, as they can be easily guessed or cracked using brute force methods. 
While hashing passwords using algorithms like SHA-256 adds a layer of security by obscuring the actual password, it’s crucial to understand that this does not render the passwords invulnerable to cracking techniques.

# Overview

This Python script demonstrates a basic brute force password cracking technique. It generates all possible combinations of a specified set of characters up to a certain length and then attempts to crack given hashed passwords by comparing the generated hashes against the target hashes. It uses SHA-256 for hashing passwords.

Note: This script is for educational purposes only and to showcase my skills in cybersecurity. Please use it responsibly and only on systems you have permission to test.

# Features

	•	SHA-256 Hashing: I utilise SHA-256, a cryptographic hash function, for hashing passwords.
	•	Password Generation: I dynamically generates all possible password combinations based on a predefined character set and password length.
	•	Time Tracking: I measure the time taken to crack each password.


# Example Output

```
Generating Cartesian products of characters in the char variable
Successfully generated 916132832x passwords
Password cracked: hello (Hash: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c85ffa72401a3787db6a3d3bb)
Time taken: 12.34 seconds
All passwords cracked.
Time taken to guess all passwords: 45.67 seconds
```

# Take-Away Lessons

This project leverages SHA-256 to hash and then crack simple passwords, illustrating that:

	•	The efficacy of brute force attacks depends not on the strength of the hashing algorithm but on the complexity of the passwords themselves.
	• Layered Security Approaches: Combining hashing with other security measures, such as salt (a random value added to the password before hashing), to further complicate cracking attempts.

# Disclaimer

This tool is provided for educational use only. Any misuse of this software is not the responsibility of the author. Always ensure you have explicit permission to test password strength on any system you use this tool with.
