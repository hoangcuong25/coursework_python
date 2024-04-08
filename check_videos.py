import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox
import video_library as lib
import font_manager as fonts


def set_text(text_area, content):           # then the new content is inserted 
    text_area.delete("1.0", tk.END)         # first the existing content is deleted     
    text_area.insert(1.0, content)          # then the new content is inserted 

# CREATE WINDOW
class CheckVideos():                          
    def __init__(self, window):
        window.geometry("850x350")              # Set window dimensions
        window.title("Check Videos")            # Set window title

        # Button to list all videos
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked, fg= 'blue')
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        # Label for entering video number
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Entry for entering video number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Button to check a video
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked, fg= 'blue')
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        # Text area to display the list of videos
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # ScrolledText area to display video details
        self.video_txt = tk.Text(window, width=37, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Label to display status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # display the list of videos in ScrolledText
        self.list_videos_clicked()

    # Method to handle the click event of the "Check Video" button
    def check_video_clicked(self):
        key = self.input_txt.get()                  # Get the video number entered by the user
        name = lib.get_name(key)                    # Get the name of the video using the key
        if name is not None:                        # If video found
            # Get details of the video
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            # Format video details
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            # Display video details in ScrolledText
            set_text(self.video_txt, video_details)
        else:                                       # If video not found
            # Show warning message
            messagebox.showwarning('Warnig', f"Video {key} not found")
            # Update status label
        self.status_lbl.configure(text="Check Video button was clicked!")

    # Method to handle the click event of the "List All Videos" button
    def list_videos_clicked(self):
        # Get the list of all videos
        video_list = lib.list_all()
        # Display the list of videos in ScrolledText
        set_text(self.list_txt, video_list)
        # Update status label
        self.status_lbl.configure(text="List Videos button was clicked!")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc