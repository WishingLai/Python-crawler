import urllib.request as req
import bs4


def getData(url):
    # 送出 req ,cookie 附上資訊 讓網站覺得是使用者而非爬蟲
    request=req.Request(url, headers={
        "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "cookie":"over18=1"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    #print(data)

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:# 如果標題包含 a 就印出來
            print(title.a.string)

    # 上一頁的連結抓取
    nextlink=root.find("a", string="‹ 上頁")
    #print(nextlink)
    return nextlink["href"]


url="https://www.ptt.cc/bbs/Gossiping/index.html"

count=0
while count<10:
    print(count)
    url="https://www.ptt.cc" + getData(url)
    count+=1

#print(titles.a.string)