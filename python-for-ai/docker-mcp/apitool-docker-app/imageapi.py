from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

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
