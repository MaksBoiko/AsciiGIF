from datetime import datetime
from exception_handler import ExceptionHandler

picture = "**$*\n" \
          "*$**\n" \
          "$***\n" \
          "\n" \
          "****\n" \
          "*fha\n"\
          "\n"


class CreateAsciiGIF:
    def __init__(self, picture):
        self.picture = picture
        self.extension = ".agif"
        self.name = "AsciiGIF"
        self.arr_picture = []
        self.width = 0
        self.height = 0
        self.size = 0
        self.create_date = str(datetime.now())[:-7]
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
        eq_el = row_arr[0]
        print(row_arr)
        for el in row_arr:
            if eq_el != el:
                ExceptionHandler('file_row_error_exception').raise_exception()

        self.width //= self.height
        # create picture array
        row_index = 0
        frame = 0
        for index, value in enumerate(picture):
            if index == 0:
                self.arr_picture.append([])
                self.arr_picture[frame].append([])
            if value == "\n":
                if index != pic_size:
                    if picture[index + 1] == "\n":
                        frame += 1
                        row_index = 0
                        self.arr_picture.append([])
                        continue
                row_index += 1
                self.arr_picture[frame].append([])
            else:
                self.arr_picture[frame][row_index].append(value)
        del self.arr_picture[frame][row_index]
        del self.arr_picture[frame][0]
        print(self.width, self.height, self.size, self.arr_picture, self.create_date)


cag = CreateAsciiGIF(picture)


