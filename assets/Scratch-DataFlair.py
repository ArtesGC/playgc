# ==== Importing all the necessary libraries
from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk
import moviepy.editor as mp


# ==== creating main class
class VideoAudioConverter:
    # ==== creating gui window
    def __init__(self, root):
        self.root = root
        self.root.title("VIDEO-AUDIO CONVERTER by DataFlair")
        self.root.geometry('1280x720')
        self.bg = ImageTk.PhotoImage(file="bg_image.jpg")
        Label(self.root, image=self.bg).place(x=0, y=0)

        Button(self.root, text="Browse Files", font=("times new roman", 15), command=self.browse).place(x=40, y=630)

    # ==== browse data from system
    def browse(self):
        self.file_name = filedialog.askopenfilename(title="Select a File", filetypes=(("Video files", "*.mp4*"),))

        Label(self.root, text=os.path.basename(self.file_name), font=("times new roman", 20), bg="blue").place(x=200, y=630)

        Label(self.root, text='Processing...', font=("times new roman", 30)).place(x=600, y=630)
        self.convert(os.path.basename(self.file_name))

        Label(self.root, text='Completed!!', font=("times new roman", 30)).place(x=1000, y=630)

    # ==== convert video to audio
    def convert(self, path):
        clip = mp.VideoFileClip(r'{}'.format(path))
        clip.audio.write_audiofile(r'{}mp3'.format(path[:-3]))


# ==== creating main function
def main():
    # ==== create tkinter window
    root = Tk()
    # === creating object for class VideoAudioConverter
    obj = VideoAudioConverter(root)
    # ==== start the gui
    root.mainloop()


if __name__ == "__main__":
    # ==== calling main function
    main()
