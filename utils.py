########################################
# Various Utilities for TeaMachine GUI #
########################################

try:
    import winsound
except ImportError:
    winsound = None

import subprocess


def playWavSound(fileName, blocking=True):
    try:
        if winsound:
            winsound.PlaySound(fileName, winsound.SND_FILENAME | (winsound.SND_ASYNC if not blocking else 0))
        else:
            subprocess.run(["aplay", not blocking and "-N" or "", fileName], shell=False)
    except Exception as e:
        print(f"Unable to play sound: {e}")