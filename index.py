from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

location = ""

# download location
def d_location():
    global location
    location = filedialog.askdirectory()
    if len(location) > 1:
        path_error.config(text=location, fg="green")
    else:
        path_error.config(text="Please choose a valid path", fg="red")


# downloading video
def DownloadVideo():
    d_quality = q_choice.get()
    url = link_entry.get()

    if len(url) > 1:
        error.config(text='')
        yt = YouTube(url)

        if d_quality == q[0]:
            select = yt.streams.filter(progressive=True).first()
        elif d_quality == q[1]:
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()
        elif d_quality == q[2]:
            select = yt.streams.filter(only_audio=True).first()
        else:
            error.config(text="Paste a valid URL", fg="red")

    select.download(location)
    error.config(text="Download Completed !!", fg="green")


root = Tk()
root.title("Youtube Downloader")  # gives title to the dialouge box
root.geometry("350x400")  # sets the dimension of the dialog box
root.columnconfigure(0, weight=1)  # center alignment

# Link
link = Label(root, text="Paste your video link here", font=("Roboto", 15, "bold"))
link.grid()

# Link Paste Box
link_entered = StringVar()
link_entry = Entry(root, width=30, textvariable=link_entered)
link_entry.grid()

# Error Message
error = Label(root, text="The Link format is Invalid", fg="red", font=("Roboto", 10))
error.grid()

# Save
save = Label(root, text="Where to Download the File ?", fg="blue", font=("Roboto", 15, "bold"))
save.grid()

# SAVEFILE BUTTON
btn = Button(root, width=10, bg="white", fg="black", text="Choose Path", command=d_location)
btn.grid()

# PathError
path_error = Label(root, text="Choose a valid path !!", fg="red", font=("jost", 10))
path_error.grid()

# Download Quality
quality = Label(root, text="Select Quality", font=("Roboto", 15))
quality.grid()

# Quality Box
q = ["720p", "360p", "Only Audio"]
q_choice = ttk.Combobox(root, values=q)
q_choice.grid()

# Download Button
download_btn = Button(root, text="Download", width=10, bg="white", fg="black", font=("Roboto", 10, "bold"),
                      command=DownloadVideo)
download_btn.grid()
root.mainloop()  # we have to do this task in loop so use mainloop
