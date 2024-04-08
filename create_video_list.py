import tkinter as tk
from tkinter import *
import video_library as lib
import font_manager as fonts
import tkinter.scrolledtext as tkst
from tkinter import messagebox

# CREATE WINDOW    
class Create_video_list():
    def __init__(self, window):
        self.play_list = []
    
        window.title('Create video list')           # Set window title
        window.geometry('800x350')                  # Set window dimensions

        # Button to add a video
        add_btn = tk.Button(window, text="Add Video", command=self.add_video, fg= 'green')
        add_btn.grid(row=0, column=2, padx=10, pady=10)

        # Button to play videos
        play_btn = tk.Button(window, text="Play Video", command=self.play_video, fg= 'blue')
        play_btn.grid(row=0, column=4, padx=10, pady=10)

        # Button to reset the video list
        reset_btn = tk.Button(window, text="Reset",command=self.reset_video, fg= 'red')
        reset_btn.grid(row=0, column=3, padx=10, pady=10)

        # Label for entering video number
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        # Entry for entering video number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        # ScrolledText area to display the list of videos
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Text area to display selected videos
        self.video_txt = tk.Text(window, width=33, height=7, wrap="none")
        self.video_txt.grid(row=1, column=3,columnspan=3, sticky="NW", padx=10, pady=10)

        # Label to display status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # display the list of videos in ScrolledText
        lib.show_list_videos(self)

    # Method to handle the click event of the "Add video" button
    def add_video(self):
        key = self.input_txt.get()          # Get the video number entered by the user
        name = lib.get_name(key)            # Get the name of the video using the key
        if name is not None:                # If video found
            text = f"{name} \n"
            self.video_txt.insert(END, text)    # Display video name in the text area
            self.play_list.append(key)          # Add video key to the play list
            
        else:       # If video not found
            # Show warning message
            messagebox.showwarning('Warnig', f"Video {key} not found")
        # Update status label
        self.status_lbl.configure(text="Add Video button was clicked!")

    # Method to handle the click event of the "Reset Video" button
    def reset_video(self):
        self.play_list = []                     # Clear the play list
        self.video_txt.delete("1.0", END)       # Clear the text area
        # Update status label-
        self.status_lbl.configure(text="Reset button was clicked!")

    # Method to handle the click event of the "Play Video" button
    def play_video(self):
        self.video_txt.delete("1.0", END)       # Clear the text area
        # Increment play count for each video in the play list
        for key in self.play_list:
            lib.increment_play_count(key)
            text = f"{lib.get_name(key)} - plays: {lib.get_play_count(key)} \n"
            self.video_txt.insert(END, text)

        # Update status label       
        self.status_lbl.configure(text="Play Video button was clicked!")


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    Create_video_list(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
