#!/usr/bin/evn python 
#coding:utf-8 

import os
import sys
try:
    import xml.etree.cElementTree as ET 
except ImportError: 
    import xml.etree.ElementTree as ET 
import sys 

VOC2012_path = "/home/work/DataSource/VOCdevkit/VOC2012/"
VOC2007_path = "/home/work/DataSource/VOCdevkit/VOC2007/"
DATA_path = [VOC2012_path, VOC2007_path]
for VOC_path in DATA_path:
    xml_file_list = os.listdir(VOC_path + "Annotations")
    if not os.path.exists(VOC_path + "Annotations_cat_dog"):
        os.mkdir(VOC_path + "Annotations_cat_dog")
    for xml_name in xml_file_list:
        try:
            tree = ET.parse(VOC_path + "Annotations/" + xml_name)     #打开xml文档 
            #root = ET.fromstring(country_string) #从字符串传递xml 
            annotation = tree.getroot()         #获得root节点  
        except Exception, e: 
            print "Error:cannot parse file:2007_003188.xml."
            sys.exit(1) 
        #print annotation.tag, "---", annotation.attrib  
        #for child in annotation: 
            #print child.tag, "---", child.attrib 

        #print "*"*10
        #print root[0][1].text   #通过下标访问 
        #print root[0].tag, root[0].text 
        #print "*"*10
        
        for object in annotation.findall('object'): #找到root节点下的所有country节点 
            #rank = country.find('name').text   #子节点下节点rank的值 
                #name = country.get('name')      #子节点下属性name的值 
            #print name, rank 
            name = object.find('name').text   #子节点下节点rank的值 
            print name 

        has_cat_or_dog = False
        #修改xml文件 
        for object in annotation.findall('object'): 
            name = object.find('name').text 
            if name != "cat" and name != "dog": 
                annotation.remove(object)
            else:
                has_cat_or_dog = True
        if has_cat_or_dog:
            print "find cat or dog! writing new xml file..."
            tree.write(VOC_path + "Annotations_cat_dog/" + xml_name)
            print "done!"
            has_cat_or_dog = False
