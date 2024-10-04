from flask import Flask, render_template, request, send_file, jsonify
import io
import json

# Экземпляр Flask
app = Flask(__name__)

# Импортируем вашу функцию для получения синонимов
from get_synonyms import main

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.txt'):
            text = file.read().decode('utf-8')
            words = text.splitlines()

            # Получаем общие синонимы
            common_synonyms, no_synonyms_words = main(words)
            synonym_dict = {word: common_synonyms.get(word, []) for word in words}

            return render_template('index_main.html', synonym_dict=json.dumps(synonym_dict), sorted_words=words)
    return render_template('index_main.html', synonym_dict=None, sorted_words=None)

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()  # Получаем данные в формате JSON
    synonym_dict = data.get('synonym_dict')

    if synonym_dict:
        try:
            synonym_dict = json.loads(synonym_dict)
        except json.JSONDecodeError:
            return '', 400

        output = io.StringIO()
        for word, synonyms in synonym_dict.items():
            if synonyms:
                output.write(f"{word}: {', '.join(synonyms)}\n")  # Записываем слово и его синонимы
            else:
                output.write(f"{word}: нет синонимов\n")  # Если нет синонимов

        output.seek(0)
        return send_file(io.BytesIO(output.getvalue().encode('utf-8')),
                         as_attachment=True,
                         download_name='synonyms.txt',
                         mimetype='text/plain')

    return '', 400

if __name__ == '__main__':
    app.run(debug=True)
