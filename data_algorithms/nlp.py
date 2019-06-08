
import requests
# import config

'''
    Source: https://cloud.ibm.com/docs/services/natural-language-understanding?topic=natural-language-understanding-getting-started#getting-started-tutorial
Used https://curl.trillworks.com to translate curl from source
'''
# TODO use config
IBM_API_KEY = "cbGnqfMQ7IF0rLqOo9uygpT0MoSjWvzTL0Oh2f6XB-kC"



def get_categories_from_text(text):

    IBM_API_URL = "https://gateway-lon.watsonplatform.net/natural-language-understanding/api"

    s = requests.Session()
    headers= {"Content-Type": "application/json"}
    params = (
        ('version', '2018-11-16'),
    )
    data = '{\n  "text": "' + text + '",\n  "features": {\n    "categories": {\n    }\n    }\n}'
    # data = '{\n  "text": "I love apples! I do not like oranges.",\n  "features": {\n    "categories": {\n    }\n    }\n}'
    s.headers.update(headers)
    r = requests.post('https://gateway-lon.watsonplatform.net/natural-language-understanding/api/v1/analyze', headers=headers, params=params, data=data.encode('utf-8'), auth=('apikey', IBM_API_KEY))
    return r.text


# text = "I like sport, mostly football. Robert Lewandowski is my favorite player. I like going to gym as well"
# print(get_categories_from_text(text))