from moviepy.editor import AudioFileClip,concatenate_audioclips

def mp4_to_mp3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

def concat_audio_files(pathes,output_path,mergedName="merged"):
    clips = [AudioFileClip(c) for c in pathes]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path+"/"+mergedName+".mp3")
    return mergedName+".mp3"
