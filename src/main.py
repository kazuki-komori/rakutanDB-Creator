# coding=utf-8
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time




def main():
    URL = 'https://duet.doshisha.ac.jp/kokai/html/fi/fi020/FI02001G.html'

    Params = '?form1%3AselectedIndex=0&form1%3AselectedPage=1&form1%3AtopPosition=0&form1%3AkaikoNendolist=2019&form1%3A_id78=&form1%3A_id82=1&form1%3A_id86=11008&form1%3A_id90=&form1%3A_id92=&form1%3A_id104=&form1%3A_id116=&form1%2Fhtml%2Ffi%2Ffi020%2FFI02001G.html=form1&form1%3A__link_clicked__=form1%3AdoKensaku'

    url = URL + Params
    options = Options()
    # Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
    options.add_argument("--headless")

    options.add_argument(
        '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 Mobile/14C92 Safari/602.1'
    )

    # ブラウザを起動する
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=options)

    print(url)
    # ブラウザでアクセスする
    driver.get(url)
    driver.refresh()
    time.sleep(3)
    res = driver.page_source
    print(res)

    # HTMLを文字コードをUTF-8に変換してから取得します。

    soup = BeautifulSoup(res, 'html.parser')
    print(soup)
    print(res)

main()
