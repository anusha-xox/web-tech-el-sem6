from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap
from flask_wtf.file import FileField, FileRequired, FileAllowed


class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=2)])
    submit = SubmitField(label='Login')


class StudentForm(FlaskForm):
    first_name = StringField(label='First Name', validators=[DataRequired()])
    last_name = StringField(label='Last Name', validators=[DataRequired()])
    grade = StringField(label='Grade', validators=[DataRequired()])
    age = StringField(label='Age', validators=[DataRequired()])
    level_assigned = StringField(label='Level', validators=[DataRequired()])
    img_url = StringField(label='Img Url', validators=[DataRequired()])
    total_points = StringField(label='Total Points', validators=[DataRequired()])
    badge = StringField(label='Badge', validators=[DataRequired()])
    no_of_writeups = StringField(label='No of Writeups', validators=[DataRequired()])
    current_book = StringField(label='Current Book Borrowed', validators=[DataRequired()])
    past_books = StringField(label='Past books', validators=[DataRequired()])
    volunteer_email = StringField(label='Volunteer Email', validators=[DataRequired()])
    submit = SubmitField(label='Add Student')


class Evaluate(FlaskForm):
    student_id = StringField(label='Your student ID', validators=[DataRequired()])
    name = StringField(label="Your Name", validators=[DataRequired()])
    grade = StringField(label="Your Grade", validators=[DataRequired()])
    level = StringField(label='The level for which you want to give the assessment', validators=[DataRequired()])
    subject = StringField(label='The subject', validators=[DataRequired()])
    question = StringField(label="your question", validators=[DataRequired()])
    answer = StringField(label="Type your answer here", validators=[DataRequired()])
    submit = SubmitField(label='Submit')


class AddBook(FlaskForm):
    isbn = StringField(label='Bar Code Number Obtained', validators=[DataRequired()])
    title = StringField(label="Title Of the Book", validators=[DataRequired()])
    genre = StringField(label="Genre", validators=[DataRequired()])
    level = StringField(label="Level Assigned", validators=[DataRequired()])
    rating = StringField(label="Rating Given", validators=[DataRequired()])
    reads = StringField(label="Reads Obtained", validators=[DataRequired()])
    age_group = StringField(label="Min. Age Requirement", validators=[DataRequired()])
    image = StringField(label="Image Url (if Available)")
    submit = SubmitField(label='Add Book')

# class Question(FlaskForm):
#     question=StringField(label="your question", validators=[DataRequired()])
#     answer=StringField(label="Type your answer here", validators=[DataRequired()])
#     submit = SubmitField(label='Login')
