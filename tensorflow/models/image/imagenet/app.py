import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
import tensorflow as tf
#import classify_image.py


UPLOAD_FOLDER = '/home/yatingupta/Image/'
ALLOWED_EXTENSIONS = set(['jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "TEST"
            #return redirect(url_for('index'))
    else:
        return """
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="" method=post enctype=multipart/form-data>
          <p><input type=file name=file>
             <input type=submit value=Upload>
        </form>
        """ 

#@app.route("/result", methods=['POST'])
#def result():
#    res=

if __name__ == "__main__":
  app.debug=True
  app.run()
#  tf.app.run()
