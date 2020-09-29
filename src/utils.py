# coding: utf-8
import numpy as np 
import pandas as pd
import glob
import openpyxl
import os
from tqdm import tqdm

from settings import *


def extract_data_function(file_name_list, num_years, num_cols):
    
    df_output = pd.DataFrame()
    use_cols_list = [0,1,2] + list(range(5,5+num_years))

    for file_name in file_name_list:

        file = pd.ExcelFile(file_name)

        for sheetName in file.sheet_names[1:]:
            #usecolsは使用したいカラムのインデックス。各エクセルファイルの取り出した年度数に応じて変わりうる。
            df = file.parse(sheetName, header=None, index_col=2, skiprows=list(range(0,8)), usecols=use_cols_list)
            processed_df = pd.DataFrame()
            index_list = np.where([~df.reset_index().iloc[:,1].duplicated()])[1]
            for i, index in tqdm(enumerate(index_list)):
                if i+1 == len(index_list):
                    ticker_df = df.iloc[index:,:]
                else:
                    ticker_df = df.iloc[index:index_list[i+1],:]
                if len(ticker_df)!=num_cols:
                    continue
                ticker_df = ticker_df.T
                ticker_df["ticker_name"] = [ticker_df.iloc[0,0]]*len(ticker_df)
                ticker_df["ticker_code"] = [ticker_df.iloc[1,0][1:]]*len(ticker_df)
                ticker_df = ticker_df.iloc[2:,:]
                processed_df = pd.concat([processed_df, ticker_df])

            processed_df = processed_df.replace("-", np.nan)
            df_output = pd.concat([df_output, processed_df])
            df_output = df_output.dropna(subset=["決算期"])
    
    return df_output


def extract_data_function_for_attribute(file_name):
    
    df_output= pd.DataFrame()

    file = pd.ExcelFile(file_name)

    for sheetName in tqdm(file.sheet_names[1:]):
        #usecolsは使用したいカラムの番号。各エクセルファイルの取り出した年度数に応じて変わりうる。
        df = file.parse(sheetName, skiprows=[0,1,3,4], header=[0], usecols=[2,3,4,5,6])
        df_output = pd.concat([df_output, df])
    
    return df_output


def extract_data_function_for_masa(file_name_list, num_cols):
    
    df_output = pd.DataFrame()
    use_cols_list = [0,1,2,5] 

    for file_name in file_name_list:

        file = pd.ExcelFile(file_name)

        for sheetName in file.sheet_names[1:]:
            #usecolsは使用したいカラムのインデックス。各エクセルファイルの取り出した年度数に応じて変わりうる。
            df = file.parse(sheetName, header=None, index_col=2, skiprows=list(range(0,2)), usecols=use_cols_list)
            processed_df = pd.DataFrame()
            index_list = np.where([~df.reset_index().iloc[:,1].duplicated()])[1]
            for i, index in tqdm(enumerate(index_list)):
                if i+1 == len(index_list):
                    ticker_df = df.iloc[index:,:]
                else:
                    ticker_df = df.iloc[index:index_list[i+1],:]
                if len(ticker_df)!=num_cols:
                    continue
                ticker_df = ticker_df.T
                ticker_df["ticker_name"] = [ticker_df.iloc[0,0]]*len(ticker_df)
                ticker_df["ticker_code"] = [ticker_df.iloc[1,0][1:]]*len(ticker_df)
                ticker_df = ticker_df.iloc[2:,:]
                processed_df = pd.concat([processed_df, ticker_df])

            processed_df = processed_df.replace("-", np.nan)
            df_output = pd.concat([df_output, processed_df])
    
    return df_output

def extract_data_function_for_masa_2(file_name_list, num_years, num_cols):
    
    df_output = pd.DataFrame()
    use_cols_list = [0,1,2] + list(range(5,5+num_years))

    for file_name in file_name_list:

        file = pd.ExcelFile(file_name)

        for sheetName in file.sheet_names[1:]:
            #usecolsは使用したいカラムのインデックス。各エクセルファイルの取り出した年度数に応じて変わりうる。
            df = file.parse(sheetName, header=None, index_col=2, skiprows=list(range(0,6)), usecols=use_cols_list)
            processed_df = pd.DataFrame()
            index_list = np.where([~df.reset_index().iloc[:,1].duplicated()])[1]
            for i, index in tqdm(enumerate(index_list)):
                if i+1 == len(index_list):
                    ticker_df = df.iloc[index:,:]
                else:
                    ticker_df = df.iloc[index:index_list[i+1],:]
                if len(ticker_df)!=num_cols:
                    continue
                ticker_df = ticker_df.T
                ticker_df["ticker_name"] = [ticker_df.iloc[0,0]]*len(ticker_df)
                ticker_df["ticker_code"] = [ticker_df.iloc[1,0][1:]]*len(ticker_df)
                ticker_df = ticker_df.iloc[2:,:]
                processed_df = pd.concat([processed_df, ticker_df])

            processed_df = processed_df.replace("-", np.nan)
            df_output = pd.concat([df_output, processed_df])
            df_output = df_output.dropna(subset=["決算期"])
    
    return df_output