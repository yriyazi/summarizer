import subprocess
import importlib

required_libraries = [
    'torch', 'pyaudio', 'wave', 'numpy', 
    'transformers', 'scipy'
]

conda_command = 'conda install'
pip_command = 'pip install'

for library in required_libraries:
    try:
        importlib.import_module(library)
    except ImportError:
        print(f'{library} not found. Installing...')
        if 'conda' in subprocess.run(['which', 'python'], capture_output=True, text=True).stdout:
            subprocess.run([conda_command, library, '-y'])
        else:
            subprocess.run([pip_command, library])

print('All required libraries are installed.')


