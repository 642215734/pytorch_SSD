#!/usr/bin/python

# pip install lxml
#读取voc文件夹，返回所有类别的json
import sys
import os
import json
import xml.etree.ElementTree as ET

XML_DIR = '/home/zlatan/Database/VOCdevkit/VOC2007/Annotations'
START_BOUNDING_BOX_ID = 1
PRE_DEFINE_CATEGORIES = {}


# If necessary, pre-define category and its id
#  PRE_DEFINE_CATEGORIES = {"aeroplane": 1, "bicycle": 2, "bird": 3, "boat": 4,
#  "bottle":5, "bus": 6, "car": 7, "cat": 8, "chair": 9,
#  "cow": 10, "diningtable": 11, "dog": 12, "horse": 13,
#  "motorbike": 14, "person": 15, "pottedplant": 16,
#  "sheep": 17, "sofa": 18, "train": 19, "tvmonitor": 20}


def get(root, name):
    vars = root.findall(name)
    return vars


def get_and_check(root, name, length):
    vars = root.findall(name)
    if len(vars) == 0:
        raise NotImplementedError('Can not find %s in %s.' % (name, root.tag))
    if length > 0 and len(vars) != length:
        raise NotImplementedError('The size of %s is supposed to be %d, but is %d.' % (name, length, len(vars)))
    if length == 1:
        vars = vars[0]
    return vars


def get_filename_as_int(filename):
    try:
        filename = os.path.splitext(filename)[0]
        return int(filename)
    except:
        raise NotImplementedError('Filename %s is supposed to be an integer.' % (filename))


def VOC_get_categories(xml_dir=XML_DIR):
    # print(os.path.exists(xml_dir))
    categories = PRE_DEFINE_CATEGORIES
    bnd_id = START_BOUNDING_BOX_ID
    for root, dirs, files in os.walk(xml_dir):
        for name in files:
            # print(name)
            # print(os.path.join(root, name))
            xml_file = os.path.join(root, name)

            xml_f = open(xml_file, 'r')

            tree = ET.parse(xml_f)
            tree_root = tree.getroot()

            ## Cruuently we do not support segmentation
            #  segmented = get_and_check(root, 'segmented', 1).text
            #  assert segmented == '0'
            for obj in get(tree_root, 'object'):
                category = get_and_check(obj, 'name', 1).text
                if category not in categories:
                    new_id = len(categories) + 1
                    categories[category] = new_id
                category_id = categories[category]
                bndbox = get_and_check(obj, 'bndbox', 1)

                bnd_id = bnd_id + 1
            xml_f.close()

    for cate, cid in categories.items():
        cat = {'id': cid, 'name': cate}
        # print(cat)
    # print(len(categories))
    return categories


if __name__ == '__main__':
    # if len(sys.argv) < 1:
    #     print('1 augument are need.')
    #     print('Usage: %s XML_LIST.txt XML_DIR OUTPU_JSON.json'%(sys.argv[0]))
    #     exit(1)

    categories = VOC_get_categories()
    print(categories)
    print([*categories])

