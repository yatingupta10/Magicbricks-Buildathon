import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename
#from classify_image import *


filename = ' '
#file = ' '

UPLOAD_FOLDER = '/home/yatingupta/Image/'
ALLOWED_EXTENSIONS = set(['jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filen):
    #global filename
    return '.' in filen and \
           filen.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            #global filename, file
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.system('python classify_image.py'+' '+ filename)
            output=[]
            with open('/home/yatingupta/Documents/repo/tensorflow/tensorflow/models/image/imagenet/output.txt','r') as content_file:
                for line in content_file:
                    output.append(line.split('(')[0])
                    output.append(line.split('=')[1].split(")")[0])
            return render_template('output.html',output=output)
            #return redirect(url_for('index'))
    else:
        return render_template('upload.html')

#@app.route("/result", methods=['POST'])
#def result():
#    res=

if __name__ == "__main__":
  app.debug=True
  app.run()
#  tf.app.run()
