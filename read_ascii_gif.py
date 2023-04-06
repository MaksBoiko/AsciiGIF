import os
import time
from datetime import datetime
from exception_handler import ExceptionHandler
import sys


class ReadAsciiGIF:
    def __init__(self, path):
        self.file = ""
        try:
            with open(path, "r") as f:
                self.file = f.read()
        except FileNotFoundError:
            print('File in path "{}" no found!'.format(path))
            sys.exit(1)

    def get_value_from_file(self, start_index):
        part_of_file = self.file[start_index:]
        end_index = part_of_file.find(";")
        value = part_of_file[:end_index]
        return value

    def print_agif(self):
        # get fps from file
        fps_start_index = self.file.find("FPS:")+len("FPS:")+1
        fps = int(self.get_value_from_file(fps_start_index))
        # get frames from file
        start_index = self.file.find("GIF_FRAMES:")+len("GIF_FRAMES:")+1
        part_of_file = self.file[start_index:]
        end_index = part_of_file.find(";")
        picture = part_of_file[:end_index]+";"
        # append each frame to array
        picture_arr = []
        start_with = 0
        for i, el in enumerate(picture):
            if el == "\n" and picture[i+1] == "\n":
                picture_arr.append(picture[start_with:i])
                start_with = i+2
        # print each frame
        while True:
            for frame in picture_arr:
                print(frame, end='')
                time.sleep(1/fps)
                os.system("cls")

    def print_meta_data(self):
        full_name_start_index = self.file.find("FULL_NAME: ")+len("FULL_NAME: ")+1
        name_start_index = self.file.find("NAME: ")+len("NAME: ")+1
        extension_start_index = self.file.find("EXTENSION: ")+len("EXTENSION: ")+1
        frame_width_start_index = self.file.find("FRAME_WIDTH: ")+len("FRAME_WIDTH: ")+1
        frame_height_start_index = self.file.find("FRAME_HEIGHT: ") + len("FRAME_HEIGHT: ")+1
        full_size_start_index = self.file.find("FULL_SIZE: ") + len("FULL_SIZE: ")+1
        fps_start_index = self.file.find("FPS: ") + len("FPS: ")+1
        create_date_start_index = self.file.find("CREATE_DATE: ") + len("CREATE_DATE: ")+1
        edit_date_start_index = self.file.find("EDIT_DATE: ") + len("EDIT_DATE: ")+1
        open_date_start_index = self.file.find("OPEN_DATE: ") + len("OPEN_DATE: ")+1
        frame_count_start_index = self.file.find("FRAME_COUNT: ") + len("FRAME_COUNT: ")+1
        


rag = ReadAsciiGIF("AsciiGIF.agif")
rag.print_agif()