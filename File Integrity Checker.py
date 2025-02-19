import hashlib
import os
import json
from tkinter import Tk, filedialog, messagebox, Button


# Function to calculate the hash of a file
def calculate_hash(file_path):
    """Calculates the SHA-256 hash of a given file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):  # Read file in chunks
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None


# Function to save hash values to a JSON file
def save_hashes(hash_file, hash_data):
    """Save the hash data to a JSON file."""
    with open(hash_file, "w") as file:
        json.dump(hash_data, file)


# Function to load hash values from a JSON file
def load_hashes(hash_file):
    """Load the hash data from a JSON file."""
    if os.path.exists(hash_file):
        with open(hash_file, "r") as file:
            return json.load(file)
    return {}


# Function to check file integrity
def check_integrity(file_list, hash_file="hashes.json"):
    """Compares current hashes of files with stored hashes."""
    stored_hashes = load_hashes(hash_file)
    current_hashes = {}
    report = []

    for file_path in file_list:
        current_hash = calculate_hash(file_path)
        if current_hash is None:
            continue

        if file_path in stored_hashes:
            if current_hash != stored_hashes[file_path]:
                report.append(f"[ALERT] File modified: {file_path}")
            else:
                report.append(f"[OK] File unchanged: {file_path}")
        else:
            report.append(f"[NEW] File not tracked yet: {file_path}")

        current_hashes[file_path] = current_hash

    save_hashes(hash_file, current_hashes)
    report.append("\nHash database updated.")
    return report


# GUI function to select files and run the checker
def run_file_integrity_checker():
    # Open file selection dialog
    file_paths = filedialog.askopenfilenames(title="Select files to monitor")

    if not file_paths:
        messagebox.showinfo("No Files Selected", "Please select at least one file to monitor.")
        return

    # Run the integrity check
    report = check_integrity(file_paths)

    # Display the report
    messagebox.showinfo("File Integrity Report", "\n".join(report))


# Main GUI setup
def main():
    root = Tk()
    root.title("File Integrity Checker")
    root.geometry("400x200")

    # Create Check button
    check_button = Button(root, text="Check", command=run_file_integrity_checker)
    check_button.pack(pady=20)

    # Create End button
    end_button = Button(root, text="End", command=root.quit)
    end_button.pack(pady=20)

    # Keep the GUI running
    root.mainloop()


if __name__ == "__main__":
     main()