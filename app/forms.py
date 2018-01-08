from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):

  plexuser = TextField("Your Plex.tv username",  [validators.Required("Please enter a Plex username.")])
  name = TextField("Name (optional)",  [validators.Optional("Please enter your name.")])
  email = TextField("Email (optional to receive confirmation)",  [validators.Optional("Please enter your email address."), validators.Email("Please enter your email address.")])
  submit = SubmitField("Send")
