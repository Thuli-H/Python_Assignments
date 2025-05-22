# Ask the user for the filename to read
filename = input("Enter the name of the file to read: ")

try:
    # Try to open the file for reading
    with open(filename, 'r') as file:
        content = file.read()

    # Modify the content (make everything uppercase as an example)
    modified_content = content.upper()

    # Create a new filename for the output
    new_filename = "modified_" + filename

    # Write the modified content to the new file
    with open(new_filename, 'w') as new_file:
        new_file.write(modified_content)

    print(f"Modified content has been written to '{new_filename}'.")

except FileNotFoundError:
    print("Error: The file was not found. Please check the filename and try again.")
except IOError:
    print("Error: Could not read or write the file. Please check your permissions or disk space.")
