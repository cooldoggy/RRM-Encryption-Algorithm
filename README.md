# RRM
## A Symmetric Hashing Algorithm
This Python script provides a simple encryption and decryption tool based on a matrix approach. 
It utilizes SHA-256 hashing to create the key and implements a encryption/decryption 
algorithm. It includes a tutorial option for getting started.

Authors: 
Jean-Luc Robitaille
Erin Rodriguez

## Features

*   **Encryption (-e):** Encrypts a plaintext string using a SHA-256 hashed password.
*   **Decryption (-d):** Decrypts ciphertext using a SHA-256 hashed password.
*   **Tutorial (-r):**  Displays a tutorial explaining the usage and basic concepts.
*   **SHA-256 Hashing:**  Uses SHA-256 to derive the key from the password.
*   **Matrix Based Encryption:**  Employs a simplified matrix-like approach.

## Prerequisites

*   Python 3.6 or higher

## Installation

No installation is required.  Just save the script as `main.py` and execute it from your 
terminal.

## Usage

The script takes the following arguments:

```bash
python main.py [flag] [plaintext] [password] [encryption rounds]
```

**Flags:**

*   `-e` (Encryption): Encrypts the provided plaintext using the given password and encryption 
rounds.
*   `-d` (Decryption): Decrypts the provided ciphertext using the given password and encryption 
rounds.
*   `-r` (Tutorial):  Displays a tutorial explaining the script's usage.

**Arguments:**

*   `[plaintext]`: The 8-character plaintext string to be encrypted or decrypted.
*   `[password]`: The password used for encryption/decryption.
*   `[encryption rounds]`: The number of rounds to perform during encryption/decryption (default 
is 2048).

**Examples:**

1.  **Encryption:**

    ```bash
    python main.py -e hello password 2048
    ```

    This will encrypt the plaintext "hello" using the password "password" with 2048 rounds. The 
output will be the encrypted ciphertext.

2.  **Decryption:**

    ```bash
    python main.py -d [ciphertext] password 2048
    ```

    This will decrypt the ciphertext to the original plaintext.

3.  **Tutorial:**

    ```bash
    python main.py -r
    ```

    This will display a tutorial explaining how to use the script.
    
