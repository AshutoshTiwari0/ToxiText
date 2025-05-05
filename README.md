# ToxiText

## Overview

**ToxiText** is an NLP-powered web application designed to detect hate speech in text. By leveraging logistic regression and TF-IDF vectorization, ToxiText helps identify toxic language in real time, offering a lightweight, browser-based interface for users to analyze and classify input text. It’s a simple yet effective tool to promote healthier online interactions.

## Features

- 🧠 Uses **Logistic Regression** + **TF-IDF** vectorizer for predictions.
- 📄 Detects hate speech in user-input text.
- ⚙️ Streamlit-based web interface for easy interaction.
- 💬 Classifies text as **Hate Speech** or **Not Hate Speech**.

## Prerequisites

- Python 3.8 or higher
- Required Python packages (listed in `requirements.txt`)

## Installation

Clone the repository:

```bash
git clone https://github.com/AshutoshTiwari0/toxitext.git
cd toxitext
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Then, open your browser and navigate to the provided URL (usually `http://localhost:8501`) to use the application.

Input any text you'd like to analyze, and the app will classify it as **Hate Speech** or **Not Hate Speech**.

## File Structure

```
├── app.py               # Main Streamlit app
├── hate_speech.pkl      # Serialized TF-IDF + Logistic Regression model
├── TweetBLM.csv         # Dataset used for model training
├── hate_speech.ipynb    # Jupyter Notebook for model development
├── toxic.png            # Image used in the app
├── requirements.txt     # Dependency file
├── Procfile             # For Heroku deployment
├── runtime.txt          # Python version (for Heroku)
├── setup.sh             # Startup script (optional for deployment)
```

## Deployment

ToxiText can be easily deployed using:

- **Streamlit Community Cloud** – Just upload your code and click "Deploy".
- **Heroku** – Use the included `Procfile` and `runtime.txt` for deployment configuration.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## Acknowledgements

- [scikit-learn](https://scikit-learn.org/)
- [Streamlit](https://streamlit.io/)
- Dataset source: BLM Tweets (Kaggle)

## License

This project is licensed under the MIT License.

---

**Made with ❤️ by Ashutosh Tiwari**
