# SmileENC
Mathematical Encryption system called smile to communicate anonymously without the government knowing.

Secure Messaging Encryption System

This encryption system is designed to provide enhanced security for confidential communications between users. It consists of three Python scripts: smile.py, sentenceENC.py, and sentenceDEC.py.

Encryption Process:

Use sentenceENC.py: This script takes a sentence as input and converts it into a series of numbers using a unique encryption algorithm. The output is a sequence of numbers, forming the main encryption key (e.g., 11121221221).

Use smile.py (Optional): smile.py can further encrypt the main key using customizable layers of encryption with additional keys. As a result, the main key becomes virtually un-decryptable without the specific keys used for encryption. Sharing this encrypted main key with trusted recipients poses no risk to the security of the messages.

Decryption Process:

Decryption with smile.py: If smile.py was used for encryption, the recipients should use the script to decrypt the main key using the additional keys shared through netcat. Only authorized users with the correct keys can obtain the original main key, ensuring secure message decryption.

Decryption with sentenceDEC.py: If only sentenceENC.py was used for encryption, sentenceDEC.py can be used to decrypt the original sentence using the main encryption key (11121221221). The decrypted message will be revealed in plain text.

Security Recommendations:

The main encryption key (11121221221) is crucial for decryption. Protect it at all costs, as unauthorized access to this key would compromise message security.

For increased security, use smile.py to apply multiple layers of encryption with additional keys. Share these keys using netcat with trusted individuals to ensure secure communications.

When using smile.py, the messages will appear as a sequence of numbers with a key, like this: (encoded_message, key). The key used to encrypt the message can be decrypted using sentenceDEC.py.

Usage:

On Unix systems (e.g., Linux, macOS), run the encryption/decryption scripts with Python 3 using the following commands:

Copy code
python3 script_name.py
On Windows, run the encryption/decryption scripts using Python 3 in the terminal:

Copy code
python3 script_name.py
Security Note:
Ensure you only share keys and encrypted messages with trusted parties. Misusing the encryption system for malicious purposes is strictly discouraged. Always use encryption responsibly and ethically.


Overview:
Anonymous Secure Chat is a powerful and user-friendly encryption tool designed to ensure secure and private communication between users. This open-source project empowers individuals to have confidential conversations without the fear of unauthorized access to their sensitive information. With customizable layers of encryption, the system provides robust protection against brute force attacks and unauthorized decryption attempts.

Use: to use this tool the main tool named (smile.py) u need to encrypt the sentences with the other tools that are below and to decrypt the encrypted messages someone sent please use the decryption tool inside the smile.py (main script) the encryption system is impossible to decrypt due to the large numbers it creates also the key created in the output the script is safe to use if u have any issues please report them. and ill try to fix them.

Needed: if u guys repost this tool please make sure to give credits to the owner or so called the creator, thank you. (give credits by putting: Okayet/Smile)

Key Features:

Layered Encryption: The system allows users to apply multiple layers of encryption, making it virtually impossible for unauthorized parties to break through the encryption barriers. Users can freely choose the encryption algorithms and keys to create their unique security configurations.

End-to-End Encryption: All communications are end-to-end encrypted, meaning the messages are only accessible to the intended recipients. The system ensures that even the service provider cannot access the contents of the messages exchanged between users.

Perfect Forward Secrecy: Each conversation session generates unique encryption keys, ensuring that compromising one session does not jeopardize the security of past or future communications.

User Anonymity: The system does not require users to disclose their real identities or personal information. Instead, users can communicate using anonymous handles or pseudonyms.

Message Deletion: Users have the option to set messages to self-destruct after a specific period, further protecting their privacy and reducing the risk of data exposure.

Open-Source: The entire codebase is open-source, encouraging transparency and peer review to identify and fix potential security vulnerabilities.

Disclaimer:
While this encryption system provides robust security measures, it is essential to remember that no encryption method is entirely foolproof. Users should exercise caution and avoid sharing sensitive information with untrusted parties. The system should not be used for malicious purposes or to encrypt data belonging to others without their consent.

Contributing:
Contributions to this project are highly appreciated! Developers can help improve the encryption algorithms, UI/UX, documentation, or report and fix bugs. All contributors are expected to adhere to the project's code of conduct and prioritize user privacy and security.
if u have any ideas write it down on fix/bug section so i can imporve the script by ur needs.

Disclaimer:
Please use this encryption system responsibly and ethically. The project maintainers and contributors disclaim any responsibility for the misuse or illegal use of this tool by any individual or entity.

LIcense: Apache 2.0
