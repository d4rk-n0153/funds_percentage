import crochet
crochet.setup()
from flask import Flask , render_template


app=Flask(__name__)

@app.route("/")
def index_page():
    from fipiran import fipiran
    return render_template('index.html')
@app.route("/funds")
def funds_page():
    return render_template('funds.html')


app.run()





