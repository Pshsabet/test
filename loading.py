import curses

def a(win):
    # curses.initscr();


    curses.start_color()
    curses.init_pair(1, 47, curses.COLOR_BLACK)

    win.addstr("Colour selected is " + "Red", curses.color_pair(1))

    win.getch()

curses.wrapper(a)