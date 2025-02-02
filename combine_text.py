import os

# Path to the folder containing the .txt files
folder_path = 'Plato_Books_Cleaned'

# Name of the output file
output_file = 'Plato_Books_combined.txt'

# Open the output file in write mode
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            # Open each text file and write its content to the output file
            with open(file_path, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write('\n')  # Add a newline between files (optional)
