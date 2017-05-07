# import matplotlib.pyplot as plt
import sunau
import numpy as np
# from features import mfcc
from python_speech_features import mfcc

class Au(sunau.Au_read):
	"""docstring for  """

	def getsignal(self):
		width = self.getsampwidth()
		signal = self.readframes(-1)
		self.rewind()
		channelNum = self.getnchannels()
		signal = np.fromstring(signal, dtype=np.dtype('>h'))
		signal = signal/32767.0000000
		return signal
		#return signal.tolist()

	def plotwaveform(self):
		signal = self.getsignal()
		Time=np.linspace(0, len(signal)/self.getframerate(), num=len(signal))
		scale = [0,Time[-1],-1,1]
		plt.plot(Time,signal)
		plt.axis(scale)
		plt.show()

	def feat(self):
		mfcc_feat = mfcc(self.getsignal(),self.getframerate(),numcep=39,nfilt=39)
		return np.concatenate((np.mean(mfcc_feat,0), np.std(mfcc_feat,0),np.amax(mfcc_feat,0),np.amin(mfcc_feat,0)), axis=0)
