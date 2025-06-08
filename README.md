  ● Overview

DataEncoder is a simple Python encryption tool that demonstrates custom character-based data encryption. It uses a user-provided key along with an internal fixed key to securely transform any text data.

✨ Features

Symmetric encryption (same key used for encryption and decryption)

Custom character transformation logic

Includes base64 encoding for safe display or storage

Easy to use with any text-based data


🚀 How It Works

The core logic lies in character code manipulation:

Each character from the input text is modified by adding or subtracting the Unicode values of a character from:

1. The user-provided key


2. An internal fixed key (Ne&1Ta#Jn_me)



The result is a transformed character, wrapping around using % 256.

Base64 is used to safely encode and decode the encrypted output for printing.


✅ Requirements

This project requires:

Python 3.6+

No external dependencies (uses only built-in modules)


Built-in modules used:

base64
```pip install base64``` Write that On CMD

📜 License

This project is licensed under the MIT License.
