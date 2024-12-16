from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width: int, height: int, title: str):
        self.__root: Tk = Tk()
        self.__root.title(title)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas: Canvas = Canvas(self.__root, bg="white",
                                     height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.__running: bool = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self) -> None:
        self.__running = False
