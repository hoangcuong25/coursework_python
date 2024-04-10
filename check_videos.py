import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox
import video_library as lib
import font_manager as fonts
from PIL import Image, ImageTk

# CREATE WINDOW
class CheckVideos():                          
    def __init__(self, window):
        window.geometry("850x350")              # Set window dimensions, width = 850, height = 350
        window.title("Check Videos")            # Set window title, title is "Check Videos"

        # Button to list all videos
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked, fg= 'blue')   # Create button List All Videos, set color is blue
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)                                                     # Set location for button List All Videos (row=0, column=0, padx=10, pady=10)

        # Label for entering video number
        enter_lbl = tk.Label(window, text="Enter Video Number")                                                     # Create Label Enter Video Number
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)                                                           # Set location for Label List All Videos (row=0, column=1, padx=10, pady=10)

        # Entry for entering video number  
        self.input_txt = tk.Entry(window, width=3)                                                                  # Create Texbox
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)                                                      # Set location for Texbox (row=0, column=2, padx=10, pady=10)

        # Button to check a video
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked, fg= 'blue')       # Create button Check Video, set color is blue
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)                                                     # Set location for button List All Videos (row=0, column=3, padx=10, pady=10)

        # ScrolledText area to display video details
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")                                 # Create ScrolledText area
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)                             # Set location for ScrolledText area (row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Text area to display the list of videos
        self.video_txt = tk.Text(window, width=37, height=4, wrap="none")                                           # Create Text area
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)                                         # Set location for Text area (row=1, column=3, sticky="NW", padx=10, pady=10) 

        # Label to display status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))                                         # Create Label status messages, font = Helvetica
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)                           # Set location for status messages (row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Label to display video image
        self.image_lbl = tk.Label(window)
        self.image_lbl.grid(row= 1, column=3, sticky= "S")                                                          # Set location for image (row= 1, column=3, sticky= "S")

        self.list_videos_clicked()                                                                                  # Display the list of videos in ScrolledText

    # Method to handle the click event of the "Check Video" button
    def check_video_clicked(self):
        key = self.input_txt.get()                  # Get the video number entered by the user
        name = lib.get_name(key)                    # Get the name of the video using the key
        
        if name is not None:                        # If video found
            # Get details of the video
            director = lib.get_director(key)        # Get director using the key
            rating = lib.get_rating(key)            # Get rating using the key
            play_count = lib.get_play_count(key)    # Get play count using the key

            # Get and display video image
            image = self.image(key)
            self.image_lbl.configure(image = image)
            self.image_lbl.image = image

            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"     # Format video details
            lib.set_text(self.video_txt, video_details)                                      # Display video details in Text area
            
        else:                                                                # If video not found
            messagebox.showwarning('Warnig', f"Video {key} not found")       # Show warning message
        self.status_lbl.configure(text="Check Video button was clicked!")    # Update status label

    # Method to handle the click event of the "List All Videos" button
    def list_videos_clicked(self):
        video_list = lib.list_all()                                         # Get the list of all videos
        lib.set_text(self.list_txt, video_list)                             # Display the list of videos in ScrolledText
        self.status_lbl.configure(text="List Videos button was clicked!")   # Update status label

    def image(self, key):
        # Load and resize image associated with the video
        image = lib.get_image_path(key)
        image = Image.open(image)
        image = image.resize((250,150), Image.BICUBIC)
        image = ImageTk.PhotoImage(image)
        return image

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc