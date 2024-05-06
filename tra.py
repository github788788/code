exec(open('util.py').read())
def tra(inp):
	from pocketsphinx import LiveSpeech
	for phrase in LiveSpeech():
	    print(phrase)
inp = []
tra(inp)