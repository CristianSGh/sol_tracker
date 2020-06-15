import argparse
import controller


def check_pin_status(type_=0, board_index=0):
    """
    Prints the values of the selected pins on the specified board(s)

    Parameters:
        type_(int):The pin type (Both | In | Out).
        board_index(int):The board(s) from which to read the pin values.
    """

    # currently will only check the first board
    board = controller.init_boards()

    if type_ == 0:
        in_status = board.get_input_status()
        out_status = board.get_output_status()
        print("In values:")
        print_pins(in_status)
        print("Out values:")
        print_pins(out_status)
    elif type_ == 1:
        in_status = board.get_input_status()
        print("In values:")
        print_pins(in_status)
    else:
        out_status = board.get_output_status()
        print("Out values:")
        print_pins(out_status)


def print_pins(pins):
    labels = {0: "OFF", 1: "ON"}
    for p in pins:
        print(labels[p])
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check PiFace I/O status.")

    pins_help_msg = "Read pin values: 0 -> Both, 1 -> In, 2 -> Out"
    parser.add_argument("-p", "--pins", help=pins_help_msg, type=int,
                        default=0, choices=[0, 1, 2])

    bds_help_msg = """
                   Select which board to read from
                   0 -> first (default)
                   1 -> second (if connected)
                   2 -> both (if connected)
                   """
    parser.add_argument("-b", "--boards", help=bds_help_msg, type=int,
                        default=0, choices=[0, 1, 2])

    args = parser.parse_args()
    print(args.pins, args.boards)
