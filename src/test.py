# src/test.py

import os
from util import count_cells_in_original, count_cells_in_masked

def load_counts(counts_path: str) -> dict:
    counts = {}
    with open(counts_path, 'r') as file:
        for line in file:
            image_name, count = line.strip().split()
            counts[image_name] = int(count)
    return counts

def test_cell_counting(data_folder: str, counts_path: str) -> dict:
    correct_counts = load_counts(counts_path)
    results = {"total_images": 0, "correct_count": 0, "errors": []}
    masked_img_folder = os.path.join(data_folder, "masked_img")
    original_img_folder = os.path.join(data_folder, "original_img")
    
    for image_name, true_count in correct_counts.items():
        original_image_path = os.path.join(original_img_folder, f"{image_name}.png")
        if os.path.exists(original_image_path):
            detected_count = count_cells_in_original(original_image_path)
            if detected_count != true_count:
                results["errors"].append((image_name, "original", true_count, detected_count))
            results["total_images"] += 1
        
        masked_image_path = os.path.join(masked_img_folder, f"{image_name}.png")
        if os.path.exists(masked_image_path):
            detected_count = count_cells_in_masked(masked_image_path)
            if detected_count != true_count:
                results["errors"].append((image_name, "masked", true_count, detected_count))
            results["total_images"] += 1

    results["accuracy"] = results["correct_count"] / results["total_images"] if results["total_images"] else 0
    return results
