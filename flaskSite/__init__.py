from flask import Flask, render_template, redirect, session, url_for, flash
from flask_pymongo import PyMongo
from flaskSite.forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '131f63954f3baad1268a3656705f2291dab469e56a62e902f03f396a613b0430'
app.config["MONGO_URI"] = "mongodb://localhost:27017/dgComputerDB"
mongo = PyMongo(app)

clc_processor = mongo.db.clc_processor
clc_cabinet = mongo.db.clc_cabinet
clc_cooler = mongo.db.clc_cooler
clc_graphicscard = mongo.db.clc_graphicscard
clc_harddrive = mongo.db.clc_harddrive
clc_memory = mongo.db.clc_memory
clc_monitor = mongo.db.clc_monitor
clc_motherboard = mongo.db.clc_motherboard
clc_ssd = mongo.db.clc_ssd
cld_powersupply = mongo.db.cld_powersupply
clc_users = mongo.db.clc_users
clc_orders = mongo.db.clc_orders

def get_all_items():
    items = {}
    items["Processor"] = list(clc_processor.find())
    items["Cabinet"] = list(clc_cabinet.find())
    items["Cooler"] = list(clc_cooler.find())
    items["Graphics Card"] = list(clc_graphicscard.find())
    items["Hard Drive"] = list(clc_harddrive.find())
    items["Memory"] = list(clc_memory.find())
    items["Monitor"] = list(clc_monitor.find())
    items["Motherboard"] = list(clc_motherboard.find())
    items["SSD"] = list(clc_ssd.find())
    items["Power Supply"] = list(cld_powersupply.find())
    return items

from flaskSite.routes import *