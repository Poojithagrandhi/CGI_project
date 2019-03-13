#!C:\Users\pooji\AppData\Local\Programs\Python\Python36\python
print("Content-type:text/html")
print()

print("<body style='background-color:skyblue'>")
print("<center>")
print("<div style='width:50%;height:200px;background-color:coral;margin-top:20px;padding:50px'>")
print("<h1>BUY HERE</h1>")
print("<table><form action='' method='post'>")
print("<tr><th>BOOK-NAME:</th><td><input type='text' name='name'/></td></tr>")
#print("<tr><th>PRICE:</th><td><input type='number' name='pr'/></td></tr>")
print("<tr><th>CARD-NUMBER:</th><td><input type='number' name='cnum'/></td></tr>")
print("<tr><td><input type='submit' value='BUY'/></td></tr>")
print("</form></table><br>")
print("</div>")
print("<button style='background-color:lightgreen;margin-top:20px;'><a href='user.cgi'>BACK</a></button>")
import cgi
import pymysql
con=pymysql.connect(host="localhost",user="root",password="",database="book")
cur=con.cursor()
f=cgi.FieldStorage()
name=f.getvalue("name")
q="delete from book where name='%s'"%(name)
cur.execute(q)
r=cur.rowcount
if r==0:
	print("<h1>Failed to buy book</h1>")
	print("<img src='25.jpg' width=300px height=300px/>")
else:
	print("<h1>Successfully baught the book</h1>")
	print("<img src='28.jpg' width=300px height=300px/>")

print("</center>")
print("</body>")