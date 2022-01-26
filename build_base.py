import subprocess


class BuilderBase():
    def get_green(self, input):
        return '\x1b[6;30;42m' + input + '\x1b[0m'

    def run(self, cmd):
        print(self.get_green("SHELL:")+" " + cmd)
        proc = subprocess.Popen(cmd, shell=True)
        ## for blocking
        proc.communicate()