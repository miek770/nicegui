import subprocess
import sys

from nicegui import ui


def hello():
    subprocess.Popen([sys.executable, "hello.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)


ui.button("Hello", on_click=hello)

ui.run(native=True)
