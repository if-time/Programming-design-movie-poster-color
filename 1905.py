import os
import requests
from lxml import etree
import re 

# 负责下载电影海报


def download_img(title, img_addr, headers, time):

    # 如果不存在图片文件夹,则自动创建
    if os.path.exists("./Top250_movie_images/"):
        pass
    else:
        os.makedirs("./Top250_movie_images/")
    if os.path.exists("./Top250_movie_images/" + time + "/"):
        pass
    else:
        os.makedirs("./Top250_movie_images/" + time + "/")

    # 获取图片二进制数据
    image_data = requests.get(img_addr, headers=headers).content
    # 设置海报存存储的路径和名称
    image_path = "./Top250_movie_images/" + time + "/" + title[0] + '.jpg'
    # 存储海报图片
    with open(image_path, "wb+") as f:
        f.write(image_data)


# 根据url获取数据,并打印到屏幕上,并保存为文件
def get_movies_data(url, headers):

    # 获取页面的响应内容
    db_response = requests.get(url, headers=headers)

    # 将获得的源码转换为etree
    db_reponse_etree = etree.HTML(db_response.content)

    # 提取所有电影数据
    db_movie_items = db_reponse_etree.xpath('//*[@class="fl line"]/a')
    print(len(db_movie_items))
    # 遍历电影数据列表,
    for db_movie_item in db_movie_items:

        # 这里用到了xpath的知识
        db_title = db_movie_item.xpath('img/@alt')
        print(db_title)
        db_date = db_movie_item.xpath('img/@data-original')
        db_img_addr = db_movie_item.xpath('img/@src')
        
        word = 'uploadfile' 
        index = [m.start() + 11 for m in re.finditer(word, str(db_date[0]))]
        print(index)
        db_movie_date = db_date[0][index[0]:index[0]+4]
        print("标题:", db_title[0]+" 时间:", db_movie_date + " URL:", db_date[0])
        # a表示追加模式, b表示以二进制方式写入, + 表示如果文件不存在则自动创建
        with open("./douban_movie_top250.txt", "ab+") as f:
            tmp_data = "标题:"+str(db_title)+ "-" + str(db_movie_date) + "\n"
            f.write(tmp_data.encode("utf-8"))

        db_img_addr = str(db_img_addr[0].replace("\'", ""))
        download_img(db_title, db_img_addr, headers, str(db_movie_date))


def main():
    # 使用列表生成式,生成待爬取的页面url的列表
    urls = []
    for i in range(5, 107):
        urls.append("http://www.1905.com/mdb/film/list/country-China/o0d0p"+str(i)+".html")
    # urls = ["[图片]http://www.1905.com/mdb/film/list/country-China/o0d0p"+str(i*1) for i in range(5,108)+".html"]

    # 设置请求头
    headers = {
        # 设置用户代理头(为狼披上羊皮)
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }

    # 为避免重复运行程序,造成内容重复,这里把上次的文件清除(可跳过)
    if os.path.isfile("./douban_movie_top250.txt"):
        os.remove("./douban_movie_top250.txt")

    # 从列表取出url进行爬取
    for url in urls:
        get_movies_data(url, headers)


if __name__ == '__main__':
    main()
