def record_audio(RECORD_SECONDS):
    import pyaudio
    import wave
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def create_spect(wav_file):
    import os
    import wave

    import pylab
    def graph_spectrogram(wav_file):
        sound_info, frame_rate = get_wav_info(wav_file)
        pylab.figure(num=None, figsize=(19, 12))
        pylab.subplot(111)
        #pylab.title('spectrogram of %r' % wav_file)
        pylab.specgram(sound_info, Fs=frame_rate)
        pylab.savefig('spectrogram.png')
    def get_wav_info(wav_file):
        wav = wave.open(wav_file, 'r')
        frames = wav.readframes(-1)
        sound_info = pylab.fromstring(frames, 'int16')
        frame_rate = wav.getframerate()
        wav.close()
        return sound_info, frame_rate
    get_wav_info('output.wav')
    graph_spectrogram('output.wav')








def record_create_spect():
    import pyaudio
    import wave
    import speech_recognition as sr
    import os
    import pylab

    r = sr.Recognizer()
    hellow=sr.AudioFile('output.wav')
    with hellow as source:
    audio = r.record(source)
    try:
        s = r.recognize_google(audio)
        print("Text: "+s)
    except Exception as e:
        print("Exception: "+str(e))
    create_spect('output.wav')
    return s


