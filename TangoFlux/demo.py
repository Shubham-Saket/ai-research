import torchaudio
from tangoflux import TangoFluxInference
from datetime import datetime

s = datetime.now()
model = TangoFluxInference(name='declare-lab/TangoFlux')
audio = model.generate('A ghost crying', steps=50, duration=5)
torchaudio.save('output.wav', audio, 44100)
print(datetime.now()-s)

