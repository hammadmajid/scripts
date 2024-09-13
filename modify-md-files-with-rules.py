# This script reads Markdown files in the given directory, removes lines starting with "status:", and replaces tags
# in the format [[tag]] with #tag, then saves the changes back to the original file.

import os
import re

def modify_markdown_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if line.startswith('status: '):
            line = ''  # Remove the line
        elif line.startswith('tags: '):
            line = re.sub(r'\[\[(.*?)\]\]', r'#\1', line)
        modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

def main(directory):
    for file in os.listdir(directory):
        if file.endswith('.md'):
            file_path = os.path.join(directory, file)
            modify_markdown_file(file_path)

if __name__ == '__main__':
    directory = '/path/to/your/directory'  # Replace with your directory path
    main(directory)
