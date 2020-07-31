import os
import subprocess


class Tornamiko:
    def __init__(self, handler):
        self.logger = handler

    def execute_command(self, command):
        self.logger.set_data(command)
        self.logger.save()

        """execute commands and handle piping"""
        try:
            if "|" in command:
                s_in, s_out = (0, 0)
                s_in = os.dup(0)
                s_out = os.dup(1)
                fdin = os.dup(s_in)

                for cmd in command.split("|"):
                    os.dup2(fdin, 0)
                    os.close(fdin)

                    if cmd == command.split("|")[-1]:
                        fdout = os.dup(s_out)
                    else:
                        fdin, fdout = os.pipe()

                    os.dup2(fdout, 1)
                    os.close(fdout)

                    try:
                        subprocess.run(cmd.strip().split())
                    except Exception:
                        print("tornamiko: command not found: {}".format(cmd.strip()))

                os.dup2(s_in, 0)
                os.dup2(s_out, 1)
                os.close(s_in)
                os.close(s_out)
            else:
                subprocess.run(command.split(" "))
        except Exception:
            print("tornamiko: command not found: {}".format(command))

    @staticmethod
    def tornamiko_cd(path):
        """convert to absolute path and change directory"""
        try:
            os.chdir(os.path.abspath(path))
        except Exception:
            print("cd: no such file or directory: {}".format(path))

    @staticmethod
    def tornamiko_help():
        print("""tornamiko: shell implementation in Python.\nSupports all basic shell commands.""")

    def main(self):
        while True:
            inp = input("(tornamiko) $ ")
            if inp == "exit":
                break
            elif inp[:3] == "cd ":
                self.tornamiko_cd(inp[3:])
            elif inp == "help":
                self.tornamiko_help()
            else:
                self.execute_command(inp)
