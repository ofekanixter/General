import os

import audio,pytube_auto as tube

MP4_SAVE_DIR="C:/Users/SmadarENB3/Desktop/songs/MP4"
MP3_SAVE_DIR="C:/Users/SmadarENB3/Desktop/songs"
EXCEL_FILE_PATH="C:/Users/SmadarENB3/Desktop/ofek/programing/python/titles.xlsx"
TEXT_FILE_PATH="C:/Users/SmadarENB3/Desktop/ofek/programing/python/titles.txt"
COL_HEAD='name'
SPEICIAL_CHAR=['@','#','$','*','"','&','|','//','/','(official video)','(Official Music Video)','(Official Video)','(OFFICIAL VIDEO)','(Video Oficial)','(video oficial)','(VIDEO OFICIAL)','(Official Video)']
TITLE_LIST_FOR_PRINT=list()
VALID_INPUT=['','concat','manual','excel','textFile','text']
SHARPS="################################\n"
HIGHLIGHTS_TAMPLATE=""
TITLE_LIST_FOR_PRINT=list()

def manual_mode(mp4_format):
    oneMore= True
    while(oneMore):
        link_or_title = input('Youtube Video URL or search title\n')
        tubeObj= tube.input_to_pytube(link_or_title)
        filename=tube.fix_title(tubeObj.title)
        TITLE_LIST_FOR_PRINT.append(filename)
        if mp4_format:
            tubeObj.streams.get_highest_resolution().download(output_path=MP4_SAVE_DIR,filename=filename+".mp4")
            print("\n"+SHARPS+"\n","finish downloading")
            oneMore = input('again? Y/N\n') =="Y"
            if oneMore:
                continue
            else:
                break
        tubeObj.streams.get_audio_only().download(output_path=MP4_SAVE_DIR,filename=filename+".mp4")
        print("\n"+SHARPS+"\n","downloading completed ","\n"+SHARPS+"\n")
        mp3Path=MP3_SAVE_DIR+"/"+filename+".mp3"
        mp4Path=MP4_SAVE_DIR+"/"+filename+".mp4"
        audio.mp4_to_mp3(mp4Path,mp3Path)
        tube.deleteFile(mp4Path)
        oneMore = input('again? Y/N\n') =="Y"

def excel_mode(mp4_format):
    titleList=tube.excel_to_titleList()
    resultsList=tube.titleList_to_reasultsList(titleList)
    tube.download_resultList(resultsList,mp4_format)

def text_mode(mp4_format):
    titleList= list()
    while(True):
        text=input('enter song titles or N(if you finished)\n')
        if(text == 'N'):
            break
        titleList.append(text.split('\n'))
    resultsList=tube.titleList_to_reasultsList(titleList)
    TITLE_LIST_FOR_PRINT = tube.download_resultList(resultsList,mp4_format)

def text_file_mode(mp4_format):
    titleList= list()
    path=input("enter file path (or just enter for the defualt) :\n")
    if(path==""):
        path=TEXT_FILE_PATH
    if(os.path.exists(path)):
        text_file =open(path,'r')
    else:
        print("this path is not exist :"+path)
    titleList=text_file.readlines()
    text_file.close
    titleList=tube.fix_file_text_from_youtube(titleList)
    resultsList=tube.titleList_to_reasultsList(titleList)
    TITLE_LIST_FOR_PRINT = tube.download_resultList(resultsList,mp4_format)

def check_input(c):
    if c==None:
        return False
    valid=c in VALID_INPUT
    if not valid:
        msg="the input: '{c}' is illegal please enter on of the valid inputs as \n{valid_list}".format(c=c,valid_list=VALID_INPUT)
        print(msg)
    return valid

def main():
    c=None
    while(not check_input(c)):
        c=input('enter mode : manual or excel or textFile or text :\n')
        if c=="":
            c='text'
    mp4_format=input('for video(mp4) enter MP4\n')=='MP4'
    match c:
        case "manual":
            manual_mode(mp4_format)
        case "excel":
            excel_mode(mp4_format)
        case "textFile":
            text_file_mode(mp4_format)
        case "text":
            text_mode(mp4_format)
    print("\nthe title that downloaded are :\n",audio.str_list(TITLE_LIST_FOR_PRINT))


    


if __name__ == "__main__":
    main()