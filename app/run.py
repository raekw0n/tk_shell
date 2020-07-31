from logger import Logger
from tornamiko import Tornamiko

if '__main__' == __name__:
    logger = Logger(path="/home/chris/PycharmProjects/raspi-shell/data/history")
    tornamiko = Tornamiko(handler=logger)
    tornamiko.main()
