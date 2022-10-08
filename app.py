from flask import Flask, render_template, request, url_for, redirect, send_file, session
from pytube import YouTube
from io import BytesIO
from pprint import pprint

app = Flask(__name__)
app.config['SECRET_KEY'] = "654c0fb3968af9d5e6a9b3edcbc7051b"

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        session['link'] = request.form.get('mp3')
        try:
            mp3 = YouTube(session['link'])
            mp3.check_availability()
        except:
            return render_template("error.html")
        return render_template("download-mp3.html", mp3 = mp3)
    return render_template("home.html")

@app.route("/convert-mp3", methods = ["GET", "POST"])
def convertmp3():
    if request.method == "POST":
        session['link'] = request.form.get('convert-mp3')
        try:
            mp3 = YouTube(session['link'])
            mp3.check_availability()
        except:
            return render_template("error.html")
        return render_template("download-mp3.html", mp3 = mp3)
    return render_template("convert-mp3.html")


@app.route("/convert-mp4", methods = ["GET", "POST"])
def convertmp4():
    if request.method == "POST":
        session['link'] = request.form.get('convert-mp4')
        try:
            mp4 = YouTube(session['link'])
            mp4.check_availability()
        except:
            return render_template("error.html")
        return render_template("download-mp4.html", mp4 = mp4)
    return render_template("convert-mp4.html")


@app.route("/download-mp3", methods = ["GET", "POST",])
def download_mp3():
    if request.method == "POST":
        buffer = BytesIO()
        mp3 = YouTube(session['link'])
        itag = request.form.get("itag")
        video = mp3.streams.get_by_itag(itag)
        video = mp3.streams.get_audio_only()
        video.stream_to_buffer(buffer)
         

        buffer.seek(0)
        
        return send_file(buffer, as_attachment=True, download_name=mp3.title + "Audio - YT2Video.mp3", mimetype="audio/mp3")
    return redirect(url_for("/"))

@app.route("/download-mp4", methods = ["GET", "POST",])
def download_mp4():
    if request.method == "POST":
        buffer = BytesIO()
        mp4 = YouTube(session['link'])
        itag = request.form.get("itag")
        video = mp4.streams.get_by_itag(itag)
        
        video.stream_to_buffer(buffer)
                 
        
        buffer.seek(0)
        
        return send_file(buffer, as_attachment=True, download_name=mp4.title + "Video - YT2Video.mp4", mimetype="video/mp4")
    return redirect(url_for("/"))
    
@app.route("/convert-mp3", methods = ["GET", "POST",])
def convert_mp3():
 return render_template("convert-mp3.html")

@app.route("/convert-mp4", methods = ["GET", "POST",])
def convert_mp4():
 return render_template("convert-mp4.html")

if __name__ == '__main__':
    app.run(debug=True)