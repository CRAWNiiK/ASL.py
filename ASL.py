# Import the necessary libraries
import requests
from PIL import Image
from io import BytesIO

# Define the base URL for the ASL image API
base_url = "https://aslbrowser.azurewebsites.net/api/v1/images/"

# Get user input
user_input = input("Enter a word or phrase: ")

# Make a GET request to the ASL image API
response = requests.get(base_url + user_input)

# Check if the response was successful
if response.status_code == 200:
	# Convert the response to an image object
	img = Image.open(BytesIO(response.content))
	# Display the image
	img.show()
else:
	print("Sorry, I could not find an ASL image for that word or phrase.")