import pifacedigitalio as pfio
import pygame
from pygame.locals import QUIT
import sys


# !REFACTORING THIS!
# _boards_ = init_boards()
# _board_ = pfio.PiFaceDigital()  # a single board (hardware_addr=0)

# def toggle_relay(relay=0, board=0):
#     _boards_[board].relays[relay].toggle()


# def get_relay_status(relay=0, board=0):
#     return _boards_[board].relays[relay].value


# def get_input_status(board=0):
#     values = [_boards_[board].input_pins[x].value for x in range(8)]
#     return values


# def get_output_status(board=0):
#     values = [_boards_[board].output_pins[x].value for x in range(8)]
#     return values
# !-----!


class Controller:
    """
    TODO: add docstring
    """

    def __init__(self, screen_size):
        # TODO: initialise boards
        print("Initialising...")
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.__boards__ = init_boards()

    def start(self):
        # TODO: Start the ontroller loop?
        print("Controller started.")

    def loop(self):
        # TODO: check for user input and then update
        # Should use a fixed time-step between each update
        # Right now it updates with no delay
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit()
            self.check_user_input()
            self.update()

    def check_user_input(self):
        """
        Check user input before every update.
        """

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_1]:
            pass

    def update(self):
        """
        TODO: check/update the boards statuses (pins, etc.)
        """

        pygame.display.update()

    def halt(self):
        """
        Stop the controller, but don't exit.

        Currently not a priority

        Raises
        ----------
        NotImplementedError
            Will raise an error if the method is called.
        """

        raise NotImplementedError

    def resume(self):
        """
        Resume the controller loop.

        Currently not a priority

        Raises
        ----------
        NotImplementedError
            Will raise an error if the method is called.
        """

        raise NotImplementedError

    def exit(self, exit_code=0):
        """
        Exit the program.

        Parameters
        ----------
        exit_code : int
            value to send to sys.exit()
            (default is 0 - normal program termination)
        """

        print("Exiting...")
        sys.exit(exit_code)

    def init_boards(self, num=1):
        """
        Initialise the PiFace boards

        Parameters
        ----------
        num : int, optional
            The number of boards to be initialised (default is 1)

        Returns
        ----------
        list
            a list of PiFaceDigital objects
        """

        boards = [pfio.PiFaceDigital()]  # the first board
        if num > 1:
            try:
                # initialize a second board
                boards.append(pfio.PiFaceDigital(hardware_addr=3))
            except pfio.NoPiFaceDigitalDetectedError:
                print("No second board detected - will only use first board")
        return boards

    def get_input_pins_values(self, board_index=0):
        """
        Returns a list of the input pins values.

        Returns a list of the input pins values for the specified board.

        Parameters
        ----------
        board_index : int
            used to access the board in the list
            (default is 0 - the first board)

        Returns
        ----------
        values:
            a list of values representing the status of each pin
        """

        values = [self.__boards__[board_index].input_pins[x].value
                  for x in range(8)]  # a board only has 8 input pins
        return values

    def get_output_pins_values(self, board_index=0):
        """
        Returns a list of the input pins values.

        Parameters
        ----------
        board_index: int
            used to access the board in the list
            (default is 0 - the first board)

        Returns
        ----------
        values:
            a list of values representing the status of each pin
        """

        values = [self.__boards__[board_index].output_pins[x].value
                  for x in range(8)]  # a board only has 8 output pins
        return values


if __name__ == "__main__":
    msg = "Simple controller for PiFaceDigital board(s)."
    print(msg)

    controller_ = Controller((300, 300))
    controller_.start()
    controller_.loop()
