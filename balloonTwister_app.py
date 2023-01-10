from scheduler import Scheduler

class BalloonTwisterApp:
    def __init__(self) -> None:
        self.__book = Scheduler()
    
    def show_menu(self):
        print('\nBalloon Twister booking System')
        print('\n-----Command Menu-----')
        print('1. Schedule a balloon twister')
        print('2. Cancel booking')
        print('3. Check the Status of balloon Twister or holiday')
        print('4. Quit')
        print('5. Signup a new balloon twister')
        print('6. Drop out an existing balloon twister')
        command_no = int(input('Choose an option:'))
        return command_no 
    def execute_command(self, command_no):
        done = True
        if command_no == 1:
            print("============Schedule a balloon Twister=============")
            customer = input('Enter customer name: ')
            holiday = input('Enter holiday: ')
            self.__book.scheduleBooking(customer, holiday, False)
        elif command_no == 2:
            customer = input(
                'Enter customer name for whom you want to cancel the booking: ')
            holiday = input(
                'Enter holiday name: ')
            self.__book.cancelBooking(customer, holiday)
        elif command_no == 3:
            print('Please enter the name of a balloon twister or holiday: ')
            key_word = input()
            self.__book.checkStatus(key_word)
        elif command_no == 4:
            self.__book.saveBalloonTwister()
            self.__book.saveHolidays()
            self.__book.saveSchedule()
            self.__book.saveWaitingList()
            done = False
        elif command_no == 5:
            twister = input('Please enter the name of new balloon twister: ')
            self.__book.addBalloonTwister(twister)
        elif command_no == 6:
            balloon_twister = input("Enter the name of balloon twister who want to drop out: ")
            self.__book.dropBalloonTwister(balloon_twister)
        return done 

def main() -> None:
    app = BalloonTwisterApp()
    
    
    done = True
    while done is True:
        command_no: int = app.show_menu()
        done = app.execute_command(command_no)
        
if __name__ == "__main__":
    main()        