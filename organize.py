import os
from pathlib import Path

SUBDIECTORIES={
"DOCUMENTS":['.pdf','.rtd','.txt'],
"AUDIO":['.m4a','.m4b','.mp3'],
"VIDEOS":['.mov','.avi','.mp4'],
"IMAGES":['.jpg','jpeg','.png']}

def pickDirectory(value):
    for category,suffixes in SUBDIECTORIES.items():
        for suffix in suffixes:
            if suffix==value:
                return category

        return 'x'


#print(pickDirectory('.pdf'))

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath=Path(item)
        filetype=filePath.suffix.lower()
        directory=pickDirectory(filetype)
        if(directory != 'x'):
            directoryPath=Path(directory)
            if directoryPath.is_dir()!=True:
                directoryPath.mkdir()
            filePath.rename(directoryPath.joinpath(filePath))

def main():
    organizeDirectory()

if __name__=="__main__":
    main()