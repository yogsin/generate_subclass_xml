#!/usr/bin/evn python 
#coding:utf-8 

import os
import sys 

VOC2012_path = "/home/work/DataSource/VOCdevkit/VOC2012/"
VOC2007_path = "/home/work/DataSource/VOCdevkit/VOC2007/"
VOC2012_trainval_name_file = VOC2012_path + "ImageSets/Main/trainval.txt"
VOC2007_trainval_name_file = VOC2007_path + "ImageSets/Main/trainval.txt"
VOC2007_test_name_file = VOC2007_path + "ImageSets/Main/test.txt"
VOC0712_trainval_list_file = "/home/work/username/caffe/data/VOC0712/trainval_cat_dog.txt"
VOC0712_test_list_file = "/home/work/username/caffe/data/VOC0712/test_cat_dog.txt"
DATA_path = [VOC2012_path, VOC2007_path]

def read_file(filename):
    name_list = []
    with open(filename, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline().strip() # 整行读取数据
            if not lines:
                break
                pass
            #p_tmp, E_tmp = [float(i) for i in lines.split()] # 将整行数据分割处理
            name_list.append(lines)  # 添加新读取的数据
            pass
        pass
    print name_list
    return name_list

def write_file(file_name, name_list):
    f = open(file_name,'w')
    for lines in name_list:
        f.write(lines + '\n')
    f.close()

for VOC_path in DATA_path:
    xml_file_list = os.listdir(VOC_path + "Annotations_cat_dog")
    source_name_list = read_file(VOC_path + "ImageSets/Main/trainval.txt")
    dest_name_list = []
    for xml_name in xml_file_list:
        if xml_name[0:-4] in source_name_list:
            dest_name_list.append(xml_name[0:-4])
    write_file(VOC_path + "ImageSets/Main/trainval_cat_dog.txt", dest_name_list)
    if VOC_path == VOC2007_path:
        source_name_list = read_file(VOC_path + "ImageSets/Main/test.txt")
        dest_name_list = []
        for xml_name in xml_file_list:
            if xml_name[0:-4] in source_name_list:
                dest_name_list.append(xml_name[0:-4])
        write_file(VOC_path + "ImageSets/Main/test_cat_dog.txt", dest_name_list)
