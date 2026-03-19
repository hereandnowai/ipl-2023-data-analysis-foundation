# Setup Instructions

Running these projects requires a Python environment with Jupyter Notebook, NumPy, Pandas, and Matplotlib.

## 1. Install Python
Ensure you have Python 3.8+ installed. You can download it from [python.org](https://www.python.org/).

## 2. Create a Virtual Environment (Recommended)
Open your terminal and run:
```bash
python -m venv venv
```

Activate the environment:
- **Windows:** `venv\Scripts\activate`
- **macOS/Linux:** `source venv/bin/activate`

## 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 4. Run Jupyter Notebook
```bash
jupyter notebook
```
This will open your browser. Navigate to the `projects/` folder and start with `01_data_cleaning_titanic/concepts.ipynb`.

## 5. Downloading Data
Each project folder contains a `download_data.py` script. Run it before starting the project:
```bash
cd projects/01_data_cleaning_titanic
python download_data.py
```
