import os

import pandas as pd
import pytube
import audio as aud

from main_script import SPEICIAL_CHAR,SHARPS,EXCEL_FILE_PATH,COL_HEAD
from main_script import MP3_SAVE_DIR,MP4_SAVE_DIR
from main_script import TEXT_FILE_PATH

TITLE_LIST_FOR_PRINT=list()

def excel_to_titleList():
    df=pd.read_excel(EXCEL_FILE_PATH)
    result=df[COL_HEAD].tolist()
    print_msg("excel to list completed!",True)
    return result

def titleList_to_reasultsList(titleList):
    reasultsList=list()
    for i in range(len(titleList)):
        reasultsList.append(input_to_pytube(titleList[i]))
    print_msg("title list to results list completed!",True)
    return reasultsList

def fix_title(title):
    for i in range(len(SPEICIAL_CHAR)):
        title=title.replace(SPEICIAL_CHAR[i],"")
    title=title.strip()
    title=title.replace("  "," ")
    title=title.replace("   "," ")
    title=title.replace("    "," ")
    title=title.replace("     "," ")
    title=title.title()
    return title

def download_resultList(resultsList, mp4_format=False):
    i=0
    for tubeObj in resultsList:
        i+=1
        print_msg("start downloading : "+str(i)+"/"+str(len(resultsList)),True)
        filename=fix_title(tubeObj.title)
        TITLE_LIST_FOR_PRINT.append(filename)
        print("\ntitle is: "+filename)
        if mp4_format:
            tubeObj.streams.get_highest_resolution().download(output_path=MP4_SAVE_DIR,filename=filename+".mp4")
            print_msg("finish downloading number "+str(i)+"/"+str(len(resultsList)),True,True)
            continue
        tubeObj.streams.get_audio_only().download(output_path=MP4_SAVE_DIR,filename=filename+".mp4")
        print_msg("finish downloading number "+str(i)+"/"+str(len(resultsList)),True,True)
        mp3Path=MP3_SAVE_DIR+"/"+filename+".mp3"
        mp4Path=MP4_SAVE_DIR+"/"+filename+".mp4"
        aud.mp4_to_mp3(mp4Path,mp3Path)
        deleteFile(mp4Path)
    return TITLE_LIST_FOR_PRINT

def deleteFile(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file {path} does not exist: ".format(path))

def print_msg(msg,sharps=False,strartLine=False,endLine=False):
    if(sharps):
        if (strartLine):
            print("\n"+SHARPS+msg+"\n"+SHARPS)
        else:
            print(SHARPS+msg+"\n"+SHARPS)
    else:
        if (strartLine and endLine):
            print("\n"+msg+"\n")
        elif(strartLine):
            print("\n"+msg)
        elif(endLine):
            print(msg+"\n")
        else:
            print(msg)
            
def input_to_pytube(link_or_title):
    if(link_or_title[0:5] == "https" or link_or_title[0:5] == "youtu"):
        return pytube.YouTube(link_or_title)
    else:
        return pytube.Search(link_or_title).results[0]

    
def fix_file_text_from_youtube(titleList):
    if titleList[0]!='\n':
        return titleList
    text_file =open(TEXT_FILE_PATH[:-4]+'_draft.txt','w')
    ret_list=[]
    for i in range(1,len(titleList),5):
        ret_list.append(titleList[i])
    print(ret_list)
    ret_list_str=aud.str_list(ret_list,False)
    print(ret_list_str)
    text_file.write(ret_list_str)
    text_file.close
    return ret_list
