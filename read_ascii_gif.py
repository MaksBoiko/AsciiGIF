import os
import time
import msvcrt
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
                if msvcrt.kbhit():
                    i = str(msvcrt.getch())[2]
                    if i == 'p':
                        os.system("pause")
                    if i == 'x':
                        sys.exit(0)
                os.system("cls")

    def print_meta_data(self):
        full_name_start_index = self.file.find("FULL_NAME: ")+len("FULL_NAME: ")
        name_start_index = self.file.find("\nNAME: ")+len("\nNAME: ")
        extension_start_index = self.file.find("EXTENSION: ")+len("EXTENSION: ")
        frame_width_start_index = self.file.find("_WIDTH: ")+len("_WIDTH: ")
        frame_height_start_index = self.file.find("_HEIGHT: ") + len("_HEIGHT: ")
        full_size_start_index = self.file.find("FULL_SIZE: ") + len("FULL_SIZE: ")
        fps_start_index = self.file.find("FPS: ") + len("FPS: ")
        creation_date_start_index = self.file.find("CREATION_DATE: ") + len("CREATION_DATE: ")
        edit_date_start_index = self.file.find("EDIT_DATE: ") + len("EDIT_DATE: ")
        opening_date_start_index = self.file.find("OPENING_DATE: ") + len("OPENING_DATE: ")
        frame_count_start_index = self.file.find("FRAME_COUNT: ") + len("FRAME_COUNT: ")

        print("Full file name: "+self.get_value_from_file(full_name_start_index))
        print("Name of file: " + self.get_value_from_file(name_start_index))
        print("Extension of file: " + self.get_value_from_file(extension_start_index))
        print("Width of frame: " + self.get_value_from_file(frame_width_start_index))
        print("Height of frame: " + self.get_value_from_file(frame_height_start_index))
        print("Size of file: " + self.get_value_from_file(full_size_start_index))
        print("FPS: " + self.get_value_from_file(fps_start_index))
        print("Date of creation: " + self.get_value_from_file(creation_date_start_index))
        print("Date of edition: " + self.get_value_from_file(edit_date_start_index))
        print("Opening date: " + self.get_value_from_file(opening_date_start_index))
        print("Count of frames: " + self.get_value_from_file(frame_count_start_index))


if __name__ == "__main__":
    path = input("Enter directory to .agif file: ")
    rag = ReadAsciiGIF(path)
    rag.print_agif()
