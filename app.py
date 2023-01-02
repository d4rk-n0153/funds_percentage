import crochet
crochet.setup()
from flask import Flask , render_template
import fipiran

app=Flask(__name__)

@app.route("/")
def index_page():
    
    return render_template('index.html')
if __name__=="__main__":
    app.run()





