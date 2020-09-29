import sys, os
import pandas as pd
# from dotenv import load_dotenv
import datetime
import distutils.util

## settings for directories
ROOT_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BS_ASSET_DIR  = os.path.join(ROOT_DIR,'data','BS資産')
BS_DEBT_DIR     = os.path.join(ROOT_DIR,'data','BS負債純資産')
CF_DIR  = os.path.join(ROOT_DIR,'data','CF')
PL_DIR = os.path.join(ROOT_DIR,'data','PL')
BASE_INFO_DIR = os.path.join(ROOT_DIR,'data','基本項目')
ATTRIBUTE_FILE = os.path.join(ROOT_DIR,'data','企業属性','東証ジャスダック全社.xlsx')
ATTRIBUTE_DIR = os.path.join(ROOT_DIR,'data','マサ_企業属性')
BOARD_DIR = os.path.join(ROOT_DIR,'data','取締役')
PROCESSED_DIR = os.path.join(ROOT_DIR,'data','加工済み')
SEGMENT_DIR = os.path.join(ROOT_DIR,'data','セグメント')