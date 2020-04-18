#from PythonMagick import Image
from pynput.keyboard import Key
import win32clipboard
import pyperclip
import sys
import ctypes


class py_copy_paste:

    def __init__(self, keyboard):
        self.keyboard_obj = keyboard
        self.buffer = ['', '', '', '', '', '', '', '', '', '']
        self.object_type_buffer = ['', '', '', '', '', '', '', '', '', '']
        self.key_type_buffer = ['u\'1\'', 'u\'2\'', 'u\'3\'', 'u\'4\'', 'u\'5\'', 'u\'6\'', 'u\'7\'', 'u\'8\'', 'u\'9\'']
        self.gmem_ddeshare = 0x2000

    def get_key_type_buffer(self):
        return self.key_type_buffer

    def get_object_type_buffer(self):
        return self.key_type_buffer

    def get_index_in_key_type_buffer(self, stringtoSearch):
        return self.key_type_buffer.index(stringtoSearch)

    def get_object_type_buffer_at_index(self, index):
        return self.object_type_buffer[index]

    def copy_image(self, current):

        # Doesn't Work
        """
        for val in self.key_type_buffer:
            if str(current[2]) in val:
                buffers = self.key_type_buffer.index(val)
                Image("clipboard:").write("PNG32:" + str(buffers) + ".png")
                self.object_type_buffer[buffers] = "Image"
        """
    def paste_image(self, current):
        # Doesn't Work
        """
        for val in self.key_type_buffer:
            if str(current[1]) in val:
                buffers = self.key_type_buffer.index(val)
                Image(str(buffers) + ".png").write("clipboard:")
                self.keyboard_obj.release(Key.ctrl_l)
                self.keyboard_obj.press(Key.ctrl_r)
                self.keyboard_obj.press('v')
                self.keyboard_obj.release('v')
                self.keyboard_obj.release(Key.ctrl_r)
                self.keyboard_obj.press(Key.ctrl_l)
        """

    def copy_file(self, current):
        # Doesn't Work
        for val in self.key_type_buffer:
            if str(current[2]) in val:
                buffers = self.key_type_buffer.index(val)
                win32clipboard.OpenClipboard()
                rawData = win32clipboard.GetClipboardData(win32clipboard.CF_HDROP)
                self.buffer[buffers] = rawData
                self.object_type_buffer[buffers] = "File"

    def paste_file(self, current):
        # Doesn't Work
        for val in self.key_type_buffer:
            if str(current[1]) in val:
                buffers = self.key_type_buffer.index(val)
                rawData = self.buffer[buffers]
                hcd = ctypes.windll.kernel32.GlobalAlloc(self.gmem_ddeshare, sys.getsizeof(rawData) + 1)
                pchData = ctypes.windll.kernel32.GlobalLock(hcd)
                pchData = hcd
                ctypes.windll.kernel32.GlobalUnlock(hCd)
                win32clipboard.SetClipboardData(win32clipboard.CF_HDROP, pchData)
                self.keyboard_obj.release(Key.ctrl_l)
                self.keyboard_obj.press(Key.ctrl_r)
                self.keyboard_obj.press('v')
                self.keyboard_obj.release('v')
                self.keyboard_obj.release(Key.ctrl_r)
                self.keyboard_obj.press(Key.ctrl_l)
                win32clipboard.CloseClipboard()

    def copy_text(self, current):
        for val in self.key_type_buffer:
            if str(current[2]) in val:
                index = self.key_type_buffer.index(val)
                self.buffer[index] = pyperclip.paste()
                self.object_type_buffer[index] = "Text"
                print("Copy at "+str(index)+": "+self.buffer[index])

    def paste_text(self, current):
        for val in self.key_type_buffer:
            if str(current[1]) in val:
                index = self.key_type_buffer.index(val)
                pyperclip.copy(self.buffer[index])
                self.keyboard_obj.release(Key.ctrl_l)
                self.keyboard_obj.press(Key.ctrl_r)
                self.keyboard_obj.press('v')
                self.keyboard_obj.release('v')
                self.keyboard_obj.release(Key.ctrl_r)
                self.keyboard_obj.press(Key.ctrl_l)
                print("Paste from " + str(index) + ": " + self.buffer[index])
