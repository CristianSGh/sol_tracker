import pifacedigitalio as pfio


def init_boards(num=1):
    boards = [pfio.PiFaceDigital()]  # the first board
    if num > 1:
        try:
            # initialize a second board
            boards.append(pfio.PiFaceDigital(hardware_addr=3))
        except pfio.NoPiFaceDigitalDetectedError:
            print("No 2nd board detected.")
    return boards


_boards_ = init_boards()
# _board_ = pfio.PiFaceDigital()  # a single board (hardware_addr=0)


def toggle_relay(relay=0, board=0):
    _boards_[board].relays[relay].toggle()


if __name__ == "__main__":
    msg = "Simple controller for PiFaceDigital board(s)."
    print(msg)
