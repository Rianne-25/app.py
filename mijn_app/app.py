from flask import Flask, jsonify
import random

app = Flask(__name__)

# Voorbeeldnieuwsberichten afkomstig van verschillende bronnen
news_sources = [
    "RTL Nieuws: 'Kabinet kondigt nieuwe maatregelen aan'",
    "NOS: 'Nederlandse economie groeit sneller dan verwacht'",
    "NU.nl: 'Topvoetballer maakt sensationele transfer'",
    "NOS: 'Weersvoorspelling: Koude fronten op komst'",
    "RTL Nieuws: 'Nieuwe wetgeving rondom AI ingevoerd'"
]

@app.route("/")
def home():
    return "Welkom bij het Fake News Spel! Scan de QR-code om een nieuwsbericht te ontvangen."

@app.route("/generate-news")
def generate_news():
    news = random.choice(news_sources)
    return jsonify({"news": news})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
