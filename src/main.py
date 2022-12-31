import tkinter as tk
import SolarSystem
import Engine
import GUI

# Update the solar system and canvas
def update_solar_system(solar_system, engine, gui):
    solar_system.addDay(gui.number_of_days)
    gui.updateDateLabel()
    solar_system.updatePosition()
    engine.updatePosition()
    gui.setPauseId(gui.canvas.after(1000, update_solar_system(solar_system, engine, gui)))

if __name__ == '__main__':
    # Create a SolarSystem object
    solar_system = SolarSystem.SolarSystem(2000, 1, 1)
    solar_system.createSunSolarSystem()

    # Create an Engine object
    engine = Engine.Engine(solar_system)

    # Create GUI
    gui = GUI.GUI(solar_system, engine)
    # Start updating the solar system
    update_solar_system(solar_system, engine, gui)
    # Run the main loop
    gui.window.mainloop()
