from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient
def create_app():
    app= Flask(__name__)
    client= MongoClient("mongodb+srv://auzair:Pakauzi123@microblogapp.1inbaxm.mongodb.net/test")
    app.db= client.microblog
    @app.route("/",methods=["GET","POST"])
    def start():
        if request.method=="POST":
            entry_content= request.form.get("content")
            formated_date=datetime.datetime.today().strftime("%Y-%m-%d")
            print(entry_content," ",formated_date)
            app.db.entries.insert_one({"content":entry_content, "Date":formated_date})
        final_entry= app.db.entries.find({})
            
        return render_template("home.html",entries=final_entry)
    return app