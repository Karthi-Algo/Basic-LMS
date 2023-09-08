from flask import Flask ,render_template,jsonify,json,request
from flask_cors import CORS
import psycopg2
import sqlite3






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

    return jsonify(data1)

if __name__ == '__main__':
    #app.debug = True
    print("running app")
    app.run(debug=True,port=5000,host='0.0.0.0')
    
