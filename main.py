from apollosat.gui import main as gui
import apollosat.helpers as h
import apollosat.constants as c

def main():
    """Run ApolloSat"""

    #h.gradient_text(c.ASCII_LOGO) # Fancy logo on startup
    #h.permanent_file(c.PERMANENT_DATA) # Write data to a permanent file (so data is not deleted on next run)
    h.wipe_file(c.MAIN_DATA) # Clean data file on each run to keep concise
    gui() # Open GUI

if __name__ == "__main__":
    main()