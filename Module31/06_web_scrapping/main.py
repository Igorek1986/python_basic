import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    def parsing_html(url: str, result: list = []) -> None:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        text = soup.find_all('h3')


        # TODO, предлагаю упростить строки ниже до одной строки кода List comprehensions.
        for elem in text:
            result.append(elem.next_element)


    header_lst = []
    parsing_html('http://www.columbia.edu/~fdc/sample.html', result=header_lst)
    print(header_lst)
