import os
import argparse

from  youtube_audio import general,audio,pytube_auto as tube

VALID_INPUT=['','FILE','TEXT','AUDIO']
HIGHLIGHTS_TAMPLATE=""
CONCAT_SONG_DIR="C:/Users/SmadarENB3/Desktop/songs/concat"
SONG_DIR="C:/Users/SmadarENB3/Desktop/songs"
MERGED_SAVE_DIR="C:/Users/SmadarENB3/Desktop/songs/concat/merged"
TEXT_FILE_PATH="C:/Users/SmadarENB3/Desktop/ofek/programing/python/titles.txt"

def file_mode(source,dest,mp4_format):
    if source.endswith('.txt'):
        return text_file_mode(source,dest,mp4_format)
    elif source.endswith('.xlsx'):
        return excel_file_mode(source,dest,mp4_format)
    print("invalid file:\n"+source)
    
def excel_file_mode(source,dest,mp4_format):
    titleList=tube.excel_to_titleList(source)
    resultsList=tube.titleList_to_reasultsList(titleList)
    return tube.download_resultList(resultsList,dest,mp4_format)

def text_file_mode(source,dest,mp4_format):
    if(source==""):
        source=TEXT_FILE_PATH
    if(os.path.exists(source)):
        text_file =open(source,'r')
    else:
        print("this path is not exist :"+source)
    titleList=text_file.readlines()
    text_file.close
    titleList=tube.fix_file_text_from_youtube(titleList,source)
    resultsList=tube.titleList_to_reasultsList(titleList)
    return tube.download_resultList(resultsList,dest,mp4_format)

def text_mode(text,dest,mp4_format):
    titleList= list()
    oneMore=True
    while(oneMore):
        text = input('enter song\n')
        titleList.append(text.split('\n'))
        oneMore=input('enter for one more or any key for finish\n')==''
    resultsList=tube.titleList_to_reasultsList(titleList)
    return tube.download_resultList(resultsList,dest,mp4_format)

def check_input(c):
    if c==None:
        return False
    valid=c in VALID_INPUT
    if not valid:
        msg="the input: '{c}' is illegal please enter on of the valid inputs as \n{valid_list}".format(c=c,valid_list=VALID_INPUT)
        print(msg)
    return valid


def concat_audio_mode(in_folder,out_folder,merged_name="merged"):
    pathes=[]
    title_list=list()
    filesnames = next(os.walk(in_folder), (None, None, []))[2]  # [] if no file
    if filesnames == []:
        print("no files in concat defualt dir")
        exit
    for name in filesnames:
        title_list.append(name)
        pathes.append(in_folder+"/"+name)
    print("title_list")
    print(title_list)
    print(merged_name)
    return audio.concat_audio_files(pathes,out_folder,merged_name),title_list



def concat_audio_mode_old(dir=CONCAT_SONG_DIR,merged_dir=MERGED_SAVE_DIR):
    oneMore=input('just enter for defualt or  any key choose pathes\n')==''
    pathes=[]
    title_list=list()
    if oneMore:
        filesnames = next(os.walk(CONCAT_SONG_DIR), (None, None, []))[2]  # [] if no file
        if filesnames == []:
            print("no files in concat defualt dir")
            exit
        for name in filesnames:
            title_list.append(name)
            pathes.append(CONCAT_SONG_DIR+"/"+name)
    while(not oneMore):
        path = input('enter song to be concat full path\n')
        pathes.append(path)
        title_list.append(path.split(sep='/')[-1])
        oneMore=input('enter for oneMore or any key for finish\n')!=''
    output = input('enter for defaualt dir or enter output path dir\n')
    mergedName= input("enter merged name\n")
    print("title_list")
    print(title_list)
    if output == '':
        return audio.concat_audio_files(pathes,MERGED_SAVE_DIR,mergedName),title_list
    else:
        return audio.concat_audio_files(pathes,output,mergedName),title_list
def start(c,s,d,mp4_format=False,merged_name="merged"):
    title_list=list()
    print(c,s,d,mp4_format)
    match c:
        case "AUDIO":
            if(d is None):
                d=MERGED_SAVE_DIR
            if(s is None):
                s=CONCAT_SONG_DIR
            merged_name,title_list=concat_audio_mode(s,d,merged_name)
        case "FILE":
            print("here")
            if(s is None):
                s=TEXT_FILE_PATH
            if(d is None):
                d=SONG_DIR
            title_list=file_mode(s,d,mp4_format)
        case "TEXT":
            if(d is None):
                d=SONG_DIR
            title_list=text_mode(s,d,mp4_format)
    if c!='AUDIO':
        print("\nThe title that downloaded are :\n"+general.str_list(title_list))
    else:
        print("\nThe title that merged are :\n{}\nThe merged name is:\n{}".format(general.str_list(title_list),merged_name))

def main():
    parser = argparse.ArgumentParser(description='youtube downloader or mp3 concating')
    parser.add_argument('mode',choices=VALID_INPUT, help='which mode to start')
    parser.add_argument('--source',help='from which dir to take files')
    parser.add_argument('--dest',help='to which dir to save files')
    parser.add_argument('-MP4',action="store_true",
                        help='is the format you want is MP4 (default:False)')
    parser.add_argument('--name',
                        help='name for the audio file that been merged')
    args = parser.parse_args()
    args = parser.parse_args()
    c=args.mode
    mp4_format=args.MP4
    d=args.dest
    s=args.source
    print(d,s)
    if(d is None):
        d= SONG_DIR
    merged_name=args.name if args.name!=None else "merged"
    print(c,args.source,args.dest,mp4_format,merged_name)
    #while(not check_input(c)):
    #   c=input('enter mode : concat, excel ,textFile or text :\n')
    #     c='text'
    start(c,s,d,mp4_format,merged_name)
if __name__ == "__main__":
    main()