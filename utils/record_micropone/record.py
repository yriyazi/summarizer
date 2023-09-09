import wave
import numpy as np

def save_wave_file(cached_audio,
                   p,
                   CHANNELS,
                   FORMAT,
                   RATE,
                   AMPLIFICATION_FACTOR=10, output_file="cached_audio.wav"):
    """
    Save the cached audio data to a WAV file.

    Args:
        cached_audio (numpy.ndarray): The audio data to be saved.
        p (pyaudio.PyAudio): PyAudio instance.
        AMPLIFICATION_FACTOR (int, optional): Amplification factor for the audio. Default is 10.
        output_file (str, optional): Output file path. Default is "cached_audio.wav".
    """
    # Save the cached audio to a WAV file
    with wave.open(output_file, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes((cached_audio * AMPLIFICATION_FACTOR).tobytes())
    print(f"Saved cached audio to {output_file}")


def record_audio(pyaudio,
                 CHANNELS,
                 FORMAT,
                 RATE,
                 CHUNK,
                 ):
    """
    Record audio from the microphone.

    Returns:
        tuple: Numpy array of recorded audio and PyAudio instance.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    # Initialize an empty list to store audio data
    audio_cache = []
    try:
        print("Recording... (Press Ctrl+C to stop)")
        while True:
            # Read audio data from the microphone
            data = stream.read(CHUNK)

            # Convert the binary audio data to a numpy array
            audio_sample = np.frombuffer(data, dtype=np.int16)

            # Append the audio sample to the cache
            audio_cache.append(audio_sample)

    except KeyboardInterrupt:
        print("Recording stopped.")

    # Close the audio stream and PyAudio instance
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Convert the list of audio samples into a numpy array
    return np.concatenate(audio_cache), p
