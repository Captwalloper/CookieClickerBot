import keyboard
from easygui import msgbox
import inspect
from typing import Iterable
from typing import Callable

class Keybind:
    def __init__(self, key: str, bind):
        self.key = key
        self.bind = lambda _: bind()
        # Reflection silliness to determine a nice display string for 'bind'
        info = inspect.getframeinfo(inspect.getouterframes(inspect.currentframe())[1][0]).code_context[0].strip()
        arg = info[info.find('(') + 1:-1].split(',')[1]
        self.displayBind = arg

def SetupKeybinds(keybinds :Iterable[Keybind], helpKey: str):
    def ShowKeybinds():
        msgbox("\n".join(map(lambda x: f'Key: {x.key}, Bind: {x.displayBind}', keybinds)))
    keybinds.append(Keybind(helpKey, ShowKeybinds))
    for keybind in keybinds:
        keyboard.on_press_key(keybind.key, keybind.bind)