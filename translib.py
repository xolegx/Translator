import requests


def get_html(url):
    return requests.get(url).text


def save_file(url, name):
    r = requests.get(url, stream=True)
    with open(name, 'bw') as f:
        f.write(r.content)


def get_translation(text, lang):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    KEY = 'trnsl.1.1.20190417T123920Z.39e232ae5fd950ca.0431bdf3a7a4cb94bfb9efacfe2d1045f6325763'
    TEXT = text
    LANG = lang

    r = requests.post(URL, data={'key': KEY, 'text': TEXT, 'lang': LANG})
    print(r)
    return eval(r.text)
