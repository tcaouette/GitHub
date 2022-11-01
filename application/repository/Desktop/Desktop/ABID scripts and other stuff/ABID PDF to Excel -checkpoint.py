#!/usr/bin/env python
# coding: utf-8

# In[23]:


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
pd.set_option('mode.chained_assignment', None)

root_dir=r"C:/Users/u106421/Desktop/ABID_pdf_home/"

def lookin_folder(root_dir, r_exfile=None):# will have to account for another root_dir
    '''Looks in a folder via a path and builds a list with files that have extension pdf'''
    ex_files =[]
    for file in listdir(root_dir):
        if 'IHAB'in file and file.endswith('.pdf'):
            ex_files.append(file)
            #ex_files = [i for i in ex_files if not i.startswith('~$')] # ----------- removes ~$ issue from list
            r_exfile = [root_dir + i for i in ex_files]
    return r_exfile

filelist = lookin_folder(root_dir)


def extract_pdf(filelist):
    for file in filelist:
        if "Scrape" in file: # the string here will be augmented for each site once I have more pdfs
            tables = camelot.read_pdf(file)
            df1 = tables[0].df # turn the data into pandas dataframe 

    return df1

# function to merge dataframe here
#def merge_df(df1,df2):

def clean_dfs(df1):# need to account for two dataframes
    df1 = df1.iloc[2:]# remove the two stacked headers
    df1.reset_index()
    df1 = df1.replace('',np.NaN)
    return df1


# In[24]:


df12= extract_pdf(filelist)

new_df = clean_dfs(df12)


# In[25]:


new_df
#list_df =new_df.values.tolist()


# In[ ]:





# In[13]:


df = pd.DataFrame(list_df,columns=['stuff0','stuff1','stuff2','#','subj_age','subj_sex','sample_antibodies','samp_type','anticoagulant','collect_date','storage_temp','enroll_date','comments'])


# In[14]:


df


# In[150]:


def send_to_excel(df):
    df.to_excel(r"C:/Users/u106421/Desktop/ABID_pdf_home/abid.xlsx", index=False)
    return print("Excel Doc Created")# need to add a header to the dataframe before it gets exported 

send_to_excel(new_df)


# In[ ]:


# create function to search for pdf's and if two merge them together


# In[ ]:


# archive the pdf's after ingestion


# In[ ]:


# trigger stored procedure


# In[ ]:


root_dir = r"G:/USRED_CLINICAL DATA/CLINTRIALS_IN_PROGRESS/IHD/Bio-Rad Canada Reproducibility Study/DM only/"
excel_Peter = r"G:/USRED_CLINICAL DATA/CLINTRIALS_IN_PROGRESS/IHD/Bio-Rad Canada Reproducibility Study/DM only/Repro -  Peterborough 2019.xlsx"
excel_GenHosp = r"G:/USRED_CLINICAL DATA/CLINTRIALS_IN_PROGRESS/IHD/Bio-Rad Canada Reproducibility Study/DM only/Repro -  Site Alexandra Marine & Gen Hosp 2019.xlsx"
excel_BIOrad = r"G:/USRED_CLINICAL DATA/CLINTRIALS_IN_PROGRESS/IHD/Bio-Rad Canada Reproducibility Study/DM only/Repro -  Site Bio-Rad 2019.xlsx"
output_manual = r"G:/USRED_CLINICAL DATA/CLINTRIALS_IN_PROGRESS/IHD/Bio-Rad Canada Reproducibility Study/DM only/Output files from python/Canada_Test_v2.xlsx"
output_manual_pool =  r"G:/USRED_CLINICAL DATA/CLINTRIALS_IN_PROGRESS/IHD/Bio-Rad Canada Reproducibility Study/DM only/Output files from python/Canada_Test_plus_pool_v2.xlsx"



# def archive_excel(dest_dir,root_dir,auto_file,manual_file):#-------archives autofile and manualfile-----instead of deleting the files for history---------
#     exfiles=[]
#     new_files=[]
#     add_date = dt.datetime.now().strftime("%Y%m%d %H%M%S%f")
#     for f in listdir(root_dir):
#         if auto_file in  f:
#             exfiles.append(f)
#             exfiles = [i for i in exfiles if not i.startswith('~$')] # ----------- removes ~$ issue from list
#             new_files = [root_dir + i for i in exfiles]
#         if manual_file in f:
#             exfiles.append(f)
#             exfiles = [i for i in exfiles if not i.startswith('~$')] # ----------- removes ~$ issue from list
#             new_files = [root_dir + i for i in exfiles]
            
#     if len(new_files) > 0:
    
#         for files in new_files:
#             shutil.move(files, dest_dir)
    
#         for file in listdir(dest_dir):
#             if not file.startswith("Archived"):
#                 dst = dest_dir + 'Archived_'+ add_date +'_' +  file 
#                 src =  dest_dir + file
        
#                 os.rename(src, dst)
#     else: 
#         print('No files to be moved to Archive.')
        
#archive_excel(root_dir)

def lookin_folder(root_dir, r_exfile=None):
    '''Looks in a folder via a path and builds a list with files that have extension xlsm'''
    ex_files =[]
    for file in listdir(root_dir):
        if 'Repro'in file and file.endswith('.xlsx'):
            ex_files.append(file)
            ex_files = [i for i in ex_files if not i.startswith('~$')] # ----------- removes ~$ issue from list
            r_exfile = [root_dir + i for i in ex_files]
    return r_exfile

