from pydub import AudioSegment
import os
import re

from pydub.playback import play

# Specify the path to ffprobe
AudioSegment.ffmpeg = "/opt/homebrew/bin/ffmpeg"
AudioSegment.ffprobe = "/opt/homebrew/bin/ffprobe"

# Function to combine MP3 files based on their names
def combine_files(folder_path, prefix):
    # Get all files in the folder
    files = os.listdir(folder_path)
    
    # Filter files based on the prefix
    matching_files = [file for file in files if file.startswith(prefix)]
    
    # Sort matching files based on the numerical part of the name
    matching_files.sort(key=lambda x: int(re.search(r'\d+', x).group()))
    
    # Combine the audio segments
    combined = AudioSegment.silent()
    for file_name in matching_files:
        file_path = os.path.join(folder_path, file_name)
        segment = AudioSegment.from_mp3(file_path)
        combined += segment
    
    # Export the combined audio
    output_path = os.path.join(folder_path, f"{prefix}_combined.mp3")
    combined.export(output_path, format="mp3")
    
    print(f"Combined files {prefix}_01 to {prefix}_{len(matching_files)} into {output_path}")

# Replace 'path_to_your_folder' with the path to the folder containing your MP3 files
folder_path = '/Users/jieranli/Downloads/delftsemethodegood/groenboek'

# Combine files for each prefix
for prefix in [f"les{i:02d}" for i in range(1, 43)]:
    combine_files(folder_path, prefix)
