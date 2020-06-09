import pifacedigitalio as pfio


def activate_listeners(listeners):
    for listener in listeners:
        listener.activate()
    print('Listeners active.')


def deactivate_listeners(listeners):
    for listener in listeners:
        listener.deactivate()
    print('Listeners deactivated.')


if __name__ == '__main__':
    NUM_INPUTS = 4

    board1 = pfio.PiFaceDigital(hardware_addr=0)
    # board2 = pfio.PiFaceDigital(hardware_addr=3)

    listeners = []
    for i in range(NUM_INPUTS):
        listener = pfio.InputEventListener(chip=board1)
        listeners.append(listener)

    for i in range(NUM_INPUTS):
        listeners[i].register(i, pfio.IODIR_ON, print)

    activate_listeners(listeners)

    msg = input('Press any key to stop.\n')

    deactivate_listeners(listeners)
