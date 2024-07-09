from tkinter import *
import requests
background_image = "./download.png"
click_img = "./images.png"

# Setup window
window = Tk()
window.config(padx=50, pady=50)
window.title("Quotes App")

# Setup Canvas
canvas = Canvas(width=300, height=300)
bg_img = PhotoImage(file=background_image)
canvas.create_image(150, 150, image=bg_img)
text = canvas.create_text(150, 150, text="Get the Quote in here!", width=150, anchor='center')
canvas.grid(row=0, column=0)

# Setup click button
click_img = PhotoImage(file=click_img)


#button function
def button_click():
    response = requests.get("https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(text, text=quote)
   
    
click_button = Button(image=click_img, command=button_click)
click_button.grid(row=1, column=0)

# Keep the window open
window.mainloop()
