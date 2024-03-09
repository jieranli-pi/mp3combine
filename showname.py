import os

def export_file_names(folder_path, output_file):
    # Get the list of files in the specified folder
    files = os.listdir(folder_path)

    # Write the file names to the output file
    with open(output_file, 'w') as file:
        for file_name in files:
            file.write(file_name + '\n')

# Replace 'folder_path' with the path of the folder you want to export
folder_path = '/Users/jieranli/Downloads/delftsemethodegood/groenboek'

# Replace 'output.txt' with the desired output file name
output_file = 'output.txt'

# Call the function to export file names
export_file_names(folder_path, output_file)
