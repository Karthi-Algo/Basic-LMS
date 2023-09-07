from flask import Flask ,render_template,jsonify,json,request
from flask_cors import CORS
import psycopg2
import sqlite3
import  logging
logging.basicConfig(filename="test.log",level=logging.DEBUG,format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
app=Flask(__name__)
CORS(app)





@app.route('/api/data',methods=['GET'])
def get_data():
    # conn =sqlite3.connect('details.db')
    conn=psycopg2.connect(database="postgres",
                          user="postgres",
                          password="Raina",
                          host="localhost",port="5432"
                          )
    cursor=conn.cursor()
    cursor.execute("""SELECT "Thumbnail".thumbnail_url,"Thumbnail".title,"Thumbnail".channel_name,"Thumbnail".views,"Thumbnail".posted_date,"Thumbnail".channelimage_url,"Topic".id,"Topic".topics 
                   FROM 
                   "Thumbnail"
                   INNER JOIN "Topic"
                   ON "Thumbnail".topic_id ="Topic".id  """ )
    data1=cursor.fetchall()
    key=["thumbnail_url","title","channel_name","views","posted_date","channelimage_url","id","topics"]
    data1=[dict(zip(key,data)) for data in data1]
    logging.debug(data1) 

    return jsonify(data1)
