import crochet
crochet.setup()
from time import sleep
from flask import Flask , render_template
import fipiran
import READ_DB


app=Flask(__name__)
@app.route("/")
def crawling():
    ##storing DB
    fipiran.fipiran()

# reading DB file
    sleep(30)

    info_dict=READ_DB.reader()

    info_dict= {
        "name":info_dict.get("name"),
        "stock":info_dict.get("stock"),
        "deposit":info_dict.get("deposit"),
        "bond":info_dict.get("bond"),
        "other":info_dict.get("other"),
        "cash":info_dict.get("cash"),

    }

    return render_template('index.html',
    names=info_dict.get("names"),
    stock=info_dict.get("stock"),
    deposit=info_dict.get("deposit"),
    bond=info_dict.get("bond"),
    other=info_dict.get("other"),
    cash=info_dict.get("cash"),
    )
if __name__=="__main__":
    app.run(debug=True,
    host="127.0.0.1",
    port="8585"
    )





