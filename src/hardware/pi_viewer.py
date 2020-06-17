import cmd
import sys
import pifacedigitalio as pfio  # placeholder until the controller is operational


class Viewer(cmd.Cmd):
    """
    Command line interface to interact with a RPi/PiFaceDigital
    """

    intro = "\n* PiFace Viewer *\n"
    prompt = "=>> "

    def start_board(self):
        self.board = pfio.PiFaceDigital()
        print("Board ready.\n")

    def do_read_pins(self, p_type=0):
        """
        Prints the pin values to the console.

        Arguments
        p_type: the type of pin to read -> 0=BOTH | 1=IN | 2=OUT (default is 0)
        """

        labels = {0: "OFF", 1: "ON"}

        if p_type == 0:
            print("IN:")
            for i in range(8):
                val = self.board.input_pins[i].value
                print(f"{i} [{labels[val]}]")
            print("\nOUT:")
            for i in range(8):
                val = self.board.output_pins[i].value
                print(f"{i} [{labels[val]}]")

        elif p_type == 1:
            print("IN:")
            for i in range(8):
                val = self.board.input_pins[i].value
                print(f"{i} [{labels[val]}]")

        elif p_type == 2:
            print("OUT:")
            for i in range(8):
                val = self.board.output_pins[i].value
                print(f"{i} [{labels[val]}]")

        else:
            print("???")

        print("\n")

    def do_set_port(self, value=None, port="input"):
        """
        Set the value of the I/O ports.

        Arguments
        value: hex value to be read (eg. [0x]FF) - has to be in range 0..FF
        port: the port type - input | output
        """

        ports = {"input": self.board.input_port, "output": self.board.output_port}
        if value:
            if type(value) == str:
                int_val = int(value, 16)
                if int_val > 255 and int_val < 0:
                    print("Invalid setting")
                    return
                else:
                    ports[port].value = int_val
            else:
                print("???")
        else:
            print("No value...")
            return

    def do_exit(self):
        print("Bye...")
        sys.exit()


if __name__ == "__main__":
    viewer = Viewer()
    viewer.cmdloop()
