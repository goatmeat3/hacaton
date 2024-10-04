from jsonschema import validate
import jsonschema
import json
from word_processing import process_word

def read_word_from_json(filename):

  try:

    with open(filename, 'r', encoding='utf-8') as file:

      data = json.load(file)

      try:
        schema = {
          "type": "array",
          "items": {
            "type": "string"
          },
          "minItems": 1  # В файле должно быть > 1 элемента
        }

        validate(instance=data, schema=schema)

        dict = {}

        for i in data:
          istina = process_word(i)
          if istina and ' ' in istina:
            for index, word in enumerate(istina.split()):
              if word not in dict:
                dict[word] = 1
              else:
                dict[word] +=1

          if istina and ' ' not in istina:
            if istina not in dict:
              dict[istina] = 1
            else:
              dict[istina] += 1
        return dict

      except jsonschema.exceptions.ValidationError as e:
        return print(f"Ошибка валидации JSON: {e}")

  except FileNotFoundError:
    return print(f"Ошибка: возможно файл поврежден.\nУбедитесь что ваш файл "
          f"формата JSON и соответствует виду, приведенному в инструкции")



