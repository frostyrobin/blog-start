from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Length, EqualTo
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


##WTFormRegister
class CreateRegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators = [DataRequired(), Length(min=8), EqualTo('confirm_password', message='Passwords must match.')])
    confirm_password = PasswordField()
    submit = SubmitField("Register")

##WTFormLogin
class CreateLoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators= [DataRequired()])
    submit = SubmitField("Login")



###WTFormComment
class CreateCommentForm(FlaskForm):
    comment = CKEditorField("Comment")
    submit = SubmitField('Submit')