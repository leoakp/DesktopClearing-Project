# Moving image files (supporting extensions: .png, .jpeg, and .jpg) from Desktop folder to a sub folder on the desktop (.../Screenshots_2024/)
#
# Importing os module
import os

# Importing shutil module
import shutil

def main():
    # Get the list of all files in the specific folder.
    source_path = "/Users/leopoldakpabio/Desktop/"
    destination_path = "/Users/leopoldakpabio/Desktop/Screenshots_2024/"

    # Retrieve the list of all images with these extensions(.png, .jpeg and .jpg) in the 'source path' folder.
    images = [f for f in os.listdir(source_path) if ('.png' in f.lower()) or ('.jpeg' in f.lower()) or ('jpg' in f.lower())]

    for image in images:
        new_path = destination_path + image
        old_path = source_path + image
        shutil.move(old_path, new_path)

    print("Screenshots stored on my Mac desktop have been moved to" + destination_path)
    print('=' * 100)
    # TO DO: Implement logging for this section.
    for image in images:
        print(image)
        print('=' * 100)

if __name__ == "__main__":
    main()




