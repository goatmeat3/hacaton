from flask import Flask, render_template, request, send_file, jsonify
import io
import json
from index import merge_synonyms
from flask_cors import CORS

# Экземпляр Flask
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.json'):  # Изменено на .json для соответствия формату
            json_data = json.load(file)  # Загружаем JSON данные
            word_counts = json_data.get('word_counts', {})  # Предполагаем, что структура JSON содержит 'word_counts'

            # Получаем общие синонимы
            merged_words1 = merge_synonyms(word_counts)  # Используем новую функцию

            return render_template('index_main.html', synonym_dict=json.dumps(merged_words1))
    return render_template('index_main.html', synonym_dict=None)

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
        for word, count in synonym_dict.items():
            output.write(f"{word}: {count}\n")  # Записываем слово и его количество

        output.seek(0)
        return send_file(io.BytesIO(output.getvalue().encode('utf-8')),
                         as_attachment=True,
                         download_name='synonyms.txt',
                         mimetype='text/plain')

    return '', 400

if __name__ == '__main__':
    app.run(debug=True)
