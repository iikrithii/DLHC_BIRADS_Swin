import os
import pandas as pd

# Read the dataset
dataset_path = "/Data1/sanket/birads/breast-level_annotations.csv"
data = pd.read_csv(dataset_path)

# Define the root directory where images are stored
image_root = "/Data3/vineela/allatoneplace"

# Function to get the BIRADS classification and split for a given study ID
def get_info(study_id):
    study_data = data[data['study_id'] == study_id]
    birads_classification = study_data['breast_birads'].iloc[0]
    split = study_data['split'].iloc[0]
    return birads_classification, split

# Iterate over each entry in the dataset
for index, row in data.iterrows():
    study_id = row['study_id']
    image_id = row['image_id']
    birads_classification, split = get_info(study_id)

    # Construct the path to the image
    image_path = os.path.join(image_root, split, birads_classification, f"{image_id}.dcm")
    
    # Check if the image exists
    if os.path.exists(image_path):
        # Process the image here (e.g., read, analyze, etc.)
        # For now, let's just print the details
        print(f"Study ID: {study_id}, BIRADS Classification: {birads_classification}, Split: {split}")
    else:
        print(f"Image not found for Study ID: {study_id}")

