import os
import re

# Automatically set the root directory to the directory where the script is located
root_directory = os.path.dirname(os.path.abspath(__file__))

# Prompt for the new version number
version = input("Enter the new version number: ")

# Regex patterns for finding CSS, JS links, and the title tag
css_pattern = re.compile(r'(href=".*?\.css)(\?v=.*?)?"')
js_pattern = re.compile(r'(src=".*?\.js)(\?v=.*?)?"')
title_pattern = re.compile(r'(<title>.*?v)(\d+\.\d+\.\d+)(</title>)')

# Traverse all files in root directory and subdirectories
for subdir, _, files in os.walk(root_directory):
    for filename in files:
        if filename.endswith('.html'):
            file_path = os.path.join(subdir, filename)

            # Read the content of the HTML file with UTF-8 encoding
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Replace or add version numbers for CSS and JS links
            updated_content = re.sub(css_pattern, r'\1?' + version + '"', content)
            updated_content = re.sub(js_pattern, r'\1?' + version + '"', updated_content)

            # Update the version number in the title tag
            updated_content = re.sub(title_pattern, r'\g<1>' + version[1:] + r'\g<3>', updated_content)

            # Write the updated content back to the file with UTF-8 encoding
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)

print("Version numbers updated successfully in all HTML files.")
