#!C:\Users\pooji\AppData\Local\Programs\Python\Python36\python
print("Content-type:text/html")
print()

import cgi
f=cgi.FieldStorage()
uname=f.getvalue("uname")
pwd=f.getvalue("pwd")
if uname=="admin":
	if pwd=="admin":
		print("<body style='background-color:skyblue'>")
		print("<center>")
		print("<button style='background-color:lightgreen;margin-top:20px;'><a href='admin.html'>BACK</a></button>")
		print("<div style='width:50%;height:200px;background-color:coral;margin-top:20px;padding:50px'>")
		print("<h1>ADD BOOK DETAILS</h1>")
		print("<table><form action='add.cgi' method='post'>")
		print("<tr><th>BOOK-NAME:</th><td><input type='text' name='name'/></td></tr>")
		print("<tr><th>PRICE:</th><td><input type='number' name='pr'/></td></tr>")
		print("<tr><th>AUTHOR:</th><td><input type='text' name='author'/></td></tr>")
		print("<tr><td><input type='submit' value='ADD'/></td></tr>")
		print("</form></table><br>")
		print("<form action='disp.cgi' method='post'>")
		print("<input type='submit' value='VIEW BOOKS'/>")
		print("</form>")
		print("</div>")
		print("</center>")
		print("</body>")
	else:
		print("Wrong password")
else:
	print("Wrong username")

	
