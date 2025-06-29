<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-PyTorch-red?style=for-the-badge&logo=pytorch" alt="PyTorch Badge">
  <img src="https://img.shields.io/badge/Transformer-HuggingFace-blueviolet?style=for-the-badge&logo=huggingface" alt="HF Badge">
  <img src="https://img.shields.io/badge/UI-PyQt6-42f5e6?style=for-the-badge&logo=qt" alt="PyQt Badge">
</p>

<h1 align="center">🧠 Sentiment Analyzer</h1>

<p align="center">
A powerful, desktop-friendly sentiment analysis tool built with <b>PyTorch</b>, <b>HuggingFace Transformers</b>, and <b>PyQt6</b>.  
Analyze text emotions with a gorgeous GUI, real-time pie charts and smooth gradient visualizations.
</p>

---

## 🚀 Features

| Feature | Description |
|--------:|-------------|
| 🎨 Beautiful GUI | Sleek, modern PyQt6 interface |
| 📊 Pie Chart | Real-time probability distribution of sentiments |
| 🌈 Gradient Score | Visual sentiment polarity from red (-1) to green (+1) |
| 🌍 Multilingual UI | Supports English and Russian (more to come) |
| 🧠 Tiny model | Based on `cointegrated/rubert-tiny-sentiment-balanced` |

---

## 📦 Installation

> Python 3.10+ is recommended. Use [Poetry](https://python-poetry.org/) for managing dependencies.

```bash
# Clone the repository
git clone https://github.com/your-username/sentiment-analyzer.git
cd sentiment-analyzer

# Install dependencies
poetry install

# Activate the virtual environment
poetry shell
```

> Or use `pip install -r requirements.txt` if you’re not using Poetry.

---

## 🖥️ Running the App

```bash
poetry run python src/main.py
```

You’ll be prompted to choose a language. After that, just enter any text — and magic happens. ✨

---

## 🛠 Tech Stack

- 🧠 `torch`, `transformers`
- 💻 `PyQt6`, `matplotlib`
- 🧪 `poetry` for dependency management

---

## 🧙‍♂️ License

This project is licensed under the **GNU Lesser General Public License**.  
Feel free to use, fork, and contribute.

---

## 👨‍🚀 Author

Developed with caffeine and curiosity by **ExtroEd**.  
Together, let’s give AI a beautiful interface! 🌌