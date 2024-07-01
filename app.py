from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib

# Load the model
model = joblib.load("LinearModel.pkl")

# Initialize FastAPI app
app = FastAPI()

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

class InputData(BaseModel):
    engine_size: float
    fuel_consumption: float

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict/")
async def predict(request: Request, engine_size: float = Form(...), fuel_consumption: float = Form(...)):
    input_values = [[engine_size, fuel_consumption]]
    prediction = model.predict(input_values)[0]
    return templates.TemplateResponse("index.html", {"request": request, "prediction": prediction})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
