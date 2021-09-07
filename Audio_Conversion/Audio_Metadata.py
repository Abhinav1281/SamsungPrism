import pandas as pd
from glob import glob
import librosa as lr
from pydub import AudioSegment as AS
import os
import math
dir=input('Input directory to read from:')
audio_files=glob(dir + '/*.wav')
print(f"{len(audio_files)} files available")
columns=['FILENAME','FOLDER','CLASS_ID','CLASS']
#print(f"{len(columns)}")
label=input("Enter Class id.:");
df=pd.DataFrame(columns=columns)
for aud in audio_files:
    audioName=str(os.path.basename(aud))
    aud=[audioName,'Fold'+label,label,'Public_Places']
    #print(f"{len(audio)}")
    #print(f"{int(math.floor(len(audio))/int(s))}")
    # print(f"{len(aud)}")
    df.loc[len(df.index)]=aud
filename=input('Enter Filename to store to:')
#print(f"{df}")
df.to_csv(filename)