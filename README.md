<h1>Multi-View Swin Transformer for Mammographic Image Classification</h1>

This repository contains the implementation of a multi-view Swin Transformer model for mammographic image classification. The model is designed to classify mammogram images into different categories, aiding in the early detection of breast cancer.

**Dataset Preprocessing:**

The dataset used in this project consists of mammographic images in DICOM format. However, as DICOM format is not directly compatible with deep learning frameworks, the images were converted to the more widely supported TIFF format for ease of use.
The data was organized into appropriate classes structured to align with the Swin Transformer architecture. Each class is represented by a subfolder containing relevant images, facilitating effective training and classification.
Training Procedure:

Prior to training, the dataset underwent normalization to standardize pixel intensity values, ensuring uniformity across images and aiding convergence during optimization.
The Swin Transformer model was trained using the Adam optimizer and cross-entropy loss function, commonly employed in classification tasks.
The training process involved rigorous validation at regular intervals, typically after each epoch, to assess model performance and prevent overfitting.
For validation purposes, the dataset was split into training and validation sets using a 50-50 split, with 50% of the data allocated to each set. This balanced partitioning ensures that the model is trained on a diverse range of samples and validated on unseen data, thereby gauging its generalization ability accurately.

**Future Scope:**

Despite the promising nature of the multi-view Swin Transformer model, further improvements can be made by integrating additional preprocessing methods into the pipeline. Techniques such as windowing, which enhance image contrast and visibility of abnormalities, can potentially boost classification accuracy significantly.
Additionally, considering that computational efficiency is not a primary concern for this application, further model tuning and experimentation can be conducted to optimize performance, even at the cost of increased computational load.
