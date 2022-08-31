#!/bin/python


from flask import Flask, render_template
import requests
import json

# All this is saying is that all that you need is 
# currently in your current directory. 
app = Flask(__name__)

### Declare get_meme function 

def get_meme():
    ## Reddit API
    url = "https://meme-api.herokuapp.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit


@app.route("/")
def index():
    meme_pic,subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

app.run(host="0.0.0.0", port=80)