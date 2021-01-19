import time
import random
import ctypes
from SMWinservice import SMWinservice

class EthanFitnessService(SMWinservice):
    _svc_name_ = "EthanFitnessService"
    _svc_display_name_ = "Ethan Fitness Service"
    _svc_description_ = "Popup workouts"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while self.isrunning:
            '''
            LOGIC GOES HERE
            '''
            #Check if service is stopped
            if self.isrunning == False: 
                break

if __name__ == '__main__':
    EthanFitnessService.parse_command_line()
