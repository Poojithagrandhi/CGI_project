#!C:\Users\pooji\AppData\Local\Programs\Python\Python36\python
print("Content-type:text/html")
print()

print("<body style='background:skyblue'>")
print("<center>")
print("<button style='background-color:lightgreen;margin-top:20px;'><a href='alog.cgi'>BACK</a></button>")
import cgi
f=cgi.FieldStorage()
name=f.getvalue("name")
pr=f.getvalue("pr")
author=f.getvalue("author")
import pymysql
con=pymysql.connect(host="localhost",user="root",password="",database="book")
cur=con.cursor()
q="insert into book(name,author,price) values('%s','%s','%s')"%(name,author,pr)
cur.execute(q)
r=cur.rowcount
if r==0:
	print("<h1>Failed to add book</h1>")
	print("<img src='25.jpg' width=500px height=500px/>")
else:
	print("<h1>Successfully added book</h1>")
	print("<img src='28.jpg' width=500px height=500px/>")
print("</center>")
print("</body>")