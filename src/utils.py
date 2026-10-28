########################################
# Various Utilities for TeaMachine GUI #
########################################

try:
    import winsound
except ImportError:
    winsound = None

import subprocess
from pathlib import Path


def playWavSound(fileName, blocking=True):
    try:
        soundPath = Path(fileName)
        if not soundPath.is_file():
            # Fall back to resolving relative paths against this file's folder
            soundPath = Path(__file__).parent / soundPath

        if winsound:
            winsound.PlaySound(str(soundPath), winsound.SND_FILENAME | (winsound.SND_ASYNC if not blocking else 0))
        else:
            subprocess.run(["aplay", not blocking and "-N" or "", str(soundPath)], shell=False)
    except Exception as e:
        print(f"Unable to play sound: {e}")