from flask import Flask, render_template, send_from_directory, url_for, jsonify
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
import openai

app = Flask(__name__, template_folder='./template')
app.config['SECRET_KEY'] = 'asdasdasas'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'
openai.api_key = "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"

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, 'Image only!'), 
            FileRequired('File was empty!')
        ]
    )
    submit = SubmitField('Upload')

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    form = UploadForm()
    response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="I want to make a list of recipes with the next ingredients (you don't have to include every single ingredient in every single recipe)\n\n- sauce\n- cabbage\n- orange\n- pear\n- avocado\n- apple\n- juice\n- milk\n- bread",
            temperature=0.3,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n"]
        )
    predicted_text = response.choices[0].text
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
        
    return render_template('index.html', form=form, file_url=file_url, predicted_text=predicted_text)

if __name__ == '__main__':
    app.run(debug=True)