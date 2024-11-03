import os
import datetime

# Ask the user for the directory path
dir_path = input("Enter the directory path: ")

# Create a dictionary to store the photo files and their dates
photos = {}

# Loop through all the files in the directory and its subdirectories
for root, dirs, files in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_ext = os.path.splitext(file)[1].lower()

        # Check if the file is an image
        if file_ext in ['.jpg', '.jpeg', '.png', '.MOV', '.mp4', '.mov', '.gif', '.bmp']:
            # Get the date modified timestamp
            mod_time = os.path.getmtime(file_path)

            # Convert the timestamp to a datetime object
            mod_date = datetime.datetime.fromtimestamp(mod_time)

            # Format the date as YYYY-MM
            date_str = f"{mod_date.year}-{mod_date.month:02}"

            # Add the file to the dictionary with the date as the key
            if date_str not in photos:
                photos[date_str] = []
            photos[date_str].append(file_path)

# Sort the photos by date
for date, files in sorted(photos.items()):
    year, month = date.split('-')
    date_path = os.path.join(dir_path, year, f"{month:02}")
    os.makedirs(date_path, exist_ok=True)

    # Move the files to the corresponding year-month directory
    for file in files:
        os.rename(file, os.path.join(date_path, os.path.basename(file)))