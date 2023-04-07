from datetime import datetime
from exception_handler import ExceptionHandler
from hashlib import sha256
import sys
import os

# pyinstaller --noconsole --onefile --icon=icon.png sys_process.py
picture = " # # \n" \
          "  #  \n" \
          " # # \n" \
          "\n" \
          "  #  \n" \
          " ### \n" \
          "  #  \n" \
          "\n" \
          "#   #\n" \
          "  #  \n" \
          "#   #\n" \
          "\n"


class CreateAsciiGIF:
    """create GIF from ASCII symbols, from text which was given user"""
    def __init__(self):

        self.picture = ""
        self.extension = ".agif"
        self.name = "AsciiGIF"
        self.fps = 10
        self.full_name = self.name + self.extension
        self.dir = str(os.getcwd() + "\\" + self.full_name)
        self.arr_picture = []
        self.frame_count = 0
        self.width = 0
        self.file = ""
        self.height = 0
        self.size = 0
        self.creation_date = str(datetime.now())[:-7]
        self.edit_date = str(datetime.now())[:-7]
        self.opening_date = str(datetime.now())[:-7]

        try:
            with open(path, "r") as f:
                self.picture = f.read()
        except FileNotFoundError:
            print('File in path "{}" no found!'.format(self.dir))
            sys.exit(1)

        row_size = 0
        row_arr = []
        pic_size = len(picture)-1
        # calculate width, height, size file(bytes) and array with length of each row
        for index in range(len(picture)):
            if picture[index] == "\n":
                if index != pic_size:
                    if picture[index + 1] == "\n":
                        continue
                row_arr.append(row_size)
                self.height += 1
                self.size += 1
                row_size = 0

            else:
                row_size += 1
                self.width += 1
                self.size += 1

        # check if widths(rows) of frames is equal
        eq_el = row_arr[0]
        for el in row_arr:
            if eq_el != el:
                ExceptionHandler('row_exception').raise_exception()

        self.width //= self.height
        # create picture array
        row_index = 0
        row_count_arr = []
        row_count = 0
        for index, value in enumerate(picture):
            if index == 0:
                self.arr_picture.append([])
                self.arr_picture[self.frame_count].append([])
                row_count += 1
            if value == "\n":
                if index != pic_size and picture[index+1] == "\n":
                    self.frame_count += 1
                    self.arr_picture.append([])
                    row_count_arr.append(row_count)
                    row_count = 0
                    row_index = -1

                else:
                    row_count += 1
                    row_index += 1
                    self.arr_picture[self.frame_count].append([])
            else:
                self.arr_picture[self.frame_count][row_index].append(value)
        del self.arr_picture[self.frame_count][row_index]
        # check if heights of frames if equal
        eq_el = row_count_arr[0]
        for el in row_count_arr:
            if eq_el != el:
                ExceptionHandler('frame_height_exception').raise_exception()

    def make_file(self):
        """ pack given data to readable program format"""
        frame_height = self.height // self.frame_count
        self.file = "\nFULL_NAME: {};\nNAME: {};\nEXTENSION: {};\nGENERAL_WIDTH: {};\nGENERAL_HEIGHT: {};" \
                    "\nFRAME_WIDTH: {};\nFRAME_HEIGHT {};\nPHOTO_SIZE: {}b;\nFPS: {};" \
                    "\nCREATION_DATE: {};\nEDIT_DATE: {};\nOPENING_DATE: {};\nFRAME_COUNT: {};" \
                    "\nGIF_FRAMES:\n{};".format(self.full_name, self.name,
                    self.extension, self.width, self.height, self.width, frame_height, self.size, self.fps, self.creation_date, self.edit_date,
                    self.opening_date, self.frame_count, self.picture)

        full_size = len(self.file)
        full_size += len("\nFULL_SIZE: {}b;\nHASH(SHA256): {};".format(full_size, sha256(str(self.file).encode('utf-8')).hexdigest()))
        self.file += "\nFULL_SIZE: {}b;".format(full_size)
        self.file += "\nHASH(SHA256): {};".format(sha256(str(self.file).encode('utf-8')).hexdigest())

    def export_file(self, path):
        try:
            with open(path+self.full_name, "w") as f:
                f.write(str(self.file))
        except FileNotFoundError:
            print('File in path "{}" no found!'.format(path))
            sys.exit(1)
        print("File in path: {} was successfully created!".format(self.dir))


if __name__ == "__main__":
    path = input("Enter directory to txt file with frames for new .agif file: ")
    cag = CreateAsciiGIF()
    cag.make_file()
    cag.export_file("")
    sys.exit(0)

