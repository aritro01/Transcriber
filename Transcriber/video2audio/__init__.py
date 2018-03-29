from ffmpy import FFmpeg


def video2audio(best):
    ff = FFmpeg(
        inputs={best.filename: None},
        outputs={'audio.wav': None}
    )

    ff.cmd
    ff.run()