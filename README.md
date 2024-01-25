# Plant-Seedling-Classification

## Dataset Description

Can you differentiate a weed from a crop seedling? The Plant Seedling Classification project aims to answer this question by utilizing machine learning techniques. Developed in collaboration with Aarhus University Signal Processing group and the University of Southern Denmark, this project focuses on classifying plant seedlings based on images.

The dataset, containing images of approximately 960 unique plants belonging to 12 species at various growth stages, can be found [here](https://www.kaggle.com/c/plant-seedlings-classification/data).

The goal is to create a classifier capable of determining a plant's species from a photo. The list of species is as follows:

1. Black-grass
2. Charlock
3. Cleavers
4. Common Chickweed
5. Common wheat
6. Fat Hen
7. Loose Silky-bent
8. Maize
9. Scentless Mayweed
10. Shepherds Purse
11. Small-flowered Cranesbill
12. Sugar beet

## Code and Dependencies

This project requires **Python** and the following Python Libraries installed:

- [numpy](http://www.numpy.org/)
- [matplotlib](http://matplotlib.org/)
- [tensorflow](https://www.tensorflow.org/)

`image-classification.ipynb` includes the code for exploratory data analysis (EDA) and the training process of the convolutional neural network (CNN) from the ground up. It explores a range of models, fine-tunes hyperparameters, and employs techniques like Batch Normalization, Dropout layers, and Data Augmentation to achieve optimal model performance.

Below are instructions on how to install dependencies using the `requirements.txt` file:

1. **Navigate to the Project Directory**:
  Open a terminal and change your working directory to the location where your project files are

2. **Create a Virtual Environment** (Optional but Recommended): It's good practice to create a virtual environment to isolate your project dependencies. Activate the virtual environment

3. **Install Dependencies**: Use `pip`` to install the required packages from the `requirements.txt` file.

``` bash
pip install -r requirements.txt
```

## Contanerization

Tensorflow Model has been converted to tensorflow lite model. The code can be found in `tf_lite.ipynb`.

 Dockerfile uses the official TensorFlow runtime image for AWS Lambda as the base image. It then installs the required Python packages, and any other necessary files into the container.

 To build the Docker image locally, you can use the following command in the directory containing your Dockerfile and other project files:

 ``` bash
 docker build -t your-image-name .
 ```
Replace your-image-name with a suitable name for your Docker image. After building the image, you can run a container based on it.

## Deployment of AWS Lambda

The Plant Seedling Classification model has been successfully deployed on AWS Lambda, enabling efficient weed and crop seedling differentiation. The deployment workflow includes:

1. Lambda Function Configuration:

- Creation of a Lambda function named <your-function-name> using `lambda_function.py`.

- Runtime set to Python 3.10 with the handler as `lambda_function.lambda_handler`.

2. Code and Dependencies:

- Uploaded `lambda_function.py` as the function code.
- Set the handler to `lambda_function.lambda_handler`.
- Added the environment variable:
  - Key: MODEL_PATH
  - Value: /path/to/your/model.tflite.

3. Code and Dependencies:

- Uploaded lambda_function.py as the function code.
- Set the handler to lambda_function.lambda_handler.
- Added the environment variable:
    - Key: MODEL_PATH
    - Value: /path/to/your/model.tflite.

4. Testing:

- Test events created and executed in the Lambda Console to ensure proper functioning.
- Sample test JSON payload includes the "url" key pointing to an image URL.

5. Deployment:

- Deployment initiated through the Lambda Console or AWS CLI.
- Function endpoint URL obtained for future predictions.

#### Usage Instructions

To obtain predictions, send an HTTP POST request to the Lambda function endpoint using a JSON payload with the "url" key pointing to the image URL.

Example using cURL:

``` bash
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://example.com/image.jpg"}' <YOUR_LAMBDA_ENDPOINT>
```
The response will contain the model predictions for the provided image.

Note: Ensure that the TFLite model file (model.tflite) is accessible by the Lambda function. Adjust the MODEL_PATH environment variable accordingly.







