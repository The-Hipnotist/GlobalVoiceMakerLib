import auditok, os, shutil, time, glob, random, wave

def split_audio_into_chunks(min_dur: int, max_dur: int, new_name: str, print_total_length_and_amount_of_files: bool):
    '''
    Splits the file into multiple files and trims silent parts of the audio file.


    min_dur: The minimum duration to cut.
    
    max_dur: The maximum duration to cut.
    
    new_name: The new name to set the split audio files to. This can be any name, or the name of the voice you are cloning. Format is {new_name-[incrementing_numbers]}.wav
    
    print_total_length_and_amount_of_files: Scans through the directory and prints the total length of audio files as well as the amount.
    '''
    name_of_file = "original.wav"
    foldername = "wavs"
    folderpath = f'{foldername}/';
    folderpath2 = 'converted/';
    if os.path.exists(foldername):
        print("Wavs folder exists. Removing and making fresh one...")
        shutil.rmtree(foldername)
        os.mkdir(foldername)
    else:
        os.mkdir(foldername)
        shutil.move("mono.wav", "wavs/")
        os.system("cls")
        name = new_name
        print(f'Name has been set as: {name}')
        time.sleep(1)
        os.mkdir(folderpath2)
        os.rename("wavs/mono.wav", "converted/mono.wav")
        os.rmdir(foldername)
        if os.path.exists("splitaudio"):
            pass
        else:
            os.mkdir("splitaudio")
        shutil.move("converted/mono.wav", "splitaudio/mono.wav")
        os.rmdir("converted")
        time.sleep(1)
        os.system("cls")
        audioregions = auditok.split(
            "splitaudio/mono.wav",
            min_dur=min_dur,
            max_dur=max_dur,
            max_silence=0.3,
            energy_threshold=45,
        )
        for i, r in enumerate(audioregions):
            filename = r.save("Region_{meta.start:3f}-{meta.end:.3f}.wav")
        for f in sorted(glob.glob("*.wav")):
            new = new_name + "-" + str(random.randint(1, 910719)) + ".wav"
            os.rename(f, new)
        os.remove("splitaudio/mono.wav")
        for o in glob.glob(f"{new_name}-*.wav"):
            shutil.move(o, "splitaudio")
        filecount = len([q for q in os.listdir('splitaudio') if os.path.isfile(os.path.join('splitaudio', q))])
        totalmins = 0
        if print_total_length_and_amount_of_files == True:
            for y in glob.glob("splitaudio/*.wav"):
                with wave.open(y, 'rb') as wavefile:
                    framerate = wavefile.getframerate()
                    frames = wavefile.getnframes()
                    duration = frames / float(framerate)
                    totalmins = totalmins + duration
            totalmins = round(totalmins / 60, 1)
            print(f"There is a total length of {totalmins} minutes across {filecount} files.")
            time.sleep(3)
            return