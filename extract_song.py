import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def fetch_lyrics(title, artist):
    url = f"https://www.azlyrics.com/lyrics/{artist}/{title}.html"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        lyrics = soup.find_all("div", attrs={"class": None, "id": None})
        if lyrics:
            return "\n".join([line.text for line in lyrics])
    return None

def search_lyrics():
    title = title_entry.get()
    artist = artist_entry.get()
    if title and artist:
        lyrics = fetch_lyrics(title.lower().replace(" ", ""), artist.lower().replace(" ", ""))
        if lyrics:
            lyrics_text.config(state=tk.NORMAL)
            lyrics_text.delete("1.0", tk.END)
            lyrics_text.insert(tk.END, lyrics)
            lyrics_text.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Lyrics Not Found", "Lyrics not found for the given song.")
    else:
        messagebox.showwarning("Missing Information", "Please enter both the song title and artist.")
def on_enter(event):
    search_button.config(bg="lime green", fg="white")
    search_button.config(width=20, height=2)

def on_leave(event):
    search_button.config(bg="purple", fg="white")
    search_button.config(width=15, height=1)
# Create a tkinter window
window = tk.Tk()
window.title("Lyrics Extractor")

# Create a style object
style = ttk.Style()

# Configure the style for the entry fields with rounded corners
style.configure('RoundedEntry.TEntry', borderwidth=4, relief="ridge", 
                fieldbackground='white', foreground='black', bordercolor='gray', 
                focuscolor='blue', borderradius=50)

# Create a frame to hold the form fields
frame = tk.Frame(window)
frame.pack(pady=20)

# Add a heading inside the form frame with double size font
reg_form = tk.LabelFrame(frame, text="Lyrics Extractor", font=("Helvetica", 20, "bold"), borderwidth=2)
reg_form.grid(row=0, column=0, pady=(20, 5), padx=20, sticky="nsew")

# Create labels and entry fields for title and artist with decreased size and rounded corners
title_label = tk.Label(reg_form, text="Title:", font=("Helvetica", 12))
title_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="e")
title_entry = ttk.Entry(reg_form, style='RoundedEntry.TEntry', font=("Helvetica", 12))
title_entry.grid(row=0, column=1, padx=10, pady=(10, 5))

artist_label = tk.Label(reg_form, text="Artist:", font=("Helvetica", 12))
artist_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
artist_entry = ttk.Entry(reg_form, style='RoundedEntry.TEntry', font=("Helvetica", 12))
artist_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a "Search" button with fully rounded corners and decreased gap between form fields
search_button = tk.Button(frame, text="Search", command=search_lyrics, font=("Helvetica", 16), width=15, relief="raised", bd=2, borderwidth=2, padx=10, pady=5, border=0, highlightthickness=0, bg="purple", fg="white")
search_button.grid(row=1, column=0, pady=(5, 10))

# Binding events for hover effect
search_button.bind("<Enter>", on_enter)
search_button.bind("<Leave>", on_leave)

# Create a text widget to display lyrics
lyrics_text = tk.Text(window, font=("Helvetica", 12), wrap=tk.WORD, height=10, width=50)
lyrics_text.pack(pady=20)

# Center the window
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"+{x}+{y}")

# Start the Tkinter event loop
window.mainloop()