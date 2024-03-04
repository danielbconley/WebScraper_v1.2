from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import math
import os

video_path = "YOUR VIDEO FOLDER PATH GOES HERE"
output_dir = "YOUR OUTPUT FOLDER PATH GOES HERE"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

video = VideoFileClip(video_path)
num_segments = math.ceil(video.duration / 60)

# makes the text the correct size and sets the position
def add_text(clip, part_text, username_text, fontsize=60, username_fontsize=30, position=("center", "top")):
    vertical_position = int(clip.size[1] * 2 / 3) - 950  # Adjusting from the top to be slightly lower for "Part" text
    part_txt_clip = TextClip(part_text, fontsize=fontsize, color='white', font="Arial", bg_color='black').set_position(("center", vertical_position)).set_duration(clip.duration)t
    username_vertical_position = vertical_position + fontsize  # Adjust based on the fontsize of the "Part" text
    username_txt_clip = TextClip(username_text, fontsize=username_fontsize, color='white', font="Arial", bg_color='black').set_position(("center", username_vertical_position)).set_duration(clip.duration)
    
    return CompositeVideoClip([clip, part_txt_clip, username_txt_clip])

# splits the video into 1 minute segments and adds channel name/part number at the top
for i in range(num_segments):
    start_time = i * 60
    end_time = min((i + 1) * 60, video.duration)
    segment = video.subclip(start_time, end_time)
    part_text = f"Part {i+1}"
    username_text = "YOUR CHANNEL NAME GOES HERE"  # Text to be added below "Part 1"
    segment_with_text = add_text(segment, part_text, username_text)
    segment_filename = os.path.join(output_dir, f"finalvideo_part{i+1}.mov")
    segment_with_text.write_videofile(segment_filename, codec="libx264", fps=24)

print("All segments have been created successfully.")
