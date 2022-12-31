import tkinter as tk
import main
from enum import Enum

class PauseButton:
    class State(Enum):
        GOING = 1
        PAUSED = 2
    def __init__(self, gui) -> None:
        self.gui = gui
        self.pauseButton = tk.Button(self.gui.window, text="Pause!", command = self.pauseButtonCommand)
        self.pauseButton.pack()
        self.state = PauseButton.State.PAUSED
    def pauseButtonCommand(self):
        if self.state == PauseButton.State.GOING:
            self.gui.log(self.pauseId)
            self.canvas.after_cancel(self.pauseId)
            self.pauseButton.config(text="Run!")
            self.state = PauseButton.State.PAUSED
        elif self.state == PauseButton.State.PAUSED:
            self.pauseButton.config(text="Pause!")
            self.gui.setPauseId(self.gui.canvas.after(1000, main.update_solar_system(self.gui.solarSystem, self.gui.engine, self.gui)))
            self.state = PauseButton.State.GOING
        else:
            print("EROR PAUSING/RUNNING")




class GUI:
    def __init__(self, solarSystem, engine) -> None:
        self.solarSystem = solarSystem
        self.engine = engine
        self.window = tk.Tk()
        self.window.title("Solar System Simulation")
        # self.window.attributes("-fullscreen", True)
        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.pack()
        self.createPauseButton()
        self.createDateLabel()
        # self.set_bg()

    def createPauseButton(self):
        self.pauseButton = PauseButton(self)

    def set_bg(self):
        # Load the background image
        bg_image = tk.PhotoImage(file = "images\star_bg.png")
        # Create the image on the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

    def log(self, args):
        print("Log: ", args)

    def createDateLabel(self):
        self.dateLabel = tk.Label(self.window, text=" Hello there. Date here ")
        self.dateLabel.pack()
        self.number_of_days = 1

    def updateDateLabel(self):
        date = self.solarSystem.getDate()
        self.dateLabel.config(text=date)

    def setPauseId(self, pasueId):
        self.pauseButton.pauseId = pasueId