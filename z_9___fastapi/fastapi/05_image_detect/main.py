from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO
from predict import predict

app = FastAPI()

@app.post("/predict/image")
async def predict_img(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = Image.open(BytesIO(await file.read()))
    prediction = predict(image)
    return prediction

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)