from time import sleep, time
import moviepy.editor as mp

file = input("\nPlease [type or paste] the location of the video:\n> ")
inicio = int(time())

print(f"\nConverting [{file}] to audio..")
sleep(0.5)
print("Please wait!\n")

clip = mp.VideoFileClip(f"{file}")
clip.audio.write_audiofile(f"{file[:-3]}mp3")

print(f"\nFile [{file[:-3]}mp3] created..\n"
      f"Convertion cocluded in {int(time() - inicio)}s!\n\n"
      f"Thanks for the support.\n"
      f"© 2022 Nurul-GC\n"
      f"™ArtesGC Inc.")
