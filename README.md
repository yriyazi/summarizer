# summarizer (Speech-to-Text and Summarization with Hugging Face and OpenAI)

Welcome to the Speech-to-Text and Summarization project! This repository demonstrates how to use Hugging Face and OpenAI models to convert spoken language into text and generate concise summaries.

## Overview

This project provides a Python script that utilizes Hugging Face's Speech-to-Text model for transcribing audio files. It then leverages OpenAI's Summarization model to create concise summaries from the transcribed text. Additionally, you can integrate FFMpeg for further processing of audio or video files.

## Getting Started

1. Clone the repository to your local machine:

```
git clone https://github.com/yriyazi/summarizer.git
cd speech-to-text-summarization
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure you have audio files for testing in the `audio_files` directory.

4. Execute the provided Python script:

```bash
python main.py
```

## Usage

### 1. Speech-to-Text Conversion

The script uses Hugging Face's Speech-to-Text pipeline to convert audio files to text. Simply place your audio files in the `audio_files` directory and run the script.

### 2. Summarization

After obtaining the transcriptions, the OpenAI Summarization model is used to generate concise summaries. You can adjust the summarization parameters in the code to suit your specific needs.

### 3. Additional Processing with FFMpeg

Integrate your FFMpeg code to further process the audio or video files as needed.

## Example Code

```python
import transformers
from transformers import pipeline

# Speech to Text using Hugging Face
speech_to_text = pipeline('speech-to-text')
audio_input = "your_audio_file.wav"
text_output = speech_to_text(audio_input)[0]['transcription']

# Summarization using OpenAI Model
summarizer = pipeline('summarization')
summary = summarizer(text_output, max_length=100, min_length=30, do_sample=False)[0]['summary_text']

# Further processing or utilization with FFMpeg
# Add your FFMpeg code here

# Now you have a powerful toolset at your fingertips! 🛠️ Let's turn speech into valuable insights and summaries effortlessly. 💡
```

## Contributing

We welcome contributions! If you have any ideas or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to explore, experiment, and innovate with this powerful combination of technologies! If you have any questions or need further assistance, please don't hesitate to reach out. Happy coding! 🚀