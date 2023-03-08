from moviepy.editor import *

CONCAT_SAVE_DIR="C:/Users/SmadarENB3/Desktop/songs/concat/merged"
SONG_DIR="C:/Users/SmadarENB3/Desktop/songs/concat"
VALID_INPUT=['','concat']
TITLE_LIST_FOR_PRINT=list()


def mp4_to_mp3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

def concat_audio_files(pathes,output_path,mergedName):
    print(pathes)
    print(output_path)
    print(mergedName)
    clips = [AudioFileClip(c) for c in pathes]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path+"/"+mergedName+".mp3")

def concat_audio_mode():
    oneMore=input('just enter for choose pathes or any key for defualt \n')==''
    pathes=[]
    if not oneMore:
        filesnames = next(os.walk(SONG_DIR), (None, None, []))[2]  # [] if no file
        if filesnames == []:
            print("no files in concat defualt dir")
            exit
        for name in filesnames:
            TITLE_LIST_FOR_PRINT.append(name)
            pathes.append(SONG_DIR+"/"+name)
    while(oneMore):
        path = input('enter song to be concat full path\n')
        pathes.append(path)
        oneMore=input('enter for oneMore or any key for finish\n')==''
    output = input('enter for defaualt dir or enter output path dir\n')
    mergedName= input("enter merged\n")
    if output == '':
        concat_audio_files(pathes,CONCAT_SAVE_DIR,mergedName)
    else:
        concat_audio_files(pathes,output,mergedName)


def check_input(c):
    valid=c in VALID_INPUT
    if not valid:
        msg="the input: '{c}' is illegal \nplease enter one of the valid inputs as \n{valid_list}".format(c=c,valid_list=VALID_INPUT)
        print(msg)
    return valid

def str_list(l, newLine=True):
    s=""
    for i in l:
        if newLine:
            s=s+i+"\n"
        else:
            s=s+i
    return s[:-1] if  newLine else s

def main():
    c=''
    while(not check_input(c)):
        c=input('enter mode : concat \n')
    concat_audio_files()
    print("\nthe title that merged are :\n",str_list(TITLE_LIST_FOR_PRINT))



if __name__ == "__main__":
    main()