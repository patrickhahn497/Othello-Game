import tkinter

class RC_count:
    """counts the number of (R)ows or (C)olumns wanted"""
    def __init__(self):
        self._count = 4

    def add(self) -> int:
        if self._count < 16:
            self._count += 2
        return self._count

    def subtract(self) -> int:
        if self._count>4:
            self._count -= 2
        return self._count


#def get_row_col():
_BACKGROUND_COLOR = '#FFFFFF'


class ScribbleApplication:
    def __init__(self):
        '''
        Initializes a new Scribble application by creating a window and
        placing a Canvas widget inside of it.  However, the application
        does not execute until its start() method is called.
        '''

        self._root_window = tkinter.Tk()

        self._scribble_canvas = tkinter.Canvas(
            master = self._root_window, width = 500, height = 400,
            background = _BACKGROUND_COLOR)
        

    def start(self) -> None:
        '''
        Starts the Scribble application.  Note that this method will not
        return until the Scribble application's window is closed.
        '''
        self._root_window.mainloop()



_light_sky_blue = "#87cefa"

class OthelloGUI:
    def __init__(self):
        """creates a window in which the input_info will be entered
        by pressing buttons"""

#creating canvas
        self._root_window = tkinter.Tk()
        self._canvas = tkinter.Canvas(master = self._root_window,
                                            width = 500, height = 700,
                                            background = _light_sky_blue)
        self._canvas.grid(  
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)#paints the canvas
        
        self._root_window.rowconfigure(0, weight = 1) # carries out the sticky
        self._root_window.columnconfigure(0, weight = 1)

        self._canvas.create_line(100, 100, 100, 200, fill='black')
        self._canvas.create_line(100, 100, 200, 100, fill='black')

        self._title = tkinter.Label(master = self._root_window, text = 'WELCOME TO OTHELLO (FULL)', font = ('Arial', 20))
        self._title.grid(row = 0, column = 0,  sticky = tkinter.N)

#input info tuple
        self._maxrow = RC_count()

        self._maxcol = RC_count()
        

#buttons
        self._button_window = tkinter.Tk()

    #Row 
        tkinter.Label(master =  self._button_window, text = 'Row Number', font = ('Arial', 25)).grid(row = 0, column = 0, columnspan = 3,  padx = 15, pady = 10)
        
        #subtract
        self._rowsubtractbutton = tkinter.Button(
        master = self._button_window, text = "-",
        font = ('Helvetica', 15), command = self._on_rowsub_pressed)
        self._rowsubtractbutton.grid(row = 1, column = 0)


        #add
        self._rowaddbutton = tkinter.Button(
        master = self._button_window, text = "+",
        font = ('Helvetica', 15))
        self._rowaddbutton.grid(row = 1, column = 2)
        

    #Column
        tkinter.Label(master =  self._button_window, text = 'Column Number', font = ('Arial', 25)).grid(row = 0, column = 3, columnspan = 3,  padx = 15, pady = 10)
        
        #subtract
        self._colsubtractbutton = tkinter.Button(
        master = self._button_window, text = "-",
        font = ('Helvetica', 15), command = self._on_colsub_pressed)
        
        self._colsubtractbutton.grid(row = 1, column = 3)

    

        #add
        self._coladdbutton = tkinter.Button(
        master = self._button_window, text = "+",
        font = ('Helvetica', 15), command = self._on_coladd_pressed)
        
        self._coladdbutton.grid(row = 1, column = 5)



        
    #First Turn
        tkinter.Label(master =  self._button_window, text = 'First Turn', font = ('Arial', 25)).grid(row = 2, column = 0, columnspan = 3,  padx = 15, pady = 15)
        

        #Black first
        self._blackfirstbutton = tkinter.Button(
        master = self._button_window, text = "(B)lack",
        font = ('Helvetica', 15))

        
        self._blackfirstbutton.grid(row = 3, column = 0)

        def _on_bfirst_pressed()->None:
            pass

        #button.config( background = color)

        #White first
        self._whitefirstbutton = tkinter.Button(
        master = self._button_window, text = "(W)hite",
        font = ('Helvetica', 15))

        
        self._whitefirstbutton.grid(row = 3, column = 2)

        def _on_wfirst_pressed()->None:
            pass

    #Top-Left Color
        tkinter.Label(master =  self._button_window, text = 'Top-Left Color', font = ('Arial', 25)).grid(row = 2, column = 3, columnspan = 3,  padx = 15, pady = 15)
        

        #Black topleft
        self._blacktopleftbutton = tkinter.Button(
        master = self._button_window, text = "(B)lack",
        font = ('Helvetica', 15))

        
        self._blacktopleftbutton.grid(row = 3, column = 3)

        def _on_btopleft_pressed()->None:
            pass

        #White first
        self._whitetopleftbutton = tkinter.Button(
        master = self._button_window, text = "(W)hite",
        font = ('Helvetica', 15))

        
        self._whitetopleftbutton.grid(row = 3, column = 5)

        def _on_wtopleft_pressed()->None:
            pass


    #Greater or Less
        tkinter.Label(master =  self._button_window, text = 'Win Condition: > or < tiles', font = ('Arial', 25)).grid(row = 4, column = 0, columnspan = 3,  padx = 15, pady = 15)
        

        #Greater
        self._greaterbutton = tkinter.Button(
        master = self._button_window, text = "(>) Greater Tiles Win",
        font = ('Helvetica', 15))

        
        self._greaterbutton.grid(row = 5, column = 0, padx = 10, pady = 10)

        def _on_greater_pressed()->None:
            #highlight the text of the button
            #put into a temporary tuple
            pass

        #Lesser
        self._lessbutton = tkinter.Button(
        master = self._button_window, text = "(<) Fewer Tiles Win",
        font = ('Helvetica', 15))

        
        self._lessbutton.grid(row = 5, column = 2, padx = 10, pady = 10)

        def _on_lesser_pressed()->None:
            pass

    #ACCEPT
        self._submitbutton = tkinter.Button(
        master = self._button_window, text = "ACCEPT",
        font = ('Helvetica', 15))

        
        self._submitbutton.grid(row = 5, column = 4, padx = 10, pady = 10)
        


        self._button_window.mainloop()
        


#defintions

    #row
    def _on_rowadd_pressed(self)->None:  
        self._maxrow.add()
        print(self._maxrow._count)


    def _on_rowsub_pressed(self)->None:
        self._maxrow.subtract()
        
    
    #col
    def _on_colsub_pressed(self)->None:
        self._maxcol.subtract()
        
    def _on_coladd_pressed(self)->None:
        self._maxcol.add()


    def _on_canvas_clicked(self, event: tkinter.Event) -> None:

        # * event.x, which specifies the x-coordinate where the click
        #   occurred
        # * event.y, which specifies the y-coordinate where the click
        #   occurred

        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        click_point = point.from_pixel(
            event.x, event.y, width, height)
    
    def start(self) -> None:

        self._root_window.mainloop()





if __name__ == '__main__':
    app = OthelloGUI()
    app.start()

