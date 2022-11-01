#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

pd.set_option('mode.chained_assignment', None)


# In[ ]:





# In[2]:


def lookin_folder(root_dir1,root_dir2, r_exfile=None):# will have to account for another root_dir
    '''Looks in a folder via a path and builds a list with files that have extension pdf'''
    ex_files =[]
    x_files =[]
    r_exfile=[]
    p_exfile=[]
    r = []
   
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
  
        #exit()
    



#filelist

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
    elif len(filelist) == 1:
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
    else:
        print('There are no PDF files')



#df

def send_to_excel(df, new_xlsx, text):
    try:
        with open(text, "a+") as file_object:
    # Move read cursor to the start of file.
            file_object.seek(0)
    # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
    # Append text at the end of file
            file_object.write("Scrape Completed and Excel File Generated")
        
        df.columns = ['rowid',	'sample_ID',	'subj_age',	'subj_sex',	'sample_antibodies',	'samp_type',	'anticoagulant',	'collect_date',	'storage_temp',	'enroll_date',	'enrolled_by',	'comments',	'all_tests_excluded']
        first_row = pd.DataFrame([{'rowid':-1,'sample_ID':'XXXXXXXX','subj_age':'XXX',	'subj_sex':'XXX',	'sample_antibodies':'XXXXXXXXXXXXX',	'samp_type':'XXXXXX',	'anticoagulant':'XXXXXXXXXXX',	'collect_date':'1/1/2001',	'storage_temp':'XXXX',	'enroll_date':'1/1/2001',	'enrolled_by':'xxxxx',	'comments':'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',	'all_tests_excluded':'XXX'}])	
    
        df = pd.concat([first_row, df])
        df = df.reset_index(drop=True)
        df.to_excel(new_xlsx, index=False)
        print(df)
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
            file_object.write("Scrape Failed and No Excel File Created")


# In[5]:


def send_to_sql(df,table_name,engine,text):
    #try:
    df.to_sql(table_name,engine,if_exists='append',index=False)
    time.sleep(30)#pauseing for 30 seconds to ensure import has finished so archive can happen without error
    with open(text, "a+") as file_object:
    # Move read cursor to the start of file.
        file_object.seek(0)
    # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
    # Append text at the end of file
        file_object.write("Data Successfully Appended to SQL Table")
   # except:
       # print("Check Database Connection")


# In[5]:


# move excel file before writing new excel file and move pdf's to new folder
# def move_files(root_dir1, root_dir2,root_dir3, dest_folder):
#     '''root_dir1 is the directory of bcw and root_dir1 directory bld, dest_folder is archive for both pdf and excel files'''
#     pdf_bcw_files =[]
#     pdf_bld_files=[]
#     excel_file=[]
#     root_files1=[]
#     root_files2=[]
#     root_files3=[]
#     add_date = dt.datetime.now().strftime("%Y%m%d")
#     #if file in listdir(root_dir1):
#     if len(listdir(root_dir1)) >= 1:
#         for file in listdir(root_dir1):
#             if 'IHAB'in file and file.endswith('.pdf'):
#                 pdf_bcw_files.append(file)
#                 root_files1 = [root_dir1 + i for i in pdf_bcw_files]
#     if len(listdir(root_dir2)) >= 1:
#         for file in listdir(root_dir2):
#             if 'IHAB'in file and file.endswith('.pdf'):
#                 pdf_bld_files.append(file)
#                 root_files2 = [root_dir2 + i for i in pdf_bld_files]
#     if len(listdir(root_dir3)) >= 1:
#         for file in listdir(root_dir3):
#             if file.endswith('.xlsx'):
#                 excel_file.append(file)
#                 root_files3 = [root_dir3 + i for i in excel_file]
                
#     files = root_files1 + root_files2 + root_files3
#    # print(files)
#     try:
#         if len(files) > 0:
    
#             for file in files:
#                 shutil.move(file, dest_folder)
    
#             for file in listdir(dest_folder):
#                 if file.endswith('.xlsx'):# if file ends with .pdf or xlsx, then remove the .xlsx and .pdf from name then create new name append the xlsx and pdf back
#                     if not file.startswith("arc"):
#                         dst = dest_folder + 'arc_'+   file[:-5] +'_' +  add_date +'.xlsx'
#                         src =  dest_folder + file
        
#                         os.rename(src, dst)
#                 if file.endswith('.pdf'):
#                     if not file.startswith("arc"):
#                         dst = dest_folder + 'arc_'+   file[:-4] +'_' +  add_date +'.pdf'
#                         src =  dest_folder + file
        
#                         os.rename(src, dst)
#         else: 
#             print('No files to be moved to Archive.')
#         return files
#     except:
#         print('Archive Failed')

  


# In[ ]:





# In[8]:


def input_config_data(config):
    '''Read in configuration file file and develop file configuration data from file.'''
    with open(config, 'r') as f: #open file (readonly) that is identified in config parameter
        lines = f.read().splitlines() 
        for line in lines:
            exec(line) #execute python strings in config file as python commands
        return [Trialkey, Driver, Server, Database, Trust_conn] #return all configuration variables to main()

def create_sqlserver_connection(driver, server, database, trust_conn):
    '''Create SQL server connection.'''
    conn = pyodbc.connect('driver={%s};server=%s;database=%s;trusted_connection=%s' % (driver, server, database, trust_conn))
    return conn

def CallStoredProc(connection, procName, *proc):
    '''Call SQL start_job stored procedure to start specified job (proc[0]).'''
    sql = """SET NOCOUNT ON;
         DECLARE @ret int
         EXEC @ret = %s %s
         SELECT @ret""" % (procName, ','.join(['?'] ))
    ret = int(connection.execute(sql, proc).fetchone()[0])
    if ret == 0:
        print(proc[0] + ' Job started OK')
    else:
        print(proc[0] + ' Job Error')
    return

def CheckStoredProc(connection, helpProc, proc, counter):
    '''Check every 10 seconds to determine if job is finished.'''
    connect = "{call [dbo].[" + helpProc + "]}"
    if counter == 0:
        connection.execute(connect,) # run first time when entering this function only!!!
    time.sleep(10) # to give program time to start executing
    connection.execute(connect,) # run first time when entering this function only!!!
    for row in connection:
        if row[2] in proc: # row[2] is name of job which should match the args that you set e.g. NA5C import
            exec_status = row[25] #row[25] is execution status (1 for executing and 4 for idle - implies finished)
            run_success = row[21] #row[21] is last_run_outcome: 0 for fail, 1 for success
            if exec_status == 4 and run_success == 1:
                print(proc + ' Job finished OK!')
                return
            elif exec_status == 4 and run_success == 0:
                print(proc + ' Job failed! Please verify all files are closed!')
                return
            else:
                print(proc + ' Job executing...')
                CheckStoredProc(connection, helpProc, proc, 1)
    return

def close_sqlserver_connection(conn):
    '''Close and delete SQL server connection.'''
    conn.close()
    del conn
    return 
          
            


# In[7]:


def main():
    text=r"C:/Users/u106421/Desktop/abid_success.txt"
    root_dir1=r"C:/Users/u106421/Desktop/ABID_pdf_home/"
    root_dir2=r"C:/Users/u106421/Desktop/ABID_pdf_home2/"
    root_dir3=r"C:/Users/u106421/Desktop/ABID_excel/"
    new_xlsx=r"C:/Users/u106421/Desktop/ABID_excel/IHAB_ELCombine.xlsx"
    dest_folder=r"C:/Users/u106421/Desktop/ABID_archive/"
    table_name ="tbl_stg1_EL"
#     params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
#                                  "SERVER=USREDAP110;"
#                                  "DATABASE=DK_Test_ClinTrial_IHD_ABID;"
#                                  "Trusted_Connection=yes")
#     engine = sqlalchemy.create_engine('mysql+pyodbc:///?odbc_connect{}'.format(params))
    engine = sqlalchemy.create_engine('mssql://USREDAP110/DK_Test_ClinTrial_IHD_ABID?driver=SQL+Server+Native+Client+11.0?charset=utf8', encoding = 'utf-8')
    
    #lister = move_files(root_dir1, root_dir2, root_dir3, dest_folder) # check to see if files need to be archived
    filelist = lookin_folder(root_dir1,root_dir2)
    df= extract_pdf(filelist)
    send_to_excel(df, new_xlsx, text)
    send_to_sql(df,table_name,engine,text)
   
    
if __name__ == "__main__":
    # execute only if run as a script
    main()


# In[ ]:




