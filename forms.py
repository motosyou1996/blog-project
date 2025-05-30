from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField , PasswordField
from wtforms.validators import DataRequired,URL
from flask_ckeditor import CKEditorField

#WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Post Title",validators=[DataRequired()])
    subtitle = StringField("Subtitle",validators=[DataRequired()])
    author = StringField("Author",validators=[DataRequired()])
    image_url = StringField("Image URL",validators=[DataRequired(),URL()])
    body = CKEditorField("Blog Content",validators=[DataRequired()])
    summit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")

class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")