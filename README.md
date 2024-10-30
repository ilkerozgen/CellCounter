# Cell Counting Application

This project is a console-based application that counts cells in a series of microscopy images. It is designed to handle both raw and masked images, allowing users to analyze single images or entire folders. This tool could be used for biological image processing tasks where counting cells or similar structures is needed.

---

## Table of Contents
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Folder Structure](#folder-structure)
- [License](#license)

---

## Project Structure

The project is organized as follows:
```
--data
   ├── masked_img          # Folder containing masked images
   ├── original_img        # Folder containing original images
   └── counts.txt          # Text file with correct cell counts for each image

--src
   ├── util.py             # Functions for counting cells in original and masked images
   ├── test.py             # Tests cell counting functions and evaluates accuracy
   └── main.py             # Main script with a console-based menu for user interaction

--LICENSE
--README.md
```

## Features

- **Single Image Counting**: Allows users to count cells in a single image, either masked or original.
- **Batch Image Counting**: Counts cells in all images within a specified folder.
- **Accuracy Testing**: `test.py` can compare counted results with actual counts to evaluate accuracy.
- **Console Menu**: `main.py` provides a simple, interactive menu for users to select operations.

---

## Installation

### Prerequisites
- Python 3.6 or higher
- Git

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ilkerozgen/CellCounter
   ```

2. **Navigate to the project directory**:

   ```bash
   cd repository-name
   ```

3. **Install required packages**:

   The main dependency is OpenCV, which is used for image processing.

   ```bash
   pip install opencv-python
   ```

4. **Optional: Set up a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate    # On MacOS/Linux
   venv\Scripts\activate       # On Windows
   ```

   Then, install dependencies inside the virtual environment:

   ```bash
   pip install opencv-python
   ```

---

## Usage

1. **Run the Application**:

   Navigate to the `src` directory:

   ```bash
   cd src
   ```

   Then, run `main.py`:

   ```bash
   python main.py
   ```

   This will open a console-based menu with the following options:
   
   - **Count cells in a single image**: Counts cells in a specified image file. The user will need to specify if the image is masked or original.
   - **Count cells in all images in a folder**: Counts cells in all `.png` images within a specified folder, either masked or original.
   - **Exit**: Exits the application.

2. **Example Commands**:

   - **Counting cells in a single image**:
     - Specify the path to the image and whether it is masked or original.
   - **Counting cells in a folder**:
     - Specify the path to the folder containing images and indicate if they are masked or original.

---

## Testing

1. **Run `test.py`**:

   `test.py` can test the cell counting functions across multiple images and compare the results with the actual counts stored in `counts.txt`.

   To run the test, navigate to the `src` directory and execute:

   ```bash
   python test.py
   ```

2. **Expected Output**:

   The script will output the accuracy of the cell-counting functions and any errors encountered, allowing users to assess performance across multiple images.

---

## Folder Structure

### Data Folder

- **`masked_img/`**: Contains masked images with cells already segmented.
- **`original_img/`**: Contains original images where cells need to be masked to count.
- **`counts.txt`**: A text file listing the correct number of cells for each image. Each line follows the format:
  
  ```
  image_name number_of_cells
  ```

### Source Folder

- **`util.py`**: Contains functions `count_cells_in_original` and `count_cells_in_masked` for counting cells in original and masked images, respectively.
- **`test.py`**: Runs tests on the cell-counting functions and compares results to actual counts.
- **`main.py`**: Provides a console-based interface for interacting with the application.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.