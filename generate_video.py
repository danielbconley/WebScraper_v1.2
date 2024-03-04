from moviepy.editor import AudioFileClip, VideoFileClip, ImageClip, concatenate_videoclips, CompositeVideoClip
import os
import random 

images_path = "YOUR IMAGE FOLDER PATH GOES HERE"
audio_path = "YOUR AUDIO FOLDER PATH GOES HERE"
background_video_path = "YOUR BACKGROUND VIDEO FOLDER PATH GOES HERE"

# list all background video files in the folder
background_files = [f for f in os.listdir(background_video_path) if f.startswith('background') and f.endswith('.mov')] # make sure the file name is in the style of "background1.mov"
# select a random background video file
selected_background_file = random.choice(background_files)
selected_background_path = os.path.join(background_video_path, selected_background_file)

# load the random background video
background_clip = VideoFileClip(selected_background_path)

all_clips = []

# load and position the title image to stay on screen for the entire video
title_image_path = os.path.join(images_path, "title.png")
title_clip = ImageClip(title_image_path)  # Don't set duration yet, it will be set later based on total duration

# Process saved audio and images to create video clips
paragraph_numbers = sorted([int(f.replace('paragraph', '').replace('.mp3', '')) for f in os.listdir(audio_path) if f.startswith('paragraph')])
for num in paragraph_numbers:
    audio_filename = os.path.join(audio_path, f"paragraph{num}.mp3")
    image_filename = os.path.join(images_path, f"paragraph{num}.png")
    
    audio_clip = AudioFileClip(audio_filename)
    image_clip = ImageClip(image_filename).set_duration(audio_clip.duration)
    
    video_clip_with_audio = image_clip.set_audio(audio_clip)
    all_clips.append(video_clip_with_audio)

# concatenate all content clips to calculate total duration
concatenated_content_clip = concatenate_videoclips(all_clips, method="compose")

# sets the duration of the title clip to match the total content duration and position it
title_clip = title_clip.set_duration(concatenated_content_clip.duration).set_position(('center', 200))  # Adjust the 50px from the top as needed

# loop the background clip to match the total content duration
looped_background_clip = background_clip.loop(duration=concatenated_content_clip.duration)

# overlay the content and the title on the looped background
final_clip = CompositeVideoClip([looped_background_clip, concatenated_content_clip.set_position("center"), title_clip], size=looped_background_clip.size)

# export the final video
final_output = "YOUR OUTPUT FOLDER GOES HERE"
final_clip.write_videofile(final_output, fps=24)

print(f"Video successfully created: {final_output}")
