import tkinter as tk
import datetime
import winsound

def set_alarm():
    alarm_time = entry.get()
    alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
    while True:
        current_time = datetime.datetime.now()
        current_hour = current_time.hour
        current_minute = current_time.minute
        if current_hour == alarm_hour and current_minute == alarm_minute:
            break

root = tk.Tk()
root.title("Alarm Clock")

label = tk.Label(root, text="Set the alarm time (HH:MM):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Set Alarm", command=set_alarm)
button.pack()

root.mainloop()