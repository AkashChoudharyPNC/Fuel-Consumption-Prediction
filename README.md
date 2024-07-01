# Fuel-Consumption-Prediction

This is a simple web application built with FastAPI that predicts vehicle CO2 emissions based on engine size and fuel consumption values. The app uses a pre-trained linear regression model.

## Features

- Predict CO2 emissions based on engine size and fuel consumption
- Simple web interface for user interaction

## Installation

Follow these steps to set up and run the application:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/AkashChoudharyPNC/Fuel-Consumption-Prediction.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd Fuel-Consumption-Prediction
    ```

3. **Create a virtual environment:**
    ```bash
    python -m venv my_env
    ```

4. **Activate the virtual environment:**
    - **On Windows:**
        ```bash
        my_env\Scripts\activate
        ```
    - **On macOS/Linux:**
        ```bash
        source my_env/bin/activate
        ```

5. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Run the application:**
    ```bash
    uvicorn app:app --reload
    ```

7. **Open your web browser and go to `http://localhost:8000`.**

## Usage

1. Enter the engine size (in liters) and fuel consumption (in liters per 100 kilometers).
2. Click the "Predict" button to get the predicted CO2 emissions.

## Project Structure

- `app.py`: The main FastAPI application file.
- `templates/index.html`: The HTML template for the web interface.
- `LinearModel.pkl`: The pre-trained model file.
- `requirements.txt`: Python packages required to run the application.
