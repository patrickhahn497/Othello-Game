import tkinter

class RC_count:
    """counts the number of (R)ows or (C)olumns wanted"""
    def __init__(self):
        self._count = 0

    def add(self) -> int:
        if self._count < 16:
            self._count += 2
        return self._count

    def subtract(self) -> int:
        if self._count>2:
            self._count -= 2
        return self._count

#def get_row_col():



_deep_sky_blue = "#00bfff"

class OthelloGUI:
    def __init__(self):
        """creates a window in which the input_info will be entered
        by pressing buttons"""
        self._root_window = tkinter.Tk()
        self._input_canvas = tkinter.Canvas(master = self._root_window,
                                            width = 500, height = 1000,
                                            background = _deep_sky_blue)




#def _on_RC_button_press():



OthelloGUI()