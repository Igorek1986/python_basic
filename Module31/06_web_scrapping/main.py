import requests
from bs4 import BeautifulSoup
from typing import List


if __name__ == '__main__':
    def parsing_html(url: str) -> List[str]:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        text = soup.find_all('h3')
        return [elem.next_element for elem in text]


    header_lst = parsing_html('http://www.columbia.edu/~fdc/sample.html')
    print(header_lst)
