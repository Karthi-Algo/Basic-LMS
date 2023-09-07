import sqlite3

db_locale='details.db'
conn=sqlite3.connect(db_locale)
c=conn.cursor()

c.execute("""
CREATE TABLE "Thumbnail" 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
	("image_id"	INTEGER ,
	"thumbnail_url"	BLOB,
	"title"	TEXT,
	"channel_name"	TEXT,
	"views"	REAL,
	"posted_date"	TEXT,
	"channelimage_url"	BLOB,
	PRIMARY KEY("image_id" AUTOINCREMENT)
)
""")
CREATE TABLE "Topic" (
	"ID"	INTEGER,
	"Topics"	VARCHAR(30),
	PRIMARY KEY("ID" AUTOINCREMENT)
);
""")




conn.commit()
conn.close()
