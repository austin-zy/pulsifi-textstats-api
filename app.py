from flasgger import Swagger
from flask import Flask, jsonify
from flask import request
from textstat.textstat import textstatistics

from helper.text_helper import count_word, count_pos, stem_text

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/calculate_text_stat', methods=['POST'])
def calculate_text_stat():
    '''
    file: docs/calculate_text_stat.yml
    '''
    try:
        content = request.json
        test_data = content['text']
    except TypeError:
        return jsonify("Your payload is empty")
    except KeyError:
        return jsonify("Text not found")
    textstats = textstatistics()
    syllable_count = textstats.syllable_count(test_data, lang='en_US')
    lexicon_count = textstats.lexicon_count(text=test_data, removepunct=True)
    sentence_count = textstats.sentence_count(test_data)
    polysyllabcount = textstats.polysyllabcount(test_data)
    avg_sentence_per_word = textstats.avg_sentence_per_word(test_data)
    word_count = count_word(test_data)
    pos_count = count_pos(test_data)
    flesch_reading_ease = textstats.flesch_reading_ease(test_data)
    smog_index = textstats.smog_index(test_data)
    flesch_kincaid_grade = textstats.flesch_kincaid_grade(test_data)
    coleman_liau_index = textstats.coleman_liau_index(test_data)
    automated_readability_index = textstats.automated_readability_index(test_data)
    dale_chall_readability_score = textstats.dale_chall_readability_score(test_data)
    difficult_words = textstats.difficult_words(test_data)
    linsear_write_formula = textstats.linsear_write_formula(test_data)
    gunning_fog = textstats.gunning_fog(test_data)
    text_standard = textstats.text_standard(test_data)
    stemmed_text = stem_text(test_data)
    result = {
        "original_text": test_data,
        "syllable_count": syllable_count,
        "lexicon_count": lexicon_count,
        "sentence_count": sentence_count,
        "avg_sentence_per_word": avg_sentence_per_word,
        "word_count": word_count,
        "pos_count": pos_count,
        "flesch_reading_ease": flesch_reading_ease,
        "smog_index": smog_index,
        "flesch_kincaid_grade": flesch_kincaid_grade,
        "coleman_liau_index": coleman_liau_index,
        "automated_readability_index": automated_readability_index,
        "dale_chall_readability_score": dale_chall_readability_score,
        "difficult_words": difficult_words,
        "linsear_write_formula": linsear_write_formula,
        "gunning_fog": gunning_fog,
        "polysyllabcount": polysyllabcount,
        "text_standard": text_standard,
        "stemmed_text": stemmed_text
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run()
