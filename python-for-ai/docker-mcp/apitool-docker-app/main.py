# Client code to call the image API
import requests


def get_image_count():
    count_of_images = 0
    response = requests.get("http://localhost:8000/images/count")
    if response.status_code == 200:
        count_of_images = response.json().get("count", -1)
    else:
        print("Error fetching image count:", response.status_code)
        return 0
    print(f"Number of images available: {count_of_images}")
    return count_of_images
