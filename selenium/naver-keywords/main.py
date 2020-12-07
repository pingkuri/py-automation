from bs4 import BeautifulSoup
from selenium import webdriver


def save_data(data, filename):
    with open(filename, 'w', encoding="UTF8") as result:
        for item in data.values():
            result.write(item + "\n")

def get_naver_keyword():
    
    driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://datalab.naver.com/keyword/realtimeList.naver?where=main")

    soup = BeautifulSoup(driver.page_source, "html.parser")
    keywords=soup.select("span.item_title")
    
    index=1
    data = {}
    for key in keywords:
        data[index] = key.get_text()
        index+=1

    print("---finish---")
    print(data)
    save_data(data, "result.txt")
    driver.close()
    
    
if __name__ == "__main__":
    get_naver_keyword()
