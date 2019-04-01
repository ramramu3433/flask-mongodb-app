from flask import Flask
from flask import request,render_template
from flask_pymongo import PyMongo
import json
from pymongo import MongoClient
import os

app=Flask(__name__)
mongo_url=os.environ.get("MONGO_DB_URI")

app.config["MONGO_URI"]=mongo_url

mongo=PyMongo(app)

@app.route("/add",methods=["POST"])
def add():
    if request.method=="POST":
       data_=json.loads(request.data)
       id_=users.insert_one({"name":data_["name"]}).inserted_id
       return "Added the product on id:{}".format(id_)
    else:
       return "Please use get method"
   
@app.route("/")
def home():
    return "<a href='total_products'>To get all the products in catalogue</a>"     
@app.route("/collections")
def get_count():
    return render_template("collections.html",db=mongo.db.name,collections=mongo.db.list_collection_names())

@app.route("/total_products")
def get_products():
    return render_template("products.html",products=users.distinct('name'))

@app.route("/count_product/<product>")
def get_count_product(product):
    return render_template("stats.html",product_=product,count=users.count_documents({"name":product}))


if __name__=="__main__":
   try: 
     client=MongoClient(mongo_url)
     client.list_databases()
     users=mongo.db.products
   except Exception as e:
     print("couldn't able to create mongodb collection due the error {}".format(e))
   app.run(port=9000,debug=True)