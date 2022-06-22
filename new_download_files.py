# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:54:06 2022

@author: Mikkel Jensen
"""
import numpy as np
import pandas as pd
#import PyPDF2
#from pathlib import Path
#import shutil, os
import os.path
import urllib
import glob


def download_file(download_url, filename):
    try:
        print(filename)
        response = urllib.request.urlopen(download_url, timeout=1.0)  
#        response.
        file = open(str(filename) + ".pdf", 'wb')
        file.write(response.read())
        file.close()
    except Exception as e:
        print('Error')
        print(str(e))
 #       print(e.read())
#    file = open(filename + ".pdf", 'wb')
#    file.write(response.read())
#    file.close()

### specify path to file containing the URLs
list_pth = 'C:/Projekter/2022-06-07_PDF_Downloader_Task/01 Scripts input/GRI_2017_2020_SAHO.xlsx'

###specify Output folder (in this case it moves one folder up and saves in the script output folder)
pth = 'C:/Projekter/2022-06-07_PDF_Downloader_Task/03 Scripts output/'

###Specify path for existing downloads
dwn_pth = 'C:/Projekter/2022-06-07_PDF_Downloader_Task/03 Scripts output/dwn/'

### cheack for files already downloaded
#dwn_files = glob.glob(os.path.join(dwn_pth, "*.pdf")) 
#exist = [os.path.basename(f)[:-4] for f in dwn_files]

###specify the ID column name
#ID = "BRnum"


##########

### read in file
df0 = pd.read_excel(list_pth, sheet_name=0)
df=df0
print('Reading of excel file succesfull')

### filter out rows with no URL in both rows
non_empty1 = df.Pdf_URL.notnull() == True
non_empty2 = df.Report_Html_Address.notnull() == True
non_empty = np.logical_or(non_empty1,non_empty2)
df = df[non_empty]
df2 = df.copy()
print('Filtering succesfull')


#writer = pd.ExcelWriter(pth+'check_3.xlsx', engine='xlsxwriter', options={'strings_to_urls': False})


#Currently crashes at index=20, as it is not a PDF.

### filter out rows that have been downloaded
#df2 = df2[~df2.index.isin(exist)]

### loop through dataset, try to download file.
#j=0
for j in df2.index:
    savefile = str(pth + "dwn/" + str(j) + '.pdf')
    download_file(df2.at[j,'Pdf_URL'],str(dwn_pth + "/" + str(j)))
#    try:
#        urllib.request.urlretrieve(df2.at[j,'Pdf_URL'], savefile)
        #if os.path.isfile(savefile):
            #try:
                #pdfFileObj = open(savefile, 'rb')
               # creating a pdf reader object
                #pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                #with open(savefile, 'rb') as pdfFileObj:
                    #pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                    #if pdfReader.numPages > 0:
                        #df2.at[j, 'pdf_downloaded'] = "yes"
                    #else:
                        #df2.at[j, 'pdf_downloaded'] = "file_error"
               
            #except Exception as e:
               # df2.at[j, 'pdf_downloaded'] = str(e)
                #print(str(str(j)+" " + str(e)))
        #else:
            #df2.at[j, 'pdf_downloaded'] = "404"
            #print("not a file")
            
#    except (urllib.error.HTTPError, urllib.error.URLError, ConnectionResetError, Exception ) as e:
#        df2.at[j,"error"] = str(e)


#df2.to_excel(writer, sheet_name="dwn")
#writer.save()
#writer.close()
