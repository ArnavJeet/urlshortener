import tkinter as tk
from tkinter import messagebox
import pyshorteners

# Function to shorten the URL
def shorten_url():
    url = url_entry.get()  # Get URL from the input field
    if url:
        try:
            # Create a Shortener object
            s = pyshorteners.Shortener()
            # Shorten the URL
            shortened_url = s.tinyurl.short(url)
            result_text.delete(1.0, tk.END)  # Clear previous result
            result_text.insert(tk.END, shortened_url)  # Insert new shortened URL
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Input Error", "Please enter a URL")

# Setting up the Tkinter window
root = tk.Tk()
root.title("URL Shortener")

# Configure window size and background color
root.geometry("500x350")  # Increased width to accommodate donation message
root.config(bg="light sky blue")

# Create the input field for URL
url_label = tk.Label(root, text="Enter URL:", fg="black", bg="light sky blue", font=("Times New Roman", 12, "italic"))
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=40, font=("Times New Roman", 12, "italic"), bg="light green", fg="black")
url_entry.pack(pady=10)

# Create a button to shorten the URL
shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url, font=("Times New Roman", 12, "italic"), bg="light green", fg="black")
shorten_button.pack(pady=10)

# Create a Text widget to display the shortened URL
result_label = tk.Label(root, text="Shortened URL: ", fg="black", bg="light sky blue", font=("Times New Roman", 12, "italic"))
result_label.pack(pady=10)

# Create a Text widget for displaying the shortened URL (selectable and copyable)
result_text = tk.Text(root, height=2, width=40, font=("Times New Roman", 12, "italic"), bg="light green", fg="black")
result_text.pack(pady=10)
result_text.config(state=tk.DISABLED)  # Initially disable editing

# Add "Programmed By" text at the bottom
programmed_by_label = tk.Label(root, text="Programmed By Arnavjeet Sarmah", fg="black", bg="light sky blue", font=("Times New Roman", 10, "italic"))
programmed_by_label.pack(side=tk.BOTTOM, pady=10)

# Donation Message at left corner
donation_message = tk.Label(root, text="Donate to support: 6001469537@fam", fg="black", bg="light sky blue", font=("Times New Roman", 10, "italic"))
donation_message.place(x=10, y=10)  # Positioning at top left corner

# Run the Tkinter event loop
root.mainloop()







