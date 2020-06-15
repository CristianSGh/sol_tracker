import pifacedigitalio as pfio


_boards_ = init_boards()
# _board_ = pfio.PiFaceDigital()  # a single board (hardware_addr=0)


def init_boards(num=1):
    boards = [pfio.PiFaceDigital()]  # the first board
    if num > 1:
        try:
            # initialize a second board
            boards.append(pfio.PiFaceDigital(hardware_addr=3))
        except pfio.NoPiFaceDigitalDetectedError:
            print("No 2nd board detected.")
    return boards


def toggle_relay(relay=0, board=0):
    _boards_[board].relays[relay].toggle()


def get_relay_status(relay=0, board=0):
    return _boards_[board].relays[relay].value


def get_input_status(board=0):
    values = [_boards_[board].input_pins[x].value for x in range(8)]
    return values


def get_output_status(board=0):
    values = [_boards_[board].output_pins[x].value for x in range(8)]
    return values


if __name__ == "__main__":
    msg = "Simple controller for PiFaceDigital board(s)."
    print(msg)
