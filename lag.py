import keyboard
import subprocess

ADAPTER_NAME = "Ethernet"

enabled = True

def toggle_network():
    global enabled

    if enabled:
        subprocess.run(
            f'netsh interface set interface "{ADAPTER_NAME}" admin=disable',
            shell=True
        )
        print(f"{ADAPTER_NAME} disabled")
    else:
        subprocess.run(
            f'netsh interface set interface "{ADAPTER_NAME}" admin=enable',
            shell=True
        )
        print(f"{ADAPTER_NAME} enabled")

    enabled = not enabled

keyboard.add_hotkey("l", toggle_network)

print("L = Toggle Ethernet")
print("ESC = Quit")

keyboard.wait("esc")