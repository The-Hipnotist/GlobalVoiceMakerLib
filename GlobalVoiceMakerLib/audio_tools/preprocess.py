import subprocess as sp, os

def preprocess_and_resample_audio():
    '''
    This will preprocess and resample the audio to the correct format.
    '''
    print("Assuming the audio file is named 'original.wav'...")
    sp.run(["ffmpeg", "-y", "-i", "original.wav", "-ar", "48000", "mono.wav"], stdout=sp.PIPE)
    os.system("cls")
    print("Done.")