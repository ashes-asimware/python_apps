import os
from icrawler.builtin import BingImageCrawler

MAX_FETCH_PER_REQUEST = 5
OUTPUT_DIR = "images"


# fetch 100 images of cars from google images and save them as PNG files
def image_generator(pictureofthing="cars", num_images=25):
    image_crawler = BingImageCrawler(storage={"root_dir": OUTPUT_DIR})

    # Crawl 100 car images
    for i in range(5):
        image_crawler.crawl(
            keyword=pictureofthing,
            max_num=num_images // MAX_FETCH_PER_REQUEST,  # number of images to fetch
            filters=None,  # you can add filters like size, type, etc.
            file_idx_offset=0,  # start naming files from car_0001.png
        )

    print(f"✅ {num_images} {pictureofthing} images downloaded to:", OUTPUT_DIR)


def clear_images():
    if os.path.exists(OUTPUT_DIR):
        for filename in os.listdir(OUTPUT_DIR):
            file_path = os.path.join(OUTPUT_DIR, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("All images cleared.")
    else:
        print("No images to clear.")


# image_generator()  # Uncomment to generate images
# clear_images()  # Uncomment to clear images
