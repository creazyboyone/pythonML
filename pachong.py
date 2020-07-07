import requests
from lxml import html
content = []
for i in range(45686, 45809):
    url = "https://www.qeto.com/article_" + str(i) + '/'
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/79.0.3945.130 Safari/537.36 "
    }
    page = requests.Session().get(url, headers=header)
    tree = html.fromstring(page.text)
    result = tree.xpath('//div[@itemprop="text"]/text()')
    content.extend(result)
    print(content)
