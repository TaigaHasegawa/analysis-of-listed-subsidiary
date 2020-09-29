# coding: utf-8
import numpy as np 
import pandas as pd
import glob
import openpyxl
import os
from tqdm import tqdm

from utils import *
from settings import *


def main():

    bs_asset_list = glob.glob(os.path.join(BS_ASSET_DIR,"*.xlsx"))
    bs_debt_list = glob.glob(os.path.join(BS_DEBT_DIR,"*.xlsx"))
    cf_list = glob.glob(os.path.join(CF_DIR,"*.xlsx"))
    pl_list = glob.glob(os.path.join(PL_DIR,"*.xlsx"))
    base_info_list = glob.glob(os.path.join(BASE_INFO_DIR,"*.xlsx"))
    attribute_file = ATTRIBUTE_FILE
    officer_summary = os.path.join(BOARD_DIR,"役員サマリー.csv")
    officer_detail = os.path.join(BOARD_DIR,"役員詳細.csv")

    bs_asset_df = extract_data_function(bs_asset_list,num_years=5,num_cols=5)
    bs_debt_df = extract_data_function(bs_debt_list,num_years=15,num_cols=6)
    df = bs_asset_df.merge(bs_debt_df, how="inner", on=["決算期", "ticker_code"])
    cf_df = extract_data_function(cf_list,num_years=15,num_cols=4)
    df = df.merge(cf_df, how="inner", on=["決算期", "ticker_code"])
    pl_df = extract_data_function(pl_list,num_years=15,num_cols=5)
    df = df.merge(pl_df, how="inner", on=["決算期", "ticker_code"])
    base_info_df = extract_data_function(base_info_list,num_years=15,num_cols=7)
    df = df.merge(base_info_df, how="left", on=["決算期", "ticker_code"])

    attribute_df = extract_data_function_for_attribute(attribute_file)
    attribute_df["株式コード（固有名コード）"] = attribute_df["株式コード（固有名コード）"].astype(str)
    df = df.merge(attribute_df, how="left", left_on=["ticker_code"], right_on=["株式コード（固有名コード）"])

    df["決算期"] = pd.to_datetime(df["決算期"], format="%Y/%m", errors="coerce")

    #officer_summary_df = pd.read_csv(officer_summary,  encoding="shift-jis", header=None, usecols=[1,7,8,9,10,11,12,13,14,15,16,17,18,21], names=["ticker_code","決算期",
    #    "連結/単独フラグ", "連番","指名委員会", "監査等委員会", "執行役員制度", "取締役人数", "社外取締役人数", "社外監査役人数", "執行役員人数", "監査等委員人数", "社外監査等委員人数", "役員女性比率"])
    
    #officer_summary_df = officer_summary_df[officer_summary_df["連番"]==1]
    #officer_summary_df["決算期"] = pd.to_datetime(officer_summary_df["決算期"], format="%Y%m", errors="coerce")
    
    #nikkei_heikin_df = pd.read_csv(nikkei_heikin)
    #nikkei_heikin_df["決算期"] = pd.to_datetime(nikkei_heikin_df["決算期"], format="%Y-%m-%d", errors="coerce")

    #nikkei_heikin_df_merge = nikkei_heikin_df.merge(officer_summary_df, how="left", on=["ticker_code","決算期"]
    
    file_name = "processed_data.csv"
    df.to_csv(os.path.join(PROCESSED_DIR, file_name), encoding='utf_8_sig', index=False)

if __name__ == "__main__":
    main()