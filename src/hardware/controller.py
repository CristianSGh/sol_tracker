# import pifacedigitalio as pfio


# !REFACTORING THIS!
# _boards_ = init_boards()
# _board_ = pfio.PiFaceDigital()  # a single board (hardware_addr=0)


# def init_boards(num=1):
#     boards = [pfio.PiFaceDigital()]  # the first board
#     if num > 1:
#         try:
#             # initialize a second board
#             boards.append(pfio.PiFaceDigital(hardware_addr=3))
#         except pfio.NoPiFaceDigitalDetectedError:
#             print("No 2nd board detected.")
#     return boards


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

    def __init__(self):
        # TODO: initialise boards
        print("Initialising...")

    def start(self):
        # TODO: Start the ontroller loop?
        print("Controller started.")

    def loop(self):
        # TODO: check for user input and then update
        # Should use a fixed time-step between each update
        # Right now it updates with no delay
        pass

    def check_user_input(self):
        """
        Check user input before every update.
        """

        pass

    def update(self):
        """
        TODO: check/update the boards statuses (pins, etc.)
        """

        pass

    def halt(self):
        """
        Stop the controller, but don't exit.
        """

        pass

    def resume(self):
        """
        Resume the controller loop.
        """

        pass

    def exit(self):
        """
        Exit the program.
        """

        pass


if __name__ == "__main__":
    msg = "Simple controller for PiFaceDigital board(s)."
    print(msg)
