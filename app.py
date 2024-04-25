from modules.summarizer import summarize_article
from modules.text_to_speech import text_to_speech_files
from modules.movie_maker import create_video

from flask import Flask, render_template, request, jsonify, Response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("mijikai.html")


@app.route('/process_text', methods=['POST'])
def process_text():

    def generate(article):

        update = "--BEGIN PROCESSING--"
        yield f"data: {update} \n\n"

        summarized_article, summarized_article_list_of_sentences = summarize_article(article)
        print(summarized_article_list_of_sentences)

        update = "--SUMMARY GENERATED--"
        yield f"data: {update} \n\n"

        saved_audio_files = text_to_speech_files(summarized_article_list_of_sentences)
        print("Audio files saved at the following locations:")
        for file_path in saved_audio_files:
            print(file_path)

        update = "--TTS CLIPS GENERATED--"
        yield f"data: {update} \n\n"

        create_video(summarized_article_list_of_sentences)

        update = "--VIDEO GENERATED--"
        yield f"data: {update} \n\n"

    data = request.json
    article = data['text']
    
    print("CALLED RESPONSE")
    
    return Response(generate(article), mimetype='text/event-stream')
    # return jsonify({'status': 'success'})





if __name__ == '__main__':
    app.run(debug=True)
