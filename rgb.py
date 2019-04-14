from PIL import Image
import numpy
import csv
import codecs
import os
import re


def data_write_csv(file_name, datas):  # file_name为写入CSV文件的路径，datas为要写入数据列表
    file_csv = codecs.open(file_name, 'w+', 'utf-8')  # 追加
    writer = csv.writer(file_csv, delimiter=' ',
                        quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in datas:
        writer.writerow(data)
    print("保存文件成功，处理结束")


def text_save(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace(
            '[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")


def list_all_files(rootdir):
    import os
    _files = []
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
            print(path)
            name = path[22:]
            toRGB(name)
            # print(name)
    return _files


def toRGB(name):
    time = name[:4]
    title = name[5:-4]
    
    print(title + " " + time)
    img = Image.open("C:\\Users\\Ifand\\Top250_movie_images\\" + name)
    img_array = img.load()
    width, height = img.size
    all_pixels = []
    for x in range(width):
        for y in range(height):
            cpixel = img_array[x, y]
            all_pixels.append(cpixel)
    # print(img_array[6, 4])
    print(len(all_pixels))

     # 如果不存在文件夹,则自动创建
    if os.path.exists("./Top250_movie_images/RGBFiles"):
        pass
    else:
        os.makedirs("./Top250_movie_images/RGBFiles")
    if os.path.exists("./Top250_movie_images/RGBFiles/" + time + "/"):
        pass
    else:
        os.makedirs("./Top250_movie_images/RGBFiles/" + time + "/")

    # data_write_csv("./Top250_movie_images/RGBFiles/" + time + "/" + title + ".csv", all_pixels)
    text_save("./Top250_movie_images/RGBFiles/" + time + "/" + title + ".txt", all_pixels)


def main():

    _fs = list_all_files('./Top250_movie_images')
    print(len(_fs))


if __name__ == '__main__':
    main()

# i = Image.open(r"C:\Users\Ifand\Top250_movie_images\2019\“大”人物.jpg")
# pixels = i.load() # this is not a list
# width, height = i.size
# row_averages = []
# for y in range(height):
#     cur_row_ttl = 0
#     for x in range(width):
#         cur_pixel = pixels[x, y]
#         cur_pixel_mono = sum(cur_pixel) / len(cur_pixel)
#         cur_row_ttl += cur_pixel_mono

#     cur_row_avg = cur_row_ttl / width
#     row_averages.append(cur_row_avg)

# print("Brighest row:",)
# print (max(row_averages))

# 使用PIL 写入像素点画图片
# img = Image.new("RGB", (5, 5))  # 创建一个5*5的图片
# pixTuple = (255, 0, 255, 15)  # 三个参数依次为R,G,B,A   R：红 G:绿 B:蓝 A:透明度
# for i in range(5):
#     for j in range(5):
#         img.putpixel((i, j), pixTuple)
# img.save("bb.png")

# 如何用python分别提取出某个像素的rgb值并写入一个一行三列的数组中
# result = np.zeros((3))
# sumC = np.zeros((3))
# for i in range(2*radius):
# for j in range(2*radius):
# if((cx-radius+i) > 0 and (cy-radius+j) > 0 and i < radius and j < radius):
# sumC[0, :, :] = sumC[0, :, :] + img[cx, cy, R]
# sumC[:, 0, :] = sumC[:, 0, :] + img(cx, cy, G)
# sumC[:, :, 0] = sumC[:, :, 0] + img(cx, cy, B)
