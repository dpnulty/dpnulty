import pytest
from bs4 import BeautifulSoup


def test_html_parses():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    assert soup is not None

