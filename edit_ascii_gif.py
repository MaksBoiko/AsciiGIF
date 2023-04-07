import sys


class EditAsciiGIF:
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

    def edit_meta_data(self):
        name_start_index = self.file.find("\nNAME: ") + len("\nNAME: ")
        # fps_start_index = self.file.find("FPS: ") + len("FPS: ")
        choose = input("What do you want to edit(name)?")
        if choose == "name":
            new_name = input("Enter name of file: ")
            old_name = self.get_value_from_file(name_start_index)
            self.file = self.file.replace(old_name, new_name, 2)
            self.file = self.file.replace(new_name, old_name, 1)
            print(self.file)

    def edit_frames(self):
        # get frames from file
        start_index = self.file.find("GIF_FRAMES:") + len("GIF_FRAMES:") + 1
        part_of_file = self.file[start_index:]
        end_index = part_of_file.find(";")
        picture = part_of_file[:end_index] + ";"
        # append each frame to array
        picture_arr = []
        start_with = 0
        for i, el in enumerate(picture):
            if el == "\n" and picture[i + 1] == "\n":
                picture_arr.append(picture[start_with:i])
                start_with = i + 2
        # print each frame
        for frame in picture_arr:
            print(frame)

        print("Copy and paste following text in any text editor. \nThen edit file and paste here."
              "Your paste text will be automatically added to .agif file.")
        print("\nEnter frames here:\n")
        frames = "\n".join(iter(input, ""))
        self.file = self.file.replace(part_of_file[:end_index], frames)



if __name__ == "__main__":
    path = input("Enter directory to .agif file: ")
    eag = EditAsciiGIF(path)
    eag.edit_frames()


