# 🌡️ Summer Heatwave Mobile Alert System

An AI/ML-powered solution to detect and predict extreme summer heatwaves and deliver timely alerts.  
This system uses historical and current climate data to assess heatwave severity and provides real-time risk alerts to help reduce health impacts caused by extreme temperature events.

---

## 📁 Project Structure

summer-heatwave-alert/
│
├── data/
│ ├── raw/ # Raw downloaded datasets (.tif, .csv)
│ └── processed/ # Cleaned and transformed data for modeling
│
├── models/ # Trained machine learning models (.pkl, .h5)
│ └── heatwave_predictor.pkl
│
├── notebooks/ # Jupyter notebooks for EDA, modeling
│ └── 01_eda_heatwave.ipynb
│
├── scripts/ # Core logic and ML scripts
│ ├── load_and_visualize.py
│ ├── tif_to_csv.py
│ └── train_model.py
│
├── .gitignore # Files/folders to be ignored by Git
├── requirements.txt # Python libraries used
└── README.md # Project documentation (this file)


---

## 🚀 Features

- 📊 Load and process climate data (e.g., temperature, heat index from `.tif`)
- 🧠 Train machine learning models to classify heatwave severity
- 🗺️ Visualize intensity and spatial distribution of heatwaves
- 🔔 Generate alerts based on predicted risk levels
- 📈 Evaluate model performance and export results

---

## 🛠️ Tech Stack

- **Languages**: Python
- **ML/AI**: Scikit-learn, Pandas, NumPy, Rasterio
- **Visualization**: Matplotlib, Seaborn, GeoTIFF heatmaps

---

## ⚙️ How to Run

### 1. Clone the Repo

    ```bash
    git clone https://github.com/your-username/summer-heatwave-alert.git
    cd summer-heatwave-alert

## 2. Create a Virtual Environment

    ```bash
    python -m venv .venv
    # Activate the environment
    .venv\Scripts\activate          # On Windows
    source .venv/bin/activate      # On macOS/Linux

## 3. Install Dependencies

    ```bash
    pip install -r requirements.txt

## 4. Run Scripts

    ```bash
    cd scripts
    python load_and_visualize.py

📥 Raw Dataset
⚠️ Raw data files are not included in the repo. Please download them separately.

You can download the required climate datasets (e.g., GeoTIFFs, CSVs) from a verified source:

🔗 Download Raw Dataset
(Replace with the actual dataset link you're using)

After download, place the files inside:

    ```bash
    data/raw/
🔮 Upcoming Milestones
✅ Complete data processing and EDA

✅ Build and train baseline ML models

📊 Enhance visualizations for better insights

🧪 Add model evaluation metrics and outputs

📡 (Optional) Automate detection using real-time weather feeds

🤝 Contributing
This is a student AI/ML project built for research and practical application.
Contributions, suggestions, and collaborations are welcome! Feel free to:

Fork the repo

Open issues

Submit pull requests




  
