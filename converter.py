import moviepy.editor

# carrega arquivo do video
video = moviepy.editor.VideoFileClip("exemple.mp4")

# extrai apenas o audio do video
audio_data = video.audio

# salva o o arquivo do audio extraido do video
audio_data.write_audiofile("exemple.mp3")
