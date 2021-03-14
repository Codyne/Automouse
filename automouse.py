import tkinter as tk
import keyboard
import mouse
import threading
import time

def main():
    global m_pos
    m_pos = []
    window = tk.Tk()
    window.title("Automouse")
    window.geometry("310x200")
    gen_window(window)
    
    keyboard.add_hotkey("escape", stop_automation)
    
    window.mainloop()

def gen_window(window):
    tk.Label(window, text="Record/Playback Mouse Actions").grid(row=0,column=0)
    record_but = tk.Button(window, text="Record Input", width=15, command=record_movement).grid(row=1, column=1)
    start_but = tk.Button(window, text="Playback Input", width=15, command=start_automation).grid(row=2, column=1)
    
    tk.Label(window, text="Manual Actions").grid(row=3, column=0)
    delay_input = tk.Label(window, text="Delay").grid(row=4, column=1)
    delay_entry = tk.Entry(window)
    delay_entry.grid(row=5, column=1)
    addclick_but = tk.Button(window, text="Add Click", width=15, command=lambda: add_click(delay_entry)).grid(row=6, column=1)
    tk.Button(window, text="Playback Input", width=15, command=start_man_automation).grid(row=7, column=1)
    

def record_movement():
    global events
    events = mouse.record(button="right")
    
def rec_m_thread():
    global events
    events = mouse.record(button="right")

def start_automation():
    global automate_clicks
    global events
    automate_clicks = True
    while automate_clicks:
        mouse.play(events[:-1], speed_factor=1.0)
    
def stop_automation():
    global automate_clicks
    automate_clicks = False
    
def add_click(delay_entry):
    mouse.on_click(lambda: save_pos(delay_entry))
    
def save_pos(delay_entry):
    global m_pos
    if delay_entry.get() and delay_entry.get().strip().isnumeric():
        m_pos.append(int(delay_entry.get()))
    m_pos.append(mouse.get_position())
    mouse.unhook_all()
    
def start_man_automation():
    global automate_clicks
    automate_clicks = True
    pt = threading.Thread(target=man_auto_handler)
    pt.start()
    
    
def man_auto_handler():
    global automate_clicks
    global m_pos
    while automate_clicks:
        for cmd in m_pos:
            if not automate_clicks:
                break
            if type(cmd) == type(0):
                time.sleep(cmd)
            else:
                mouse.move(cmd[0], cmd[1])
                mouse.click(button="left")
        time.sleep(0.5)

if __name__ == "__main__":
    main()