from __future__ import print_function
from openpyxl import load_workbook
from openpyxl import workbook
from datetime import datetime
import os
import sys
import shutil

#######################################################################
#
# DCF CSV extraction file for Ruby Project  
# Author: David Kleppang
# Revision: B
# Date: 06/17/2019
#
# Application will extract information from multiple CSV files for Ruby 
# project and copy into one combined file suitable for importing into 
# SQL server through an import procedure
#
# Rev A: Initial
# Rev B: Update files to include Session Name feature 
#
#######################################################################

def input_config_data(config):
    '''Function to read in CONFIG.txt file and develop file configuration data from file'''
    with open(config, 'r') as f:
        lines = f.read().splitlines() 
        for line in lines:
            exec(line, globals()) #execute python strings in config file as python commands
        return [ICT] 

def extract_rawdata(rawdata_filepath):
    '''Function to add each Raw data source name and filepath to a list for further processing'''
    rawdata_filelist = [] #create empty list
    for filename in os.listdir(rawdata_filepath): #iterate thru each file in raw data file folder
        rawdata_filelist.append(rawdata_filepath + filename) #append to list of raw data files c/w full path information
    return rawdata_filelist

def read_input_file(rawdatafile_list):
    ''' Function to read manual csv files.  The function works by inputting a read-only list of all files to compare in sequential
        form'''
    file_list = []
    for rawfile in rawdatafile_list:
        if '(' in rawfile: #in case there is any duplicate files which usually have a '(n)' in the file name
            continue
        rawfile_hash =  rawfile[-36:-4] #extract file hash from csv files
        if rawfile[-3:] == 'csv':
            with open(rawfile, 'r') as f:
                lines = f.read().splitlines()
                #lines = lines[:-1]
                for line in lines:
                    try:
                        if line[0] == '1' or line[0] == '2':
                            line = (line + ',' + rawfile_hash).split(',')
                            file_list.append(line)
                    except:
                        print('Error in csv Read')
    return file_list

def find_insertion_point(wsdest, BINSEARCH_UB, SINK_ROW_INIT):
    ''' Function using binary search to determine insertion point for destination workbook'''
    low = SINK_ROW_INIT
    high = BINSEARCH_UB 
    i=0
    while low <= high:
        mid = (low + high) // 2
        #insertion_point is final mid in this algorithm
        i+=1
        if str(wsdest['A' + str(mid)].value) == "None" and str(wsdest['A' + str(mid-1)].value) != "None":
            return mid
        elif str(wsdest['A' + str(mid)].value) == "None":
            high = mid - 1
        else:
            low = mid + 1
    return None

def add_manual_results(oRPS_DICT): #This is for valid data results
    ''' Function to iterate through each csv file and 
    pull data from relevant fields to insert into destfile'''
    manual_feature_dict = {}
    dest_feature_dict = {}
    for result in orig_file:
        for index, manual_feature in enumerate(MAN_FORM_STRUCT):
            manual_feature_dict[manual_feature] = result[index]
        for dest_feature in DEST_DICT:
            if dest_feature in manual_feature_dict:
                dest_feature_value = DEST_DICT.get(dest_feature, "")
                manual_feature_value = manual_feature_dict.get(dest_feature, "")
                dest_feature_dict[dest_feature_value] =  manual_feature_value
        for column in DEST_DICT_REVERSE:
            #print(column)
            if column in dest_feature_dict:
                if column == DEST_DICT.get("IsExcluded", "") and dest_feature_dict.get(column, "") == 'true':
                    wsdest[column + str(insertion_point)] = 1 
                elif column == DEST_DICT.get("IsExcluded", "") and dest_feature_dict.get(column, "") == 'false':
                    wsdest[column + str(insertion_point)] = 0 
                elif column == DEST_DICT.get("DataEntryPersonNumber", "") and dest_feature_dict.get(column, "") == '1':
                    wsdest[column + str(insertion_point)] = 1 
                elif column == DEST_DICT.get("DataEntryPersonNumber", "") and dest_feature_dict.get(column, "") == '2':
                    wsdest[column + str(insertion_point)] = 2 
                elif column == DEST_DICT.get("RowID", ""):
                    wsdest[column + str(insertion_point)] = int(dest_feature_dict.get(column, "")) 
                elif column == DEST_DICT.get("Well_Positivity", ""):
                    wsdest[DEST_DICT.get("Well_Positivity", "") + str(insertion_point)] = manual_feature_dict.get("Well_Positivity", "") 
                    wsdest[DEST_DICT.get("Well_Result", "") + str(insertion_point)] = MANUAL_INTERPS_DICT.get(manual_feature_dict.get("Well_Positivity", ""), "") 
                else:
                    wsdest[column + str(insertion_point)] = dest_feature_dict.get(column, "")
        #wsdest[DEST_DICT.get("RowID", "") + str(insertion_point)] = insertion_point - SINK_ROW_INIT + 1 
        wsdest[DEST_DICT.get("TrialKey", "") + str(insertion_point)] = TRIALKEY 
        wsdest[DEST_DICT.get("DateLoaded", "") + str(insertion_point)] = datetime.now() 
        insertion_point += 1
    return insertion_point

def archive_buffer(buffer_file, dm_arc, type):
    '''Function to archive buffer file in dm_arc location'''
    if type == 'move':
        shutil.move(buffer_file, dm_arc + 'Arc_' + str(format(datetime.now().strftime('%Y%m%d %H%M%S ')))+ '_' + buffer_file.rsplit("/",1)[-1])
    else:
        shutil.copy2(buffer_file, dm_arc + 'Arc_' + str(format(datetime.now().strftime('%Y%m%d %H%M%S ')))+ '_' + buffer_file.rsplit("/",1)[-1])
    return

def main():
    '''Main function'''

    ###################################################   FILE PATHS
    ##Test Files
    # No test files needed.
    ##Production Files below
    rawdatapathlist_manual = 'Cst/' # production Filelocation list
    configfile = '' # production config file
    destfile = 'x' # production file
    dm_arc = '/' # archive location
    ####################################################   END OF FILE PATHS

    ###################################################   GET CONFIGURATION DATA
    [TR_DICT] = input_config_data(configfile) #obtain configuration params
    ###################################################   END OF GET CONFIGURATION DATA

    #### GET SINK (DESTINATION COMBINED REPRO RESULTS) WORKBOOK AS FILE OBJECT 
    wb = load_workbook(filename = destfile)
    wsdest = wb['Data']

    #### GET SOURCE INFO FROM FILE LOCATIONS LIST AND LOAD DATA INTO OBJECT LIST
    manual_files = extract_rawdata(rawdatapathlist_manual)

    #### OBTAIN INSERTION POINT INTO SINK 
    insertion_point = find_insertion_point(wsdest, BINSEARCH_UB, SINK_ROW_INIT)
    if insertion_point == None:
        print('Binary search upper bound exceeded.  Increase upper bound parameter in config file')
        sys.exit()

    #### PROCESS MANUAL LIST 
    orig_file_args = (manual_files)
    manual_orig_file = read_input_file(orig_file_args)

    print('Processing Manual Form Results...')
    manual_result_args = (manual_orig_file, wsdest, destfile, insertion_point, DEST_DICT, DEST_DICT_REVERSE, MAN_FORM_STRUCT, SINK_ROW_INIT, TRIALKEY, EQUIPSN_SITE_DICT_REVERSE, MANUAL_INTERPS_DICT)
    add_manual_results(*manual_result_args)
    print('Saving Manual Form Results...')

    wb.save(filename = destfile)

    #### ARCHIVE BUFFER FILE _Manual
    for buffer_manual_file in manual_files:
        bufferarchive_manual_args = (buffer_manual_file, dm_arc, 'move')
        archive_buffer(*bufferarchive_manual_args)

    #### ARCHIVE COMBINED EXPORT FILE
    bufferarchive_auto_args = (destfile, dm_arc, 'copy')
    archive_buffer(*bufferarchive_auto_args)

if __name__ == '__main__':
    main()