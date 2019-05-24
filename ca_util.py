# -*- coding: utf-8 -*-

"""
create data : 2019-05-18
description : campaign assistant 유틸리티 함수
"""

#import 
import numpy as np
import random, re
import os
import pandas as pd 

# 로그 프린트
def log_print(log):
	print("-"*50)
	print(log)
	print("-"*50)

# file parsing
def conf_parsing(filename):
    try:
        parameter = {}

        f = open(filename, encoding='utf-8')
        data = f.readlines()

        for line in data:
            if not line.strip() or line[0] =='#':
                continue
            else:
                #print(line)
                key, value = line.split("=")
                parameter[key.strip()] = value.strip()
        f.close()
        return parameter
    except OSError:
        print('No such file or directory: ',filename)

# create-folder
def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. '+ directory)

# 리스트를 딕션러리 변환
def lsit_to_dic(listdata):
    dic_data = {}

    for data in listdata:
        data_split = data.split(':')

        # 문자열 데이터를 숫자로 변환하기 
        #value
        #fn = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n
        #list(map(fn, value))

        key     = data_split[0]
        value   = data_split[1]

        dic_data[key] = (value)
    return dic_data
    
# 표준화
def standardization(data):
    try:
        numerator = data - np.mean(data, 0)
        denominator = np.std(data, 0)
        # noise term prevents the zero division
        return round(numerator / (denominator + 1e-7),2)
    except ValueError as e:
        print(e)
    finally:
        None

# 정규화
def normalization(data):
    try:
        numerator = data - np.min(data, 0)
        denominator = np.max(data, 0) - np.min(data, 0)
        # noise term prevents the zero division
        return round(numerator / (denominator + 1e-7),2)
    except ValueError as e:
        print(e)
    finally:
        None
