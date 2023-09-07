import sqlite3

db_locale='details.db'
conn=sqlite3.connect(db_locale)
c=conn.cursor()

c.execute(""" 
INSERT INTO Thumbnail(image_id,thumbnail_url,title,channel_name,views,posted_date,channelimage_url)VALUES
('1','https://img.freepik.com/premium-photo/business-data-financial-figures-visualiser-graphic_31965-22136.jpg?size=626&ext=jpg&ga=GA1.2.1113312722.1689656663&semt=ais','Datascience','karthi yt','3.4M views','3 days ago','https://images.unsplash.com/photo-1505968409348-bd000797c92e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60'),
('2','https://plus.unsplash.com/premium_photo-1668490321931-9a8dbc048734?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGZyZWUlMjBpbWFnZXN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60','Datascience','raja yt','3M views','5 days ago','https://images.unsplash.com/photo-1593696954577-ab3d39317b97?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60'),
('3','https://img.freepik.com/free-photo/3d-rendering-biorobots-concept_23-2149524396.jpg?size=626&ext=jpg&ga=GA1.1.1113312722.1689656663&semt=ais','Machine Learning','raina yt','2.4M views','7 days ago','https://images.unsplash.com/photo-1530076886461-ce58ea8abe24?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60'),
('4','https://media.istockphoto.com/id/1283875643/photo/modern-office-space-with-waiting-room-board-room-and-cityscape-background.jpg?s=612x612&w=0&k=20&c=UiXhxyDlleOy_fJIeMlq5ATdn7yx9PLyzBNI_pG1xew=','Machine Learning','suresh yt','1.4M views','2 days ago','https://images.unsplash.com/photo-1585020430145-2a6b034f7729?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fGZyZWUlMjBpbWFnZXN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60'),
('5','https://img.freepik.com/free-vector/wireframe-robot-ai-artificial-intelligence-robotic-hand-machine-learning-cyber-mind-domination-concept_127544-852.jpg?size=626&ext=jpg&ga=GA1.1.1113312722.1689656663&semt=ais','Articial Intelligence','virat yt','1.9M views','5 days ago','https://images.unsplash.com/photo-1499209974431-9dddcece7f88?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGZyZWUlMjBpbWFnZXN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60'),
('6','https://img.freepik.com/free-photo/medium-shot-man-wearing-vr-glasses_23-2149126949.jpg?size=626&ext=jpg&ga=GA1.1.1113312722.1689656663&semt=ais','Articial Intelligence','sharma yt','5.4M views','2 weeks ago','https://plus.unsplash.com/premium_photo-1682124185255-0f04e1663aec?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGZyZWUlMjBpbWFnZXN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60'),
('7','https://img.freepik.com/premium-photo/python-programming-code-abstract-technology-background_272306-146.jpg?size=626&ext=jpg&ga=GA1.1.1113312722.1689656663&semt=ais','Python','ashwin yt','1.1M views','1 day ago','https://img.freepik.com/free-vector/digital-coding-background-with-numbers-zero-one_1017-30363.jpg?size=626&ext=jpg&ga=GA1.1.1113312722.1689656663&semt=ais'),
('8','https://img.freepik.com/free-vector/innovation-education-logo-template-vector-with-atom-science-graphic_53876-125986.jpg?size=626&ext=jpg&ga=GA1.1.1113312722.1689656663&semt=ais','Reactjs','varma yt','1.9M views','3 weeks ago','https://img.freepik.com/free-vector/gradient-code-logo-with-tagline_23-2148811020.jpg?size=626&ext=jpg&ga=GA1.1.1113312722.1689656663&semt=ais')

          """)



conn.commit()
conn.close()
