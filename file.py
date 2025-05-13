def read_and_modify_file():
    # Ask user for the input filename
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Define output filename
        output_filename = "modified_" + input_filename

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to: {output_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()
