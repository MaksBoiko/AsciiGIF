import sys


class ExceptionHandler:
    def __init__(self, exception):
        self.exception = exception
        self.exceptions = {'row_exception': "Error in size of rows(width of frame is not equal)!",
                           "frame_height_exception": "Error in count of rows(heights of frames is not equal)!"}

    def raise_exception(self):
        if self.exception in self.exceptions:
            print(self.exceptions[self.exception])
            sys.exit(1)
