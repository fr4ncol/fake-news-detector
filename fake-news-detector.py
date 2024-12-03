from flask import Flask, render_template, request, redirect, url_for, flash, session
import requests
from mistralai import Mistral

app = Flask(__name__)
app.secret_key = "supersecretkey"  

model = "mistral-large-latest"
client = Mistral(api_key='LLyqibiPrFeMPvNQvdvlwr6lLGgzCrS2')

def get_tweet_text(url):
    try:
        post_id = url.split("/")[-1]
        search_query = f"https://cdn.syndication.twimg.com/tweet-result?id={post_id}&token=a"
        response = requests.get(search_query)
        data = response.json()
        return data.get("text", "No text found.")
    except Exception as e:
        return f"Error: {e}"

def get_mistral_response(tweet_text, language):
    try:
        if language == "en":
            content = """
                      Determine whether the following statement is "True" or "False":
                      Statement: {statement}
                      Label:
                      """
            content = content.format(tweet_text=tweet_text)
        else:
            content = """
                      Określ, czy poniższe stwierdzenie jest "Prawdziwe" czy "Fałszywe":
                      Stwierdzenie: {statement}
                      Klasyfikacja:  
                      """
            content = content.format(tweet_text=tweet_text)

        response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": content,
                },
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error in communication with the Mistral model: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    if "language" not in session:
        session["language"] = "pl"

    language = session["language"]

    if request.method == "POST":
        tweet_url = request.form.get("tweet_url")
        if tweet_url:
            tweet_text = get_tweet_text(tweet_url)
            mistral_response = get_mistral_response(tweet_text, language)
            return render_template("index.html", tweet_text=tweet_text, tweet_url=tweet_url, mistral_response=mistral_response, language=language)
        else:
            flash("Please provide a valid tweet URL.")
    return render_template("index.html", language=language)

@app.route("/set_language/<lang>")
def set_language(lang):
    session["language"] = lang
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
