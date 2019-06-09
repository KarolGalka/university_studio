import json

import requests

import unicodedata

'''
Source: https://cloud.ibm.com/docs/services/natural-language-understanding?topic=natural-language-understanding-getting-started#getting-started-tutorial
Used https://curl.trillworks.com to translate curl from source
'''

IBM_API_KEY = "cbGnqfMQ7IF0rLqOo9uygpT0MoSjWvzTL0Oh2f6XB-kC"
IBM_API_URL = "https://gateway-lon.watsonplatform.net/natural-language-understanding/api"


def _normalize_char(c):
    try:
        cname = unicodedata.name(c)
        cname = cname[:cname.index(' WITH')]
        return unicodedata.lookup(cname)
    except (ValueError, KeyError):
        return " "  # c


def _replace_polish_signs(text: str):
    # polish_chars = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ż', 'ź']
    # replace_chars = ['a', 'c', 'e', 'l', 'n', 'o', 's', 'z', 'z']
    # char_dict = dict(zip(polish_chars, replace_chars))
    cleared_text = ""
    for char in text:
        cleared_text += _normalize_char(char)  # char_dict.get(character, character)
    return text


def _get_categories_from_text(text):
    clear_text = str(unicodedata.normalize('NFD', text).encode('ascii', 'ignore'))
    # clear_text = re.sub("[^a-zA-Z,. ]", "", clear_text)
    s = requests.Session()
    headers = {"Content-Type": "application/json"}
    params = (
        ('version', '2018-11-16'),
    )
    data = '{\n  "text": "' + clear_text + '",\n  "features": {\n    "categories": {\n    }\n    }\n}'
    # data = '{\n  "text": "I love apples! I do not like oranges.",\n  "features": {\n    "categories": {\n    }\n    }\n}'
    s.headers.update(headers)
    response = requests.post('https://gateway-lon.watsonplatform.net/natural-language-understanding/api/v1/analyze',
                      headers=headers, params=params, data=data, auth=('apikey', IBM_API_KEY))
    if response.status_code == 200:
        response_json = json.loads(response.text)
        text_analysis = {"categories": response_json["categories"], "signs": response_json["usage"]["text_characters"]}
        return text_analysis
    else:
        return {}

# text = "I like sport, mostly football. Robert Lewandowski is my favorite player. I like going to gym aswell"
# print(get_categories_from_text(text))
