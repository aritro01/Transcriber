import ytd
import video2audio
import slicer
import subgen

best = ytd.start()
ytd.save(best)
video2audio.video2audio(best)
slicer.slice()
subgen.makesub()
