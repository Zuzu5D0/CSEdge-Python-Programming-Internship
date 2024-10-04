import pyaudio
import wave
import numpy as np
import soundfile as sf

class VoiceRecorder:
    def __init__(self, channels=1, rate=44100, chunk=1024):
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.frames = []
        self.audio_interface = pyaudio.PyAudio()

    def start_recording(self):
        print("Recording started...")
        self.frames = []
        stream = self.audio_interface.open(format=pyaudio.paInt16,
                                           channels=self.channels,
                                           rate=self.rate,
                                           input=True,
                                           frames_per_buffer=self.chunk)

        try:
            while True:
                data = stream.read(self.chunk)
                self.frames.append(data)
        except KeyboardInterrupt:
            print("Recording stopped.")
        finally:
            stream.stop_stream()
            stream.close()

    def save_recording(self, filename, file_format='WAV'):
        if file_format.upper() == 'WAV':
            self.save_as_wav(filename)
        elif file_format.upper() == 'FLAC':
            self.save_as_flac(filename)
        else:
            print("Unsupported format. Please use 'WAV' or 'FLAC'.")

    def save_as_wav(self, filename):
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.audio_interface.get_sample_size(pyaudio.paInt16))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(self.frames))
        print(f"Recording saved as {filename}")

    def save_as_flac(self, filename):
        data = np.frombuffer(b''.join(self.frames), dtype=np.int16)
        sf.write(filename, data, self.rate, format='FLAC')
        print(f"Recording saved as {filename}")

    def close(self):
        self.audio_interface.terminate()

if __name__ == "__main__":
    recorder = VoiceRecorder()

    try:
        recorder.start_recording()
    except Exception as e:
        print(f"Error: {e}")

    # Ask for filename and format
    filename = input("Enter filename to save (without extension): ")
    file_format = input("Enter file format (WAV/FLAC): ")
    recorder.save_recording(f"{filename}.{file_format}", file_format)

    recorder.close()
