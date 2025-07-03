
# azure_image_classifier.py
# Mahesh Ramdas Gite — Microsoft Azure AI Internship Project

from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

# Replace these with your Azure Custom Vision details:
ENDPOINT = "YOUR_CUSTOM_VISION_ENDPOINT"  # Example: https://<region>.api.cognitive.microsoft.com/
PREDICTION_KEY = "YOUR_PREDICTION_KEY"
PROJECT_ID = "YOUR_PROJECT_ID"
PUBLISHED_NAME = "YOUR_PUBLISHED_ITERATION_NAME"

# Authenticate with Azure
credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
predictor = CustomVisionPredictionClient(ENDPOINT, credentials)

# Open a local test image
with open("test_image.jpg", "rb") as image_data:
    results = predictor.classify_image(
        PROJECT_ID, PUBLISHED_NAME, image_data.read()
    )

# Display prediction results
for prediction in results.predictions:
    print(
        f"Tag: {prediction.tag_name}, "
        f"Probability: {prediction.probability * 100:.2f}%"
    )
