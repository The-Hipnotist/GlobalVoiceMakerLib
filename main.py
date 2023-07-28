from GlobalVoiceMakerLib.downloader import YouTube
from GlobalVoiceMakerLib.ffmpeg import check_for_ffmpeg
from GlobalVoiceMakerLib.audio_tools import preprocess
from GlobalVoiceMakerLib.slice import split

check_for_ffmpeg.run_checker()
linkto = input("Enter link: ")
YouTube.download_video(linkto)
preprocess.preprocess_and_resample_audio()
split.split_audio_into_chunks(
    min_dur=1,
    max_dur=5,
    new_name="test",
    print_total_length_and_amount_of_files=True
)
