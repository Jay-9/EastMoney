from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas
import time
import datetime


def info_collect(stock_num):
    the_stock = []
    for x in range(1, 19):
        the_stock.append(brower.find_element_by_xpath('//*[@id="table_wrapper-table"]/tbody/tr[%d]/td[%d]' % (stock_num, x)).text)
    return the_stock


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    brower = webdriver.Chrome(options=chrome_options)
    brower.get('http://quote.eastmoney.com/center/gridlist.html#hs_a_board')

    stock_index = []
    for i in range(1, 19):
        stock_index.append(brower.find_element_by_xpath('//*[@id="table_wrapper-table"]/thead/tr/th[%d]/span' % i).text)

    all_stock_info = pandas.DataFrame(index=stock_index)

    for _ in range(1, 11):  # 每页20个,200个需3‘27s
        for i in range(1, 21):
            stock = info_collect(i)
            all_stock_info[stock[0]] = stock
        brower.find_element_by_xpath('//*[@id="main-table_paginate"]/a[2]').click()
        time.sleep(3)

    all_stock_info.to_csv('a.csv', header=False, encoding="utf_8_sig")
    brower.close()
    brower.quit()
    print(start_time, '\t', datetime.datetime.now(), '\n', datetime.datetime.now() - start_time)
