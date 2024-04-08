import tkinter as tk
from tkinter import *
import video_library as lib
import font_manager as fonts
from library_item import LibraryItem
import tkinter.scrolledtext as tkst
from tkinter import messagebox


# CREATE WINDOW
class Update_video():
    def __init__(self, window):

        window.title('Update videos')       # Set window title
        window.geometry('800x350')          # Set window dimensions

        # Button to update a video
        update_btn = tk.Button(window, text="Update Video",command=self.update_video, fg = 'blue' )
        update_btn.grid(row=0, column=0, padx=10, pady=10)

        # label for entering video number
        number_lbl =tk.Label(window, text='Number')
        number_lbl.grid(row=0, column=1, padx=10, pady=10, sticky= E)
        
        # Entry for entering video number
        self.input_number = tk.Entry(window, width=3)
        self.input_number.grid(row=0, column=2, padx=10, pady=10, sticky= W)

        # label for entering new rating
        rating_lbl =tk.Label(window, text='New rating')
        rating_lbl.grid(row=0, column=3, padx=10, pady=10, sticky= E)

        # Entry for entering new rating
        self.input_rating = tk.Entry(window, width=3)
        self.input_rating.grid(row=0, column=4, padx=10, pady=10,sticky= W)

        # ScrolledText area to display the list of videos
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3,  padx=10, pady=10)

        # Text area to display selected video details
        self.video_txt = tk.Text(window, width=24, height=5, wrap="none")
        self.video_txt.grid(row=1, column=3, columnspan= 3, sticky="NW", padx=10, pady=10)

        # Label to display status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4,  padx=10, pady=10)

        # display the list of videos in ScrolledText
        lib.show_list_videos(self)

    # Method to handle the click event of the "Update Video" button
    def update_video(self):
        try:
            key = self.input_number.get()           # Get the video number entered by the user
            name = lib.get_name(key)                # Get the name of the video using the key
            rating = int(self.input_rating.get())   # Get the new rating entered by the user
            if rating >= 0:
                if name is not None :                   # If video found
                    lib.set_rating(key, rating)         # Update the rating of the video
                    # Format text
                    text = f"Name: {lib.get_name(key)} \nNew rating: {lib.get_rating(key)} \nPlays: {lib.get_play_count(key)}"
                    # Display updated video details in the text area
                    lib.set_text(self.video_txt, text )
                    lib.show_list_videos(self)                         # Refresh the video list
                else:                                   # If video not found
                    # Show warning message
                    messagebox.showwarning('Warnig', f"Video {key} not found")
                # Update status label
                self.status_lbl.configure(text="Update Video button was clicked!")
            else:
                messagebox.showerror('Error', "Ratting must be an positive numbers")        # Show error message
        except ValueError :                     # If there's a value error
            messagebox.showerror('Error', "Ratting must be an integer")        # Show error message

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    Update_video(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc