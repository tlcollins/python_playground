import curses
from random import randint

class ty_cow:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.direction = 4

    def move(self):
        if self.direction == 1:
            self.y -= 1
        if self.direction == 2:
            self.y -= 1
            self.x += 1
        if self.direction == 3:
            self.x += 1
        if self.direction == 4:
            self.y += 1
            self.x += 1
        if self.direction == 5:
            self.y += 1
        if self.direction == 6:
            self.y += 1
            self.x -= 1
        if self.direction == 7:
            self.x -= 1
        if self.direction == 8:
            self.y -= 1
            self.x -= 1

        if self.x < 1:
            self.x += 1
            self.direction = 3
        if self.y < 1:
            self.y += 1
            self.direction = 5
        if self.x > curses.COLS-1:
            self.x -= 1
            self.direction = 7
        if self.y > curses.LINES-1:
            self.y -= 1
            self.direction = 1

            
        self.direction += randint(-1,1)
        if self.direction == 0:
            self.direction = 8
        if self.direction == 9:
            self.direction = 1

        stdscr.addstr(self.y, self.x, 'c')

if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.halfdelay(1)
    stdscr.clear()

    cowlist = []

    for x in range(10):
        cowlist.append(ty_cow())

    ch = stdscr.getch()
        
    while ch != 113:
        stdscr.clear()


        for x in range(len(cowlist)):
            cowlist[x].move()


        stdscr.refresh()
        stdscr.addstr(0,0,"{:d}".format(ch))
        ch = stdscr.getch()

    curses.endwin()
