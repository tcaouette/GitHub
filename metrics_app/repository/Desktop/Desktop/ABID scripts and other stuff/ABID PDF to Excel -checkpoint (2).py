#!/usr/bin/env python
# coding: utf-8

# In[187]:


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
pd.set_option('mode.chained_assignment', None)

root_dir1=r"C:/Users/u106421/Desktop/ABID_pdf_home/"
root_dir2=r"C:/Users/u106421/Desktop/ABID_pdf_home2/"
root_dir3=r"C:/Users/u106421/Desktop/ABID_excel/"
new_xlsx=r"C:/Users/u106421/Desktop/ABID_excel/abid.xlsx"
dest_folder=r"C:/Users/u106421/Desktop/ABID_archive/"
def lookin_folder(root_dir1,root_dir2, r_exfile=None):# will have to account for another root_dir
    '''Looks in a folder via a path and builds a list with files that have extension pdf'''
    ex_files =[]
    x_files =[]
    r_exfile=[]
    p_exfile=[]
    for file in listdir(root_dir1):
        if 'IHAB'in file and file.endswith('.pdf'):
            ex_files.append(file)
            #ex_files = [i for i in ex_files if not i.startswith('~$')] # ----------- removes ~$ issue from list
            r_exfile = [root_dir1 + i for i in ex_files]
    for file in listdir(root_dir2):
        if 'IHAB'in file and file.endswith('.pdf'):
            x_files.append(file)
            p_exfile = [root_dir2 + i for i in x_files]
    files = r_exfile + p_exfile
    return files

filelist = lookin_folder(root_dir1,root_dir2)

filelist

def extract_pdf(filelist): # need more functions to take care of the many possibilities to return dataframes
    if len(filelist) > 1:
        for file in filelist:
            if "Scrape" in file: # the string here will be augmented for each site once I have more pdfs
                tables = camelot.read_pdf(file)
                df1 = tables[0].df
                df1 = df1.iloc[2:]# remove the two stacked headers
                df1.columns=['1','2','3','4','5','6','7','8','9','10','11','12','13']
                df1.reset_index()
                df1 = df1.replace('',np.nan)# turn the data into pandas dataframe 
                df1 = df1[df1['3'].notna()]
            if "Dust" in file:
                tables = camelot.read_pdf(file)
                df2 = tables[0].df
                df2 = df2.iloc[2:]# remove the two stacked headers
                df2.columns=['1','2','3','4','5','6','7','8','9','10','11','12','13']
                df2.reset_index()
                df2 = df2.replace('',np.nan)
                df2 = df2[df2['3'].notna()]
        df_row = pd.concat([df1, df2])
        return df_row
    else:
        #return print("less than 1")
        for file in filelist:
            if "Scrape" in file: # the string here will be augmented for each site once I have more pdfs
                tables = camelot.read_pdf(file)
                df1 = tables[0].df
                df1 = df1.iloc[2:]# remove the two stacked headers
                df1.columns=['1','2','3','4','5','6','7','8','9','10','11','12','13']
                df1.reset_index()
                df1 = df1.replace('',np.nan)# turn the data into pandas dataframe 
                df1 = df1[df1['3'].notna()]
                return df1
            
            if "Dust" in file:
                tables = camelot.read_pdf(file)
                df2 = tables[0].df
                df2 = df2.iloc[2:]# remove the two stacked headers
                df2.columns=['1','2','3','4','5','6','7','8','9','10','11','12','13']
                df2.reset_index()
                df2 = df2.replace('',np.nan)
                df2 = df2[df2['3'].notna()]
                return df2
   

df= extract_pdf(filelist)

df

def send_to_excel(df, new_xlsx):
    df.to_excel(root_dir3, index=False)
    return print("Excel Doc Created")# need to add a header to the dataframe before it gets exported 

send_to_excel(df,new_xlsx)


# In[194]:


# move excel file before writing new excel file and move pdf's to new folder
def move_files(root_dir1, root_dir2,root_dir3, dest_folder):
    '''root_dir1 is the directory of bcw and root_dir1 directory bld, dest_folder is archive for both pdf and excel files'''
    pdf_bcw_files =[]
    pdf_bld_files=[]
    excel_file=[]
    root_files1=[]
    root_files2=[]
    root_files3=[]
    add_date = dt.datetime.now().strftime("%Y%m%d %H%M%S%f")
    #if file in listdir(root_dir1):
    if len(listdir(root_dir1)) >= 1:
        for file in listdir(root_dir1):
            if 'IHAB'in file and file.endswith('.pdf'):
                pdf_bcw_files.append(file)
                root_files1 = [root_dir1 + i for i in pdf_bcw_files]
    if len(listdir(root_dir2)) >= 1:
        for file in listdir(root_dir2):
            if 'IHAB'in file and file.endswith('.pdf'):
                pdf_bld_files.append(file)
                root_files2 = [root_dir2 + i for i in pdf_bld_files]
    if len(listdir(root_dir3)) >= 1:
        for file in listdir(root_dir3):
            if file.endswith('.xlsx'):
                excel_file.append(file)
                root_files3 = [root_dir3 + i for i in excel_file]
                
    files = root_files1 + root_files2 + root_files3
    if len(files) > 0:
    
        for file in files:
            shutil.move(file, dest_folder)
    
        for file in listdir(dest_folder):
            if not file.startswith("Archived"):
                dst = dest_folder + 'Archived_'+ add_date +'_' +  file 
                src =  dest_folder + file
        
                os.rename(src, dst)
    else: 
        print('No files to be moved to Archive.')
    return files
lister = move_files(root_dir1, root_dir2, root_dir3, dest_folder)
            
            


# In[195]:


print(lister)


# In[ ]:


def archive_pdf(dest_dir,root_dir1,root_dir2,bcw_file,bld_file):
    exfiles=[]
    new_files=[]
    add_date = dt.datetime.now().strftime("%Y%m%d %H%M%S%f")
    for f in listdir(root_dir1):
        if auto_file in  f:
            exfiles.append(f)
            exfiles = [i for i in exfiles if not i.startswith('~$')] # ----------- removes ~$ issue from list
            new_files = [root_dir + i for i in exfiles]
        if manual_file in f:
            exfiles.append(f)
            exfiles = [i for i in exfiles if not i.startswith('~$')] # ----------- removes ~$ issue from list
            new_files = [root_dir + i for i in exfiles]
            
    if len(new_files) > 0:
    
        for files in new_files:
            shutil.move(files, dest_dir)
    
        for file in listdir(dest_dir):
            if not file.startswith("Archived"):
                dst = dest_dir + 'Archived_'+ add_date +'_' +  file 
                src =  dest_dir + file
        
                os.rename(src, dst)
    else: 
        print('No files to be moved to Archive.')


# In[ ]:





# In[151]:





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

