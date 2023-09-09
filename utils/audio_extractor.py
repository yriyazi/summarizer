import subprocess

def encode_to_x265(input_file, output_file):
    """
    Encode a video file to x265 format using FFmpeg.

    :param input_file: Input video file path.
    :param output_file: Output file path for the encoded video.
    """
    # Use FFmpeg with libx265 to encode the video file
    ffmpeg_cmd = f'ffmpeg -i  "{input_file}" -vn -acodec pcm_s16le -ar 16000 -ac 1 "{output_file}"'
    subprocess.run(ffmpeg_cmd, shell=True)

def write_text_to_file(filename, text):
    """
    Write a text string to a file.

    :param filename: The name of the file to write to.
    :param text: The text string to write to the file.
    """
    try:
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Text has been written to {filename}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
