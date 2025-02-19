#Internship Details
Company Name: CODTECH IT SOLUTIONS PVT. LTD
intern Name: SANIL SAMIR MHATRE
Intern ID: CT08JTP
Domain: CYBER SECURITY AND ETHICAL HACKING
Batch Duration: JANUARY 20th, 2025 to FEBRUARY 20th, 2025
Mentor Name: NEELA SANTOSH KUMAR

# File Integrity Checker
This is a simple file integrity checker that uses SHA-256 hashes to monitor changes in files. It provides a graphical user interface (GUI) to select files and check their integrity.

## Features
- Calculate SHA-256 hashes of files
- Save and load hash values to/from a JSON file
- Check file integrity and report changes
- Simple GUI to select files and run the checker

## Requirements
- Python 3.6+
- Tkinter (usually included with Python)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/file-integrity-checker.git
    cd file-integrity-checker
    ```
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the script:
    ```sh
    python File\ Integrity\ Checker.py
    ```
2. Use the GUI to select files and check their integrity.

## Project Structure
- `File Integrity Checker.py`: Main script containing the logic and GUI for the file integrity checker.
- [requirements.txt](http://_vscodecontentref_/0): List of dependencies.
- [.gitignore](http://_vscodecontentref_/1): Specifies files and directories to be ignored by Git.
- [hashes.json](http://_vscodecontentref_/2): JSON file to store the hash values of monitored files.

## How It Works
1. **Calculate Hash**: The `calculate_hash` function calculates the SHA-256 hash of a given file. It reads the file in chunks and updates the hash object with each chunk, then returns the hexadecimal digest of the hash.
2. **Save Hashes**: The `save_hashes` function saves the hash data to a JSON file. It opens the file in write mode and uses `json.dump` to write the hash data to the file.
3. **Load Hashes**: The `load_hashes` function loads the hash data from a JSON file. It checks if the file exists using `os.path.exists`, then opens the file in read mode and uses `json.load` to read the hash data from the file. If the file does not exist, it returns an empty dictionary.
4. **Check Integrity**: The `check_integrity` function compares the current hashes of files with the stored hashes. It loads the stored hashes, calculates the current hashes of the selected files, and compares them. It generates a report indicating whether each file has been modified, is unchanged, or is new. It then saves the current hashes to the JSON file and returns the report.
5. **Run File Integrity Checker**: The `run_file_integrity_checker` function is the main GUI function. It opens a file selection dialog for the user to select files to monitor. If no files are selected, it shows an info message. It then runs the integrity check and displays the report in a message box.
6. **Main GUI Setup**: The `main` function sets up the main GUI window with a title and size. It creates two buttons: one to run the file integrity checker and one to end the program. It then starts the Tkinter main loop to keep the GUI running.
By following these steps, the File Integrity Checker provides a simple and effective way to monitor changes in files using SHA-256 hashes and a user-friendly GUI.

## License
This project is licensed under the MIT License.
