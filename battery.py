import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent <= 30 and plugged!=True:
    from pynotifier import Notification

    Notification(
        title="Battery Low",
        description=str(percent) + "% Battery remain!!",
        duration=5,  # Duration in seconds
        
    ).send()
