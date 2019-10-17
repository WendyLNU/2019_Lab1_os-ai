import numpy as np
import xlrd
import xlwt
# from sklearn import preprocessing # 进行标准化数据时，需要引入这个包
from sklearn.model_selection import train_test_split
#


def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))
#
def split_age_range(user_id):
    """

    将特征值年龄进行离散化为8个特征值
    :param age: 年龄区间值
    :return: 离散化后的特征

    """
    if user_id >0 and user_id<=50000:
        return [1,0,0,0,0,0,0,0,0]
    elif user_id >50000 and user_id<=100000:
        return [0,1,0,0,0,0,0,0,0]
    elif user_id >100000 and user_id<=150000:
        return [0,0,1,0,0,0,0,0,0]
    elif user_id >150000 and user_id<=200000:
        return [0,0,0,1,0,0,0,0,0]
    elif user_id >200000 and user_id<=250000:
        return [0,0,0,0,1,0,0,0,0]
    elif user_id >250000 and user_id<=300000:
        return [0,0,0,0,0,1,0,0,0]
    elif user_id >300000 and user_id<=350000:
        return [0,0,0,0,0,0,1,0,0]
    elif user_id >350000 :
        return [0,0,0,0,0,0,0,1,0]
    # elif age == 8:
    #     return [0,0,0,0,0,0,0,0,1]

def split_gender(merchant_id):
    """

    将特征值性别进行离散化
    :param gender:
    :return: 返回离散化的特征

    """
    if merchant_id >0 and merchant_id<=3000:
        return [1,0,0]
    elif merchant_id >3000:
        return [0,1,0]
#    elif gender == 2:
#        return [0,0,1]

def split_log(prob):


#    分割数据文件中的Log数据
 #   :param Log: Log数据
  #  :return: 处理后的特征值


    items = Log.strip().split('#')
    purchase = 0;total = 0
    click = 0;add_to_card = 0;add_to_favourite = 0
    for i in range(len(items)):
        total += 1
        item = items[i].strip().split(':')
        if item[4] == '2':
            purchase += 1
        if item[4] == '1':
            add_to_card += 1
        if item[4] == '3':
            add_to_favourite += 1
    return [float(total),float(round(purchase/total,3)),float(add_to_card),float(add_to_favourite)]

def loadDataSet(path, training_sample,colnameindex=0,by_name=u's1'):
    """

    加载数据

    :param path: 数据文件存放路径
    :param training_sample: 数据文件名
    :param colnameindex: 文件列名下标
    :param by_name: 表名
    :return: 数据集和类别标签

    """
    dataMat = [];
    labelMat = []  # 定义列表
    filename = path + training_sample
    print(filename)
    data = open_excel(filename)
    table = data.sheet_by_name(by_name) # 获得表格
    nrows = table.nrows  # 拿到总共行数
    colnames = table.row_values(colnameindex)  # 某一行数据 ['user_id', 'age_range', 'gender', 'merchant_id','label']
    for rownum in range(1, nrows):  # 也就是从Excel第二行开始，第一行表头不算
        row = table.row_values(rownum)
        if row[1] == '' or row[2] == '' or row[5] == '':
            continue
        if row:
            app = []
            app = split_age_range(row[1])+split_gender(row[2]) + split_log(row[5]) # 将Log转化为特征值
            dataMat.append(app)
            labelMat.append(float(row[4])) # 获取类别标签
    return dataMat, labelMat
#
#
#
def main():
    """
    主函数
    :return: null

    """
    wb = xlwt.Workbook()
    ws = wb.add_sheet('s1',cell_overwrite_ok=True)
    path = "D:\\"
    training_sample = 'samplesubmission.csv' # 训练数据文件
    trainingSet, trainingLabels = loadDataSet(path, training_sample)  # 取训练数据
    # print(len(trainingSet))
    num = len(trainingSet)
    for i in range(num):
        for j in range(16):
            ws.write(i,j,trainingSet[i][j])
        ws.write(i,j+1,trainingLabels[i])
    wb.save('D:/schoolwork/featuredata.xls')
    print("处理完成")

if __name__ == '__main__':
    """
    程序入口
    """
    main()

