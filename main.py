from tkinter import *
import pyshorteners
import pyperclip

root = Tk()
root.title("URL SHORTENER")
root.configure(bg="#e0f7fa")  # Light teal background

url = StringVar()
sortUrl = StringVar()

def urlshort():
    long_url = url.get()
    generatedurl = pyshorteners.Shortener().tinyurl.short(long_url)
    sortUrl.set(generatedurl)

def copy():
    generatedurl = sortUrl.get()
    pyperclip.copy(generatedurl)

# Main Frame
main_frame = Frame(root, bg="#e0f7fa")
main_frame.pack(padx=20, pady=20)

# Title Label
Label(main_frame, text="URL Shortener App", font=("Helvetica", 20, "bold"), bg="#e0f7fa", fg="#00695c").pack(pady=10)

# URL Entry Frame
url_frame = Frame(main_frame, bg="#e0f7fa")
url_frame.pack(pady=10)

Label(url_frame, text="Enter URL:", font=("Helvetica", 14), bg="#e0f7fa", fg="#00695c").pack(side=LEFT, padx=5)
Entry(url_frame, textvariable=url, width=40, font=("Helvetica", 14), bg="#ffffff", fg="#00695c", highlightbackground="#00695c").pack(side=LEFT, padx=5)

# Generate Button
Button(main_frame, text="Generate URL", command=urlshort, font=("Helvetica", 14, "bold"), bg="#ff8a65", fg="#ffffff", activebackground="#ff7043", activeforeground="#ffffff", bd=0, padx=10, pady=5).pack(pady=10)

# Shortened URL Entry Frame
shorturl_frame = Frame(main_frame, bg="#e0f7fa")
shorturl_frame.pack(pady=10)

Label(shorturl_frame, text="Shortened URL:", font=("Helvetica", 14), bg="#e0f7fa", fg="#00695c").pack(side=LEFT, padx=5)
Entry(shorturl_frame, textvariable=sortUrl, width=40, font=("Helvetica", 14), bg="#ffffff", fg="#00695c", highlightbackground="#00695c").pack(side=LEFT, padx=5)

# Copy Button
Button(main_frame, text="Copy URL", command=copy, font=("Helvetica", 14, "bold"), bg="#4db6ac", fg="#ffffff", activebackground="#26a69a", activeforeground="#ffffff", bd=0, padx=10, pady=5).pack(pady=10)

root.mainloop()


