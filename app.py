import crochet
crochet.setup()
from time import sleep
import Read_DB
from flask import Flask , render_template
import fipiran
app=Flask(__name__)
@app.route("/")
def crawling():
    ##storing DB
    fipiran.fipiran()

# reading DB file

#using Read_DB and reader method
    sleep(30)


    info_dict=Read_DB.reader()
    names=info_dict.get('name')
    stock=info_dict.get('stock')
    deposit=info_dict.get('deposit')
    bond=info_dict.get('bond')
    other=info_dict.get('other')
    cash=info_dict.get('cash')
    # table_info=[names,stock,deposit,bond,other,cash]


    return render_template('index.html',
    names=names,
    stock=stock,
    deposit=deposit,
    bond=bond,
    other=other,
    cash=cash,
    )
if __name__=="__main__":
    app.run(debug=True,host="127.0.0.127",port="8585")





