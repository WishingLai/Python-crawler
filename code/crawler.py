
import urllib.request as req
import bs4

url="https://www.ptt.cc/bbs/movie/index.html"

# 送出req 附上資訊 讓網站覺得是使用者而非爬蟲
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
})
with req.urlopen(request)as response:
    data=response.read().decode("utf-8")

#print(data)

root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title")
for title in titles:
    if title.a != None:
        print(title.a.string)


#print(titles.a.string)