from sentence_transformers import SentenceTransformer, util
from reading_file import read_word_from_json
from collections import defaultdict

def merge_synonyms(json_filename, similarity_threshold=0.7):
    def find_common_synonym(word1, word2):
        return word1  # Здесь можно добавить логику для нахождения общего синонима

    model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')
    word_counts = read_word_from_json(json_filename)
    print("word_counts:\n", word_counts)

    # Группировка синонимов
    merged_words = defaultdict(int)
    processed_words = set()  # Множество для отслеживания обработанных слов

    for i, word1 in enumerate(word_counts):
        if word1 in processed_words:
            continue

        current_synonym = word1  # Начинаем с текущего слова
        current_count = word_counts[word1]  # Начальное значение

        for j, word2 in enumerate(word_counts):
            if i == j or word2 in processed_words:
                continue

            embeddings = model.encode([current_synonym, word2])
            similarity = util.cos_sim(embeddings[0], embeddings[1]).item()

            if similarity >= similarity_threshold:
                common_synonym = find_common_synonym(current_synonym, word2)
                current_synonym = common_synonym  # Обновляем текущий синоним, если нужно
                current_count += word_counts[word2]  # Добавляем значение к текущему счетчику
                processed_words.add(word2)

        merged_words[current_synonym] = current_count  # Записываем результат в merged_words
        processed_words.add(word1)

    print("merged_words:\n", merged_words)
    return merged_words

# Пример использования функции
# merged_results = merge_synonyms("file.json")
