from flask import Flask, render_template, send_from_directory, url_for, jsonify
from flask_uploads import UploadSet, IMAGES, configure_uploadsx
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
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role": "user", "content": "Hello, how are you?"}
        ]
    )

    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)

    return render_template('index.html', form=form, response=response['choices'][0]['message']['content'])

if __name__ == '__main__':
    app.run(debug=True)