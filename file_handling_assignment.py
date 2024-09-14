# I CREATED A FILE BELOW
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("12345\n")
        file.write("Python is fun!\n")
    print("File created and initial content written successfully.")
except Exception as e:
    print(f"An error occurred during file creation: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("File content after initial write:")
    print(content)
except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending new line 1.\n")
        file.write("Appending new line 2.\n")
        file.write("Appending new line 3.\n")
    print("New lines appended successfully.")
except Exception as e:
    print(f"An error occurred during file appending: {e}")

# File Reading and Display after Appending
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("File content after appending:")
    print(content)
except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
finally:
    print("File handling operations completed.")