from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import random
from datetime import datetime

app = FastAPI()

# Add CORS middleware to allow web app to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

IMAGES_FOLDER = Path("images")
MAX_IMAGES = 9  # Assuming a maximum of 25 images are stored


# add a default route and return swagger page
@app.get("/")
async def root():
    """Return a welcome message with link to API docs"""
    return """<h1>Welcome to the Image API</h1>
<p>Use the /docs endpoint to explore the API documentation.</p>"""


@app.get("/images/count")
async def get_image_count():
    """Return the number of PNG files in the images folder"""
    if not IMAGES_FOLDER.exists():
        return {"count": 0}

    jpg_files = list(IMAGES_FOLDER.glob("*.jpg"))
    return {"count": len(jpg_files)}


@app.get("/images/{random_number}")
async def get_image_by_number(random_number: str):
    """Return a PNG file whose name contains the matching random number"""
    if not IMAGES_FOLDER.exists():
        raise HTTPException(status_code=404, detail="Images folder not found")

    # Look for PNG files that contain the random number in their name
    number = int(random_number.strip()) % MAX_IMAGES + 1  # Ensure within range
    print(number)
    matching_files = [f for f in IMAGES_FOLDER.glob("*.jpg") if str(number) in f.stem]

    if not matching_files:
        raise HTTPException(
            status_code=404,
            detail=f"No image found with random number % {MAX_IMAGES}: {number}",
        )

    # Return the first matching file
    image_path = matching_files[0]
    return FileResponse(
        path=image_path, media_type="image/png", filename=image_path.name
    )


@app.get("/pictureofcar")
async def get_random_car_picture():
    """Return a random image from the images folder"""
    if not IMAGES_FOLDER.exists():
        raise HTTPException(status_code=404, detail="Images folder not found")

    # Get all image files (jpg and png)
    image_files = list(IMAGES_FOLDER.glob("*.jpg"))

    if not image_files:
        raise HTTPException(status_code=404, detail="No images found in folder")

    # Randomly select one image
    random_image = random.choice(image_files)

    return FileResponse(
        path=random_image,
        media_type=f"image/{random_image.suffix[1:]}",
        filename=random_image.name,
    )


@app.get("/moonphase")
async def get_moon_phase(
    date: str = Query(..., description="Date in YYYY-MM-DD format"),
):
    """Return the moon phase for a given date"""
    try:
        # Parse the date
        input_date = datetime.strptime(date, "%Y-%m-%d")

        # Calculate moon phase using a simple algorithm
        # Known new moon: January 6, 2000
        known_new_moon = datetime(2000, 1, 6)
        lunar_cycle = 29.53059  # days in a lunar cycle

        # Calculate days since known new moon
        days_since = (input_date - known_new_moon).days

        # Calculate current position in lunar cycle (0-29.53)
        phase_position = days_since % lunar_cycle

        # Determine phase based on position and map to image file
        if phase_position < 1.85 or phase_position > 27.68:
            image_name = "newmoon.png"
        elif 6.38 <= phase_position <= 8.38:
            image_name = "halfmoon.png"
        elif 13.76 <= phase_position <= 15.76:
            image_name = "fullmoon.png"
        elif 20.65 <= phase_position <= 22.65:
            image_name = "halfmoon.png"
        else:
            image_name = "emptycircle.png"

        # Check if image exists
        image_path = IMAGES_FOLDER / image_name
        if not image_path.exists():
            raise HTTPException(
                status_code=404, detail=f"Moon phase image not found: {image_name}"
            )

        return FileResponse(
            path=image_path, media_type="image/png", filename=image_name
        )

    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid date format. Please use YYYY-MM-DD format (e.g., 2025-11-26)",
        )


if __name__ == "__main__":
    import uvicorn
    import configsettings as cs

    uvicorn.run(
        app,
        host=cs.IP_ADDRESS,
        port=cs.PORT,
        ssl_keyfile=cs.SSL_KEYFILE,
        ssl_certfile=cs.SSL_CERTFILE,
    )
