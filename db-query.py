import sqlite3

db_locale='details.db'
conn=sqlite3.connect(db_locale)
c=conn.cursor()

c.execute("""SELECT Thumbnail.thumbnail_url,Thumbnail.title,Thumbnail.channel_name,Thumbnail.views,Thumbnail.posted_date,Thumbnail.channelimage_url,Topic.ID,Topic.Topics 
                   FROM 
                   Thumbnail
                   INNER JOIN Topic
                   ON Thumbnail.topicID =Topic.ID where ID=4""")
info=c.fetchall()
print(info)

conn.commit()
conn.close()
