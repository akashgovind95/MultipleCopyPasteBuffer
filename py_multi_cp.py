from pynput import keyboard
from pynput.keyboard import Key, Controller
import win32clipboard
from cp_comb import cp_comb
from py_cp import py_copy_paste


class pyMultiCP:
    def __init__(self):
        self.keyboard_obj = Controller()
        self.cp_comb = cp_comb()
        self.py_cp = py_copy_paste(self.keyboard_obj)
        self.current = []

    def on_press(self, key):
        if key not in self.current:
            self.current.append(key)

        if len(self.current) == 3:
            if len([pattern for pattern in self.cp_comb.get_copy_combinations() if
                    str(self.current[0]) == str(pattern[0]) and (str(self.current[2]) in str(pattern[2])) and str(
                        self.current[1]) in str(pattern[1])]) != 0:

                win32clipboard.OpenClipboard()

                if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
                    win32clipboard.CloseClipboard()
                    self.py_cp.copy_text(self.current)
                """
                elif win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_DIB):
                    win32clipboard.CloseClipboard()
                    self.py_cp.copy_image(self.current)
                elif win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_HDROP):
                    win32clipboard.CloseClipboard()
                    self.py_cp.copy_file(self.current)
                """

        elif len(self.current) == 2:
            if len([pattern for pattern in self.cp_comb.get_paste_combinations() if
                    str(self.current[0]) == pattern[0] and str(self.current[1]) in pattern[1]]) != 0:
                index = [self.py_cp.get_index_in_key_type_buffer(string) for string in self.py_cp.get_key_type_buffer() if
                         str(self.current[1]) in string][0]
                if self.py_cp.get_object_type_buffer_at_index(index) == "Text":
                    self.py_cp.paste_text(self.current)
                """
                elif self.py_cp.get_object_type_buffer_at_index(index) == "Image":
                    self.py_cp.paste_image(self.current)
                elif self.py_cp.get_object_type_buffer_at_index(index) == "File":
                    self.py_cp.paste_file(self.current)
                """

    def on_release(self, key):
        try:
            self.current.remove(key)
        except:
            pass

    def cp_keyboard_listener(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

