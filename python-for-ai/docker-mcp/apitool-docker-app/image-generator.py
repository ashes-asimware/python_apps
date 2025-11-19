import os
from icrawler.builtin import GoogleImageCrawler


# fetch 100 images of cars from google images and save them as PNG files
def image_generator(pictureofthing="cars", num_images=100):
    # Set up the output folder
    output_dir = os.Path("images")
    os.makedirs(output_dir, exist_ok=True)

    # Configure the crawler
    google_crawler = GoogleImageCrawler(storage={"root_dir": output_dir})

    # Crawl 100 car images
    google_crawler.crawl(
        keyword="cars",
        max_num=100,  # number of images to fetch
        filters=None,  # you can add filters like size, type, etc.
        file_idx_offset=0,  # start naming files from car_0001.png
    )

    print("✅ 100 car images downloaded to:", output_dir)


def clear_images():
    output_folder = "images"
    if os.path.exists(output_folder):
        for filename in os.listdir(output_folder):
            file_path = os.path.join(output_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("All images cleared.")
    else:
        print("No images to clear.")


image_generator()  # Uncomment to generate images
# clear_images()  # Uncomment to clear images
