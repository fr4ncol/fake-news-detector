from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from mistralai import Mistral


app = Flask(__name__)
app.secret_key = "supersecretkey"  # Ustaw klucz do sesji Flaska

model = "mistral-large-latest"
client = Mistral(api_key='B4HRyk4lAmuY42FNd2oafVjWEFn91mjo')

def get_tweet_text(url):
    try:
        post_id = url.split("/")[-1]
        search_query = f"https://cdn.syndication.twimg.com/tweet-result?id={post_id}&token=a"
        response = requests.get(search_query)
        data = response.json()
        return data.get("text", "Nie znaleziono tekstu.")
    except Exception as e:
        return f"Błąd: {e}"
    
def get_mistral_response(tweet_text):
    try:
        response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": f"Sklasyfikuj, czy podane stwierdzenie jest prawdziwe czy fałszywe: {tweet_text}",
                },
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Błąd w komunikacji z Mistral: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tweet_url = request.form.get("tweet_url")
        if tweet_url:
            # Pobieranie tekstu tweeta
            tweet_text = get_tweet_text(tweet_url)
            # Uzyskiwanie odpowiedzi od Mistral
            mistral_response = get_mistral_response(tweet_text)
            return render_template("index.html", tweet_text=tweet_text, tweet_url=tweet_url, mistral_response=mistral_response)
        else:
            flash("Proszę podać prawidłowy URL tweetu.")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
