from apollosat.gui import main as gui
import apollosat.helpers as h
import apollosat.constants as c

def main():
    #h.gradient_text(c.ASCII_LOGO)
    #h.permanent_file(c.PERMANENT_DATA)
    h.wipe_file(c.MAIN_DATA)
    gui()

if __name__ == "__main__":
    main()