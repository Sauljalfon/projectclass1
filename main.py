from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    restaurants = StringField('Restaurants name', validators=[DataRequired()], render_kw={"size":30})
    rest_location = URLField('Restaurant Location', validators=[DataRequired()], render_kw={"size":30})
    opening_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()], render_kw={"size":30})
    closing_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()], render_kw={"size":30})
    food_rating = SelectField('Food Rating', choices=[
        ('👍', '👍'),
        ('👍👍', '👍👍'),
        ('👍👍👍', '👍👍👍'),
        ('👍👍👍👍', '👍👍👍👍'),
        ('👍👍👍👍👍', '👍👍👍👍👍'),
    ])
    service = SelectField('Service', choices=[
        ('✘', '✘'),
        ('💪', '💪'),
        ('💪💪', '💪💪'),
        ('💪💪💪', '💪💪💪'),
        ('💪💪💪💪', '💪💪💪💪'),
        ('💪💪💪💪💪', '💪💪💪💪💪'),
    ])
    cost = SelectField('Cost', choices=[
        ('💵', '💵'),
        ('💵💵', '💵💵'),
        ('💵💵💵', '💵💵💵'),
        ('💵💵💵💵', '💵💵💵💵'),
        ('💵💵💵💵💵', '💵💵💵💵💵'),
    ])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        restaurants = form.restaurants.data
        rest_location = form.rest_location.data
        opening_time = form.opening_time.data
        closing_time = form.closing_time.data
        food_rating = form.food_rating.data 
        service = form.service.data
        cost = form.cost.data
        final_string_csv = f"{restaurants},{rest_location},{opening_time},{closing_time},{food_rating},{service},{cost}\n"
        
        with open('data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            csv_file.write(final_string_csv)

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes', methods=["GET", "POST"])
def cafes():
    with open('data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
