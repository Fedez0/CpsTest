import os
import guizero as gui
import threading
import time as tn


clicks = 0
time = 0
labelClicks = None
labelTime = None
temp = True
def start_timer():
    global labelTime,temp,clicks
    start_time = tn.time()
    while temp:
        elapsed_time = tn.time() - start_time
        
        labelTime.value = f" {elapsed_time:.2f} "
        if elapsed_time >= 10:
            break
    show_popup()
    clicks = 0
        
def show_popup():
    global clicks
    popup = gui.Window(frame, title="Finished", width=300, height=100)
    message = gui.Text(popup, text=f"Results: {(clicks/10):.2f} CPS", size=20, font="Arial", color="black")
    close_button = gui.PushButton(popup, text="Chiudi", command=popup.destroy)
    popup.show(wait=True)
def buttonClicked():
    global clicks, labelClicks
    if clicks == 0:
        timer = threading.Thread(target=start_timer)
        timer.start()        
    clicks += 1
    labelClicks.value = f"Clicks: {clicks}"
    pass
def setLayout(frame):
    global labelClicks, labelTime
    label = gui.Text(frame, text="CPS Test", size=40, font="Arial", color="black")
    image = gui.Picture(frame, image="cps.png")
    labelClicks = gui.Text(frame, text=f"Clicks: {clicks}", size=20, font="Arial", color="black")
    button = gui.PushButton(frame, text="Click here", command=buttonClicked,width=20, height=5)
    
    labelTime = gui.Text(frame, text=f"Time: {time}", size=20, font="Arial", color="black")
    
    pass
def chiusura():
    global temp
    temp = False
    frame.destroy()
    pass
if __name__ == "__main__":
    try:
        os.system('cls')
    except:
        os.system('clear')
    frame = gui.App(title="My App", width=800, height=600, layout="auto")
    
    
    setLayout(frame)
    frame.when_closed = chiusura
    frame.display()
    