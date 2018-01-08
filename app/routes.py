#!flask/bin/python
from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail
from plexapi.server import PlexServer

mail = Mail()

app = Flask(__name__)

app.secret_key = 'xxxxxx'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'contact@example.com'
app.config["MAIL_PASSWORD"] = 'your-password'

PLEX_URL = 'http://plex.themetabay.org:32400'
PLEX_TOKEN = app.secret_key
plex_server_var = PlexServer(PLEX_URL, PLEX_TOKEN)



mail.init_app(app)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/invite', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('invite.html', form=form)
    else:
      
      # actual Plex invite
      plex.myPlexAccount().updateFriend(user=form.plexuser.data, server=plex_server_var, sections='')
      
      # email confirmation to server owner
      msg = Message(Plex user form.plexuser.data invted, sender='contact@example.com', recipients=['your_email@example.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)

      return render_template('invite.html', success=True)

  elif request.method == 'GET':
    return render_template('invite.html', form=form)
  
if __name__ == '__main__':
  app.run(debug=True)
