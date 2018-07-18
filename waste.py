import re
import requests
from urllib import parse


def get_html(link):
    print('REQUESTS -> ' + str(link))
    headers = {
        'user-agent':
            'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0)'
            ' Gecko/20100101 Firefox/38.0',
    }
    s = requests.Session()
    response = s.get(link, headers=headers, timeout=15)
    html = str(response.text)
    return html


def get_info(url):
    res = []
    for link in url:
        html = get_html(link)
        dates = re.search(r'content" class="listof">([\s\S]*?)<script', html)
        dates = dates.group(1) if dates else ''
        dates = dates.replace('>SOLD OUT - MORE INFO</a>',
                              '>SOLD OUT - MORE INFO</a><br><br>').replace(
                              '>ON SALE NOW</a>', '>>ON SALE NOW</a><br><br>')
        res.append(dates)
    text = ''.join(res)
    return text


def main(url):
    return(get_info(url))


if __name__ == "__main__":
    main()
