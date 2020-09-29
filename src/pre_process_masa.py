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
    attribute_list = glob.glob(os.path.join(ATTRIBUTE_DIR,"*.xlsx"))
    segment_list = glob.glob(os.path.join(SEGMENT_DIR,"*.xlsx"))

    pl_df = extract_data_function(pl_list,num_years=15,num_cols=5)
    segment_df = extract_data_function_for_masa_2(segment_list,num_years=16,num_cols=9)
    df = pl_df.merge(segment_df, how="inner", on=["決算期", "ticker_code"])
    attribute_df = extract_data_function_for_masa(attribute_list, 6)
    attribute_df["株式コード（固有名コード）"] = attribute_df["株式コード（固有名コード）"].astype(str)
    df = df.merge(attribute_df, how="left", left_on=["ticker_code"], right_on=["株式コード（固有名コード）"])

    df["決算期"] = pd.to_datetime(df["決算期"], format="%Y/%m", errors="coerce")
    
    file_name = "processed_data_for_masa.csv"
    df.to_csv(os.path.join(PROCESSED_DIR, file_name), encoding='utf_8_sig', index=False)

if __name__ == "__main__":
    main()