# 🛒 Product Price Comparison and Prediction System

This project scrapes product prices from e-commerce sites, compares them, and predicts future price trends using machine learning.

## 🚀 Features

- Web scraping from e-commerce websites (e.g., Amazon, Flipkart)
- Price comparison across platforms
- Price trend prediction using ML models
- Extensible for dashboards and alerts

## 📁 Project Structure

```
product-price-comparison/
├── data/               # Collected product data
├── models/             # Trained ML models
├── notebooks/          # Jupyter notebooks for analysis
├── scripts/            # Python scripts (scraper, ML, etc.)
│   ├── scraper.py      # Web scraper code
│   └── model.py        # ML model training
├── requirements.txt    # Python dependencies
├── .gitignore          # Files to ignore in Git
└── README.md           # Project documentation
```

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/product-price-comparison.git
cd product-price-comparison
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Scraper

Edit `scripts/scraper.py` with a real product URL and run:

```bash
python scripts/scraper.py
```

---

## 📈 Future Plans

- Add LSTM model for price forecasting
- Build a price drop alert system
- Include review sentiment analysis

---

## 📄 License

MIT License
