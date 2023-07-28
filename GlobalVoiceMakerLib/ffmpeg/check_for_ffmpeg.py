import subprocess as sp

def run_checker():
    '''
    Runs a Subprocess cmd to check if ffmpeg exists in PATH and C:.
    
    Returns True if so, and False if not.
    '''
    try:
        sp.check_call(["ffmpeg", "-version"], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
        return print("True.")
    except FileNotFoundError or sp.CalledProcessError:
        return print("False.")