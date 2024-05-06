exec(open('util.py').read())
def rec(inp):

	"""
	import pyaudio 
	# detect devices:
	p = pyaudio.PyAudio()
	host_info = p.get_host_api_info_by_index(0)    
	device_count = host_info.get('deviceCount')
	devices = []
	# iterate between devices:
	for i in range(0, device_count):
	    device = p.get_device_info_by_host_api_device_index(0, i)
	    devices.append(device['name'])
	print (	devices)	
	"""

	"""
	# import required libraries
	import sounddevice as sd
	from scipy.io.wavfile import write
	import wavio as wv
	# Sampling frequency
	freq = 44100
	# Recording duration
	duration = 5
	# Start recorder with the given values 
	# of duration and sample frequency
	recording = sd.rec(int(duration * freq), 
	                   samplerate=freq, channels=2)
	# Record audio for the given number of seconds
	sd.wait()
	# This will convert the NumPy array to an audio
	# file with the given sampling frequency
	write("recording0.wav", freq, recording)
	# Convert the NumPy array to audio file
	wv.write("recording1.wav", recording, freq, sampwidth=2)
	"""
	"""
	import soundcard as sc
	import numpy
	# get a list of all speakers:
	speakers = sc.all_speakers()
	# get the current default speaker on your system:
	default_speaker = sc.default_speaker()
	# get a list of all microphones:
	mics = sc.all_microphones()
	# get the current default microphone on your system:
	default_mic = sc.default_microphone()
	# search for a sound card by substring:
	#>>> sc.get_speaker('Scarlett')
	#<Speaker Focusrite Scarlett 2i2 (2 channels)>
	#>>> one_mic = sc.get_microphone('Scarlett')
	#<Microphone Focusrite Scalett 2i2 (2 channels)>
	# fuzzy-search to get the same results:
	#one_speaker = sc.get_speaker('FS2i2')
	#one_mic = sc.get_microphone('FS2i2')
	#print(speakers)
	print(speakers[0])
	data = default_speaker.record(samplerate=48000, numframes=48000)
	# normalized playback
	default_speaker.play(data/numpy.max(numpy.abs(data)), samplerate=48000)
	"""

	import wave, struct, math, random
	sampleRate = 44100.0 # hertz
	duration = 1.0 # seconds
	frequency = 440.0 # hertz
	obj = wave.open('sound.wav','w')
	obj.setnchannels(1) # mono
	obj.setsampwidth(2)
	obj.setframerate(sampleRate)
	for i in range(10):
	   value = random.randint(-32767, 32767)
	   data = struct.pack('<h', value)
	   obj.writeframesraw( data )
	obj.close()

inp = []
rec(inp)