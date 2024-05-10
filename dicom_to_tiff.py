import os
import pydicom
import imageio

def convert_dicom_to_tiff(parent_folder, output_dir):
    # Iterate through class folders inside the parent folder
    for class_folder in os.listdir(parent_folder):
        class_folder_path = os.path.join(parent_folder, class_folder)
        if not os.path.isdir(class_folder_path):
            continue
        
        # Create corresponding output class folder
        output_class_folder = os.path.join(output_dir, class_folder)
        os.makedirs(output_class_folder, exist_ok=True)
        
        # Iterate through DICOM files in the class folder
        for filename in os.listdir(class_folder_path):
            if filename.endswith('.dcm'):
                dicom_file_path = os.path.join(class_folder_path, filename)
                # Read DICOM image
                dicom_data = pydicom.dcmread(dicom_file_path)
                
                # Convert DICOM image to numpy array
                image_array = dicom_data.pixel_array
                
                # Save as TIFF image
                output_filename = os.path.splitext(filename)[0] + '.tif'
                output_file_path = os.path.join(output_class_folder, output_filename)
                imageio.imwrite(output_file_path, image_array)
                print(f"Converted {filename} to {output_filename}")

# Example usage:
parent_folder = '/Data1/sanket/birads/Data/Test_DICOM'
output_dir = '/Data1/sanket/birads/Data/Test'

convert_dicom_to_tiff(parent_folder, output_dir)
