from library_item import LibraryItem
import tkinter as tk

library = {}
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5)
library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2)
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1)
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3)


def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return
# Method to display the list of all videos
def show_list_videos(self):
    video_list = list_all()
    set_text(self.list_txt, video_list)

def set_text(text_area, content):           # then the new content is inserted 
    text_area.delete("1.0", tk.END)         # first the existing content is deleted     
    text_area.insert(1.0, content)          # then the new content is inserted 