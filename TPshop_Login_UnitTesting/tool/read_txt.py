def read_txt(filename):
    filepath = "../data/"+ filename
    with open(filepath, "r", encoding="utf-8")as f:
        return f.readlines()

if __name__ == '__main__':
    # datas = read_txt("login.txt")
    # arrs = []
    # for data in datas:
    #     arrs.append(tuple(data.strip().split(",")))
    # print(arrs)


    # 写法：
    arr = []
    for data in read_txt("login.txt"):
        arr.append(tuple(data.strip().split(",")))
    print(arr)

    """
        难点：
            1. 去除字符串前后空格、换行符  strip()
            2. 使用split(",")拆分字符串，结果返回列表
            3. 使用tuple()将返回的列表强转为元祖
    """