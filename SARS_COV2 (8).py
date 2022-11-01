#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import re
import sys
import csv
import openpyxl
import decimal
import os
from os import listdir
from os.path import isfile, join
import datetime as dt
import shutil
import uuid
from openpyxl import load_workbook
import tabula
import PyPDF2 as pypdf2 
import camelot
import math
import pyodbc
import time
import sqlalchemy
from sqlalchemy import create_engine
import urllib
from tkinter import *
from tkinter import ttk, messagebox
from itertools import cycle

text=r"C:/Users/u106421/Desktop/sarscov2_success.txt"
root_dir1=r"C:/Users/u106421/Desktop/SARS_COV_2/Evolis/"
root_dir2=r"C:/Users/u106421/Desktop/SARS_COV_2/PR4100/" 
root_dir3=r"C:/Users/u106421/Desktop/SARSCOV2_excel/"
new_xlsx=r"C:/Users/u106421/Desktop/SARSCOV2_excel/SARSCOV2_ELCombine.xlsx"
dest_folder=r"C:/Users/u106421/Desktop/SARSCOV2_Archive/"


def lookin_folder(root_dir1,root_dir2, r_exfile=None):# will have to account for another root_dir
    '''Looks in a folder via a path and builds a list with files that have extension pdf'''
    ex_files =[]
    x_files =[]
    r_exfile=[]
    p_exfile=[]
    r = []
    if len(listdir(root_dir1)) >= 1:
        for file in listdir(root_dir1):
            if file.endswith('.txt'):
                ex_files.append(file)
                #ex_files = [i for i in ex_files if not i.startswith('~$')] # ----------- removes ~$ issue from list
                r_exfile = [root_dir1 + i for i in ex_files]
    if len(listdir(root_dir2)) >= 1:
        for file in listdir(root_dir2):
            if file.endswith('.txt'):
                x_files.append(file)
                p_exfile = [root_dir2 + i for i in x_files]
    files = r_exfile + p_exfile
    return files
txt_file_paths =lookin_folder(root_dir1,root_dir2, r_exfile=None)
print(txt_file_paths)
def evolis_add_meta(txt_file_paths):
    append_evolis = pd.DataFrame()
    for path in txt_file_paths:
        if 'Evolis' in path:
            evolis_data = pd.read_csv(path,skiprows=23, sep="|",na_filter = True)
            evolis_data = evolis_data[:-1] 
            rows_to_keep = [1,2,3,5]
            evolis_meta = pd.read_csv(path, skiprows = lambda x: x not in rows_to_keep,sep='|', header=None)
            transpose_eMeta = evolis_meta.T
            new_header = transpose_eMeta.iloc[0]            
            transpose_eMeta = transpose_eMeta[1:] 
            transpose_eMeta.columns = new_header
            eMeta_repeated = pd.concat([transpose_eMeta]*len(evolis_data), ignore_index=True)
            join_df = evolis_data.join(eMeta_repeated)
            append_evolis = append_evolis.append(join_df)
    return  append_evolis

def extract_pr4100(txt_file_paths):
    append_pr41 = pd.DataFrame()
    for path in txt_file_paths:
        if 'PR4100' in path:
            pr41_data = pd.read_csv(path, skiprows=2, header=None, sep='|')
            comments = pr41_data.loc[pr41_data[0] == 'C', :]
            pr41_data[2]=pr41_data[2].str.strip('^^^BRSARSt')
            pr41_data[6] = pr41_data[6].apply(lambda x: '{:.0f}'.format(x))
            pr41_data = pr41_data.loc[(pr41_data[0] != 'P') & (pr41_data[0] != 'C') & (pr41_data[0] != 'L'), :]
            pr41_data[[7,8]] = pr41_data[2].str.split("^",expand=True) 
            pr41_data.drop([1,2,4,5,7], axis=1, inplace=True) #add 6 back, and remove_P
            append_pr41 = append_pr41.append(pr41_data)
    return append_pr41

def extract_pr4100_comments(txt_file_paths):
    append_comments = pd.DataFrame()
    for path in txt_file_paths:
        if 'PR4100' in path:
            pr41_data = pd.read_csv(path, skiprows=1, header=None, sep='|',names=list(range(7)))
            comments = pr41_data.loc[(pr41_data[0] == 'C'),:]
            comments[2]=comments[2].str.strip('\^^^')
            split = comments[2].str.split("^",expand=True) 
            split.columns = ['{}'.format(x+7) for x in split.columns]
            comments = comments.join(split)
            append_comments = append_comments.append(comments)
            append_comments.columns =[0,1,2,3,4,5,6,7,8,9,10]
    return append_comments

com = extract_pr4100_comments(txt_file_paths)



def pr41_comments_drop(df):
    df.drop([0,1,4,5,6,7,9,10], axis=1, inplace=True)
    df = df[[8,2,3]]
    df['Comments'] = df[2] +" "+ df[3]
    df.drop([2,3], axis=1, inplace=True)
    df.columns =['Well', 'Comments']
    return df

pr41_comments = pr41_comments_drop(com)



def pr41_list_df(df):
    n = 6  #chunk row size
    df = [df[i:i+n] for i in range(0,df.shape[0],n)]
    return df



def pr41_move_add_row(df):
    for i in range(len(df)):
        df[i].iloc[0,1] = df[i].iloc[1,3]
        df[i]=list_df[i].append(pd.Series(), ignore_index=True)
    return df
    

def pr41_move_date(df):
    for i in range(len(df)):
        df[i].iloc[6,0]='R'
        df[i].iloc[6,1]=df[i].iloc[0,2]
    return df



def pr41_drop_cols(df):
    for i in range(len(df)):
        df[i].drop(6, axis=1, inplace=True) 
        df[i].drop(8, axis=1, inplace=True) 
    return df


def transpose_pr41(df):
    df_append=[]
    for i in range(len(df)):
        df_append.append(df[i].set_index(0).transpose())
    transposed_pr41 = pd.concat(df_append)
    transposed_pr41.columns=['Well','Sample ID','Layout','OD for Cutoff','S/CO','Cutoff Result','Date']
    return transposed_pr41


# In[207]:


pr41_data = extract_pr4100(txt_file_paths)
    
list_df = pr41_list_df(pr41_data)
    
new_df = pr41_move_add_row(list_df)
    
df_R = pr41_move_date(new_df)
    
cleaned_pr41 = pr41_drop_cols(df_R)
    
transposed_pr41 = transpose_pr41(cleaned_pr41)


# In[210]:


#transposed_pr41.join(pr41_comments)
pr41_final_data =transposed_pr41.merge(pr41_comments, on='Well', how='left')


# In[211]:


pr41_final_data


# In[9]:


def send_to_excel(df, new_xlsx, text):
    add_date = dt.datetime.now().strftime("%Y%m%d_%H:%M:%S")
    try:
        with open(text, "a+") as file_object:
    # Move read cursor to the start of file.
            file_object.seek(0)
    # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
    # Append text at the end of file
            yay = "Scrape Completed and Excel File Generated " + add_date
            file_object.write(yay)
        
        df.to_excel(new_xlsx, index=False)
        
        return print("Excel Doc Created")# need to add a header to the dataframe before it gets exported 
    except:
        with open(text, "a+") as file_object:
    # Move read cursor to the start of file.
            file_object.seek(0)
    # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
    # Append text at the end of file
            failed = "Scrape Failed and No Excel File Created " + add_date
            file_object.write(failed)


def evolis_send_to_sql(df,table_name,engine,text):# customize for evolis and pr4100
    #try:
    
    add_date = dt.datetime.now().strftime("%Y%m%d_%H:%M:%S")
    df['dateinsert'] = pd.to_datetime('today')
    df.to_sql(table_name,engine,if_exists='replace',index=False,dtype={'Patient ID':sqlalchemy.types.INTEGER(),
                                                                        'Assay':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'Well':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'OD for Cutoff':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'S/CO':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'Cutoff Result':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'Date':sqlalchemy.types.sqlalchemy.types.DATE(),
                                                                        'dateinsert':sqlalchemy.types.Date(),
                                                                      })
    time.sleep(30)#pauseing for 30 seconds to ensure import has finished so archive can happen without error
    with open(text, "a+") as file_object:
    # Move read cursor to the start of file.
        file_object.seek(0)
    # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
    # Append text at the end of file
        excellent = "Data Successfully Appended to SQL Table " + add_date
        file_object.write(excellent)
   # except:
       # print("Check Database Connection")
def pr41_send_to_sql(df,table_name,engine,text):# customize for evolis and pr4100
    #try:
    # change header values on the pr41data
    add_date = dt.datetime.now().strftime("%Y%m%d_%H:%M:%S")
    df['dateinsert'] = pd.to_datetime('today')
    df.to_sql(table_name,engine,if_exists='replace',index=False,dtype={'Well':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'Sample ID':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'Layout':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'Flag':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'OD':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'S/CO':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'Result':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'Instrument ID:':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'Time:':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'DATE:':sqlalchemy.types.DATE(),
                                                                        'Operator':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'dateinsert':sqlalchemy.types.Date(),
                                                                        
                                                                      })
    time.sleep(30)#pauseing for 30 seconds to ensure import has finished so archive can happen without error
    with open(text, "a+") as file_object:
    # Move read cursor to the start of file.
        file_object.seek(0)
    # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
    # Append text at the end of file
        excellent = "Data Successfully Appended to SQL Table " + add_date
        file_object.write(excellent)
   # except:
       # print("Check Database Connection")

# move excel file before writing new excel file and move pdf's to new folder
def move_files(root_dir1, root_dir2,root_dir3, dest_folder):
    '''root_dir1 is the directory of bcw and root_dir1 directory bld, dest_folder is archive for both pdf and excel files'''
    pdf_bcw_files =[]
    pdf_bld_files=[]
    excel_file=[]
    root_files1=[]
    root_files2=[]
    root_files3=[]
    add_date = dt.datetime.now().strftime('%Y%m%d_%H%M%S')
    #if file in listdir(root_dir1):
    if len(listdir(root_dir1)) >= 1:
        for file in listdir(root_dir1):
            if file.endswith('.txt'):
                pdf_bcw_files.append(file)
                root_files1 = [root_dir1 + i for i in pdf_bcw_files]
    if len(listdir(root_dir2)) >= 1:
        for file in listdir(root_dir2):
            if file.endswith('.txt'):
                pdf_bld_files.append(file)
                root_files2 = [root_dir2 + i for i in pdf_bld_files]
    if len(listdir(root_dir3)) >= 1:
        for file in listdir(root_dir3):
            if file.endswith('.xlsx'):
                excel_file.append(file)
                root_files3 = [root_dir3 + i for i in excel_file]
                
    files = root_files1 + root_files2 + root_files3
   # print(files)
    try:
        if len(files) > 0:
    
            for file in files:
                shutil.move(file, dest_folder)
    
            for file in listdir(dest_folder):
                if file.endswith('.xlsx'):# if file ends with .pdf or xlsx, then remove the .xlsx and .pdf from name then create new name append the xlsx and pdf back
                    if not file.startswith("arc"):
                        dst = dest_folder + 'arc_'+   file[:-5] +'_' +  add_date +'.xlsx'
                        src =  dest_folder + file
        
                        os.rename(src, dst)
                if file.endswith('.txt'):
                    if not file.startswith("arc"):
                        dst = dest_folder + 'arc_'+   file[:-4] +'_' +  add_date +'.txt'
                        src =  dest_folder + file
        
                        os.rename(src, dst)
        else: 
            print('No files to be moved to Archive.')
        return files
    except:
        print('Archive Failed')


def main():
######################## below are for production####################################################

    text=r"xt"
    root_dir1=r"//
    root_dir2=r"//"
    root_dir3=r""
    evolis_new_xlsx=r""
    pr4100_new_xlsx=r"
    dest_folder=r""
#######################################################################################################

    evolis_table_name ="stg0_UPLOAD_EVOLIS"
    pr41_table_name ="stg0_UPLOAD_PR41"

    engine = sqlalchemy.create_engine('mssql://charset=utf8', encoding = 'utf-8')
    
   
    #txt_file_paths = lookin_folder(root_dir1,root_dir2)
    ##evolis
    #evolis_df = evolis_add_meta(txt_file_paths)
    ##PR41
    #pr41_data = extract_pr4100(txt_file_paths)
    
    #list_df = pr41_list_df(pr41_data)
    
    #new_df = pr41_move_add_row(list_df)
    
    #df_R = pr41_move_date(new_df)
    
    #cleaned_pr41 = pr41_drop_cols(df_R)
    
    #transposed_pr41 = transpose_pr41(cleaned_pr41)
    
    #send_to_excel(transposed_pr41, new_xlsx, text)
    
    #pr41_send_to_sql(transposed_pr41,pr41_table_name,engine,text)
    ###end pr41
    #send_to_excel(evolis_df, new_xlsx, text)
   # evolis_send_to_sql(evolis_df,evolis_table_name,engine,text)
    move_files(root_dir1, root_dir2, root_dir3, dest_folder)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()


# In[3]:





# In[ ]:




