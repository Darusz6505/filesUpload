# upload one or more files in one action
# https://www.youtube.com/watch?v=E9c59Gvib2U

# Flas - pozwala testować pliki html w lokalnie i dynamicznie uruchamianym serverze
# oruchmienie skryptu, uruchamia server app.run()

from flask import Flask, render_template, request
import os

app = Flask(__name__)

# app.config["UPLOAD_PATH"] = "C:/Users/Pracownik/Desktop/test_upload"
app.config["UPLOAD_PATH"] = "G:/Mój dysk/Py/Test"

@app.route("/upload_file", methods=["GET", "POST"])

def upload_file():
    if request.method == 'POST':
        for f in request.files.getlist('file_name'):
            # f = request.files['file_name']
            f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))
        return render_template("upload-file.html", msg="Files has beed uploaded successfully")
    return render_template("upload-file.html", msg="Please choose a file")

if __name__ == '__main__':
    app.run(debug=True)
    