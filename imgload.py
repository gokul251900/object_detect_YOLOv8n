from tkinter import Tk, filedialog

def load_img():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"),
            ("All Files", "*.*"),
        ],
    )
    return file_path
