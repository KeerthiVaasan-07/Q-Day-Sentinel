from flask import Flask,request,jsonify
from scanner import scan_file
import os

app=Flask(__name__)

UPLOAD_FOLDER="uploads"

os.makedirs(UPLOAD_FOLDER,exist_ok=True)

@app.route("/scan",methods=["POST"])
def scan():

    file=request.files["file"]

    path=os.path.join(UPLOAD_FOLDER,file.filename)

    file.save(path)

    result=scan_file(path)

    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)
