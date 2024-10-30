# src/main.py

import os
from util import count_cells_in_original, count_cells_in_masked

def main():
    while True:
        print("Cell Counting Application")
        print("1. Count cells in a single image")
        print("2. Count cells in all images in a folder")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            image_path = input("Enter the path to the image: ")
            masked = input("Is the image masked? (yes/no): ").strip().lower()
            if masked == 'yes':
                cell_count = count_cells_in_masked(image_path)
            else:
                cell_count = count_cells_in_original(image_path)
            print(f"Detected cell count: {cell_count}")

        elif choice == '2':
            folder_path = input("Enter the path to the folder with images: ")
            masked = input("Are the images masked? (yes/no): ").strip().lower()
            total_count = 0
            image_count = 0

            for filename in os.listdir(folder_path):
                if filename.endswith('.png'):
                    image_path = os.path.join(folder_path, filename)
                    if masked == 'yes':
                        cell_count = count_cells_in_masked(image_path)
                    else:
                        cell_count = count_cells_in_original(image_path)
                    print(f"{filename}: {cell_count} cells")
                    total_count += cell_count
                    image_count += 1

            print(f"\nTotal cells in {image_count} images: {total_count}")

        elif choice == '3':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
