from sentence_transformers import SentenceTransformer, util
from collections import defaultdict
from reading_file import read_word_from_json

def merge_synonyms(json_filename, similarity_threshold=0.7):
    model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')
    word_counts = read_word_from_json(json_filename)
    merged_words = defaultdict(int)
    processed_words = set()

    for word1 in word_counts:
        if word1 in processed_words:
            continue

        current_synonym = word1
        current_count = word_counts[word1]

        for word2 in word_counts:
            if word1 == word2 or word2 in processed_words:
                continue

            embeddings = model.encode([word1, word2])
            similarity = util.cos_sim(embeddings[0], embeddings[1]).item()

            if similarity >= similarity_threshold:
                current_synonym = word1
                current_count += word_counts[word2]
                processed_words.add(word2)

        merged_words[current_synonym] = current_count
        processed_words.add(word1)
    return merged_words
