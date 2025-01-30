from random import Random
from tkinter import *
from PIL import Image, ImageTk



class Application:
    def __init__(self):
        self.root = Tk()
        self.root.title("BMO")
        self.image_paths = {
            "smile": "faces/smile.jpg",
            "idle": "faces/sleep.jpg",
            "uncertain": "faces/derp.jpg",
            "loading": "faces/loading.jpg",
            "error": "faces/worried.jpg"
        }
        self.face = Label(self.root)
        self.face.pack(side="top", fill=BOTH)

        self.load_image("smile")
        self.root.attributes("-fullscreen", False)

        self.root.bind("<Return>", self.change_face)

        self.root.mainloop()

    def load_image(self, image_name):
        selected_face = self.image_paths[image_name]
        image = Image.open(selected_face)
        face = ImageTk.PhotoImage(image)
        self.face.configure(image=face)
        self.face.image = face


    def change_face(self, event):
        random = Random()
        r = random.randrange(0, len(self.image_paths.items()))
        faces = list(self.image_paths.keys())
        print(faces[r])
        self.load_image(faces[r])


def main():
    app = Application()



if __name__ == '__main__':
    main()
