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
import camelot
import math
import pyodbc
import time
import sqlalchemy
from sqlalchemy import create_engine
import urllib
from tkinter import *
from tkinter import ttk, messagebox




pd.set_option('mode.chained_assignment', None)



def lookin_folder(root_dir1,root_dir2, r_exfile=None):# will have to account for another root_dir
    '''Looks in a folder via a path and builds a list with files that have extension pdf'''
    ex_files =[]
    x_files =[]
    r_exfile=[]
    p_exfile=[]
    r = []
    if len(listdir(root_dir1)) >= 1:
        for file in listdir(root_dir1):
            if file.endswith('.pdf'):
                ex_files.append(file)
                #ex_files = [i for i in ex_files if not i.startswith('~$')] # ----------- removes ~$ issue from list
                r_exfile = [root_dir1 + i for i in ex_files]
    if len(listdir(root_dir2)) >= 1:
        for file in listdir(root_dir2):
            if file.endswith('.pdf'):
                x_files.append(file)
                p_exfile = [root_dir2 + i for i in x_files]
    files = r_exfile + p_exfile
    return files
  


def extract_pdf(filelist): # need more functions to take care of the many possibilities to return dataframes
    
    if len(filelist) > 1:
#         for file in filelist:
#             if ".pdf" in file: # the string here will be augmented for each site once I have more pdfs
        tables = camelot.read_pdf(filelist[0])
        df1 = tables[0].df
        df1 = df1.iloc[2:]# remove the two stacked headers
        df1.columns=['1','2','3','4','5','6','7','8','9','10','11','12','13']
        df1.reset_index()
        df1 = df1.replace('',np.nan)# turn the data into pandas dataframe 
        df1 = df1[df1['3'].notna()]
#             if "Dust" in file:
        tables2 = camelot.read_pdf(filelist[1])
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
        #for file in filelist:
           # if "Scrape" in file: # the string here will be augmented for each site once I have more pdfs
        tables = camelot.read_pdf(filelist[0])
        df = tables[0].df
        df = df.iloc[2:]# remove the two stacked headers
        df.columns=['1','2','3','4','5','6','7','8','9','10','11','12','13']
        df.reset_index()
        df = df.replace('',np.nan)# turn the data into pandas dataframe 
        df = df[df['3'].notna()]
        return df
            

    else:
        print('There are no PDF files')



#df

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
        
        df.columns = ['rowid',	'sample_ID',	'subj_age',	'subj_sex',	'sample_antibodies',	'samp_type',	'anticoagulant',	'collect_date',	'storage_temp',	'enroll_date',	'enrolled_by',	'comments',	'all_tests_excluded']
        first_row = pd.DataFrame([{'rowid':-1,'sample_ID':'XXXXXXXX','subj_age':'XXX',	'subj_sex':'XXX',	'sample_antibodies':'XXXXXXXXXXXXX',	'samp_type':'XXXXXX',	'anticoagulant':'XXXXXXXXXXX',	'collect_date':'1/1/2001',	'storage_temp':'XXXX',	'enroll_date':'1/1/2001',	'enrolled_by':'xxxxx',	'comments':'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',	'all_tests_excluded':'XXX'}])	
    
        df = pd.concat([first_row, df])
        df = df.reset_index(drop=True)
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

def send_to_sql(df,table_name,engine,text):
    #try:
    
    add_date = dt.datetime.now().strftime("%Y%m%d_%H:%M:%S")
    df['dateinsert'] = pd.to_datetime('today')
    df.to_sql(table_name,engine,if_exists='replace',index=False,dtype={'rowid':sqlalchemy.types.INTEGER(),
                                                                        'sample_ID':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'subj_age':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'subj_sex':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'sample_antibodies':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'samp_type':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'anticoagulant':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'collect_date':sqlalchemy.types.DATE(),
                                                                        'storage_temp':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'enroll_date':sqlalchemy.types.DATE(),
                                                                        'enrolled_by':sqlalchemy.types.NVARCHAR(length=50),
                                                                        'comments':sqlalchemy.types.NVARCHAR(length=255),
                                                                        'all_tests_excluded':sqlalchemy.types.NVARCHAR(length=50),
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
    add_date = dt.datetime.now().strftime("%Y%m%d")
    #if file in listdir(root_dir1):
    if len(listdir(root_dir1)) >= 1:
        for file in listdir(root_dir1):
            if file.endswith('.pdf'):
                pdf_bcw_files.append(file)
                root_files1 = [root_dir1 + i for i in pdf_bcw_files]
    if len(listdir(root_dir2)) >= 1:
        for file in listdir(root_dir2):
            if file.endswith('.pdf'):
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
                if file.endswith('.pdf'):
                    if not file.startswith("arc"):
                        dst = dest_folder + 'arc_'+   file[:-4] +'_' +  add_date +'.pdf'
                        src =  dest_folder + file
        
                        os.rename(src, dst)
        else: 
            print('No files to be moved to Archive.')
        return files
    except:
        print('Archive Failed')

  

def main():
######################## below are for production####################################################
    text=r"G:/USRED_CLINICAL DATA/CLINTRIALS_IN_PROGRESS/IHD/IH-500 Antibody Identification/10 Data Management/DM Only/abid_success.txt"
    root_dir1=r"G:/USRED_CLINICAL DATA/CLINTRIALS_IN_PROGRESS/IHD/IH-500 Antibody Identification/08 Monitoring/Enrollment Monitoring/BLD PDFs/"
    root_dir2=r"G:\USRED_CLINICAL DATA/CLINTRIALS_IN_PROGRESS/IHD/IH-500 Antibody Identification/08 Monitoring/Enrollment Monitoring/BCW PDFs/"
    root_dir3=r"G:/USRED_CLINICAL DATA/CLINTRIALS_IN_PROGRESS/IHD/IH-500 Antibody Identification/10 Data Management/DM Only/"
    new_xlsx=r"G:/USRED_CLINICAL DATA/CLINTRIALS_IN_PROGRESS/IHD/IH-500 Antibody Identification/10 Data Management/DM Only/IHAB_ELCombine.xlsx"
    dest_folder=r"G:/USRED_STORAGE/Clinicals/Data Management/IHD IH-500 ABID/"
#######################################################################################################
######################## below are for testing locally################################################
#     text=r"C:/Users/u106421/Desktop/abid_success.txt"
#     root_dir1=r"C:/Users/u106421/Desktop/ABID_pdf_home/"
#     root_dir2=r"C:/Users/u106421/Desktop/ABID_pdf_home2/" 
#     root_dir3=r"C:/Users/u106421/Desktop/ABID_excel/"
#     new_xlsx=r"C:/Users/u106421/Desktop/ABID_excel/IHAB_ELCombine.xlsx"
#     dest_folder=r"C:/Users/u106421/Desktop/ABID_archive/"
#######################################################################################################
    table_name ="tbl_stg1_EL"

    engine = sqlalchemy.create_engine('mssql://USREDAP110/DK_Test_ClinTrial_IHD_ABID?driver=SQL+Server+Native+Client+11.0?charset=utf8', encoding = 'utf-8')
    
   
    filelist = lookin_folder(root_dir1,root_dir2)
    df= extract_pdf(filelist)
    send_to_excel(df, new_xlsx, text)
    send_to_sql(df,table_name,engine,text)
    move_files(root_dir1, root_dir2, root_dir3, dest_folder) # check to see if files need to be archived
    messagebox.showinfo('Success!','PDF successfully uploaded to SQL!')
    
#     def run():
#         if __name__ == "__main__":
window=Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
#window.withdraw()
window.title("ABID Scrape PDF")
window.geometry('550x200')

btn = Button(window, text="Run Script", bg="black", fg="white",command=main)
btn.grid(column=0, row=0)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()
#window.deiconify()
#window.destroy()

        #main()
    # execute only if run as a script
