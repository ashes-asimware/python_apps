from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

IMAGES_FOLDER = Path("images")


@app.get("/images/count")
async def get_image_count():
    """Return the number of PNG files in the images folder"""
    if not IMAGES_FOLDER.exists():
        return {"count": 0}

    png_files = list(IMAGES_FOLDER.glob("*.png"))
    return {"count": len(png_files)}


@app.get("/images/{random_number}")
async def get_image_by_number(random_number: str):
    """Return a PNG file whose name contains the matching random number"""
    if not IMAGES_FOLDER.exists():
        raise HTTPException(status_code=404, detail="Images folder not found")

    # Look for PNG files that contain the random number in their name
    matching_files = [f for f in IMAGES_FOLDER.glob("*.png") if random_number in f.stem]

    if not matching_files:
        raise HTTPException(
            status_code=404,
            detail=f"No image found with random number: {random_number}",
        )

    # Return the first matching file
    image_path = matching_files[0]
    return FileResponse(
        path=image_path, media_type="image/png", filename=image_path.name
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
