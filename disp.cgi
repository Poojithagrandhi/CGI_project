#!C:\Users\pooji\AppData\Local\Programs\Python\Python36\python
print("Content-type:text/html")
print()

import pymysql
con=pymysql.connect(host="localhost",user="root",password="",database="book")
cur=con.cursor()
q="select name,author,price from book"
cur.execute(q)
print("<body style='background:skyblue'>")
print("<center>")
print("<h1>BOOK DETAILS</h1>")
print("<button style='background-color:lightgreen;margin-top:20px;'><a href='alog.cgi'>BACK</a></button>")
print("<table style='background:orange;border:2px solid brown;box-shadow:3px 5px gray'>")
print("<tr>")
print("<th>NAME</th>")
print("<th>AUTHOR</th>")
print("<th>PRICE</th>")
print("</tr>")
for r in cur.fetchall():
	print("<tr>")
	for c in r:
		print("<td style='background:pink;border:1px solid brown;padding:5px'>"+c+"</td>")
	print("</tr>")
print("</center>")
print("</table>")
print("</body>")