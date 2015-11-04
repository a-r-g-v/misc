import MySQLdb
import urlparse

poe = "https://wordpress.wordpress"

db = MySQLdb.connect(db="wordpress",user="",passwd="") 
c = db.cursor() 
sql = "SELECT ID,guid from wp_posts;"
c.execute(sql)
records = c.fetchall()
for record in records:
   o = urlparse.urlparse(record[1])
   url = poe + o.path
   if o.query:
     url = url + "?" + o.query
   print "UPDATE wp_posts SET guid ='" + url + "' where ID = '" + str(record[0]) + "';"

