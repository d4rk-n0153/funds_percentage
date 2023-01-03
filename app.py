import crochet
crochet.setup()
from flask import Flask , render_template
import fipiran

app=Flask(__name__)
@app.route("/")
def crawling():
    ##storing DB
    fipiran.fipiran()
# reading DB file


    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True,host="127.0.0.127",port="8585")





