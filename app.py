import crochet
crochet.setup()
from time import sleep
import Read_DB
from flask import Flask , render_template
import fipiran
import json



app=Flask(__name__)
@app.route("/")
def crawling():
    ##storing DB
    fipiran.fipiran()

# reading DB file

#using Read_DB and reader method
    sleep(50)


    # info_dict=Read_DB.reader()
    # names=info_dict.get('name')
    # stock=info_dict.get('stock')
    # deposit=info_dict.get('deposit')
    # bond=info_dict.get('bond')
    # other=info_dict.get('other')
    # cash=info_dict.get('cash')
    # table_info=[names,stock,deposit,bond,other,cash]
    with open('/home/d4rk/Documents/funds/static/DB/DB.json','rb') as f:
        data=json.load(f)
    for _ in data:
        name=[_.get('name') for _ in data]
        stock=[_.get('stock') for _ in data]
        deposit= [_.get('deposit') for _ in data]
        bond= [_.get('bond') for _ in data]
        other= [_.get('other') for _ in data]
        cash= [_.get('cash') for _ in data]

    
    info_dict= {
        "name":name,
        "stock":stock,
        "deposit":deposit,
        "bond":bond,
        "other":other,
        "cash":cash,

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





