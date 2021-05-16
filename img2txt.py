
class img2txt:

    def convert(self, image_name):
        try:
            from PIL import Image
        except ImportError:
            import Image
        import pytesseract

        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
        return(pytesseract.image_to_string(Image.open(image_name)))


import socket
import threading
from course import Course
from note import Note
from datetime import datetime

class ClientML:

    def __init__(self, name, address, course, note):
        self.username = name
        self.note = note
        self.course = course

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((address, course.course_port))
        iThread = threading.Thread(target = self.sendMsg, args=(sock, ))
        iThread.daemon = True
        iThread.start()
        print("You are now connected as one of the Notetakers in this classroom.")

        while True:
            data = sock.recv(1024)
            if not data:
                break
            elif data[0:4] == b'[ML]':
                print('testML')
                # Test function
                # a = img2txt()
                # print(a.convert("test.png"))
            else:
                self.note.body = self.note.body + data.decode('UTF-8') + "\n"
                print("[note] " + str(data, "utf-8"))

    

class P2P:
    peers = ['127.0.0.1']
