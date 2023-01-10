from booking import Booking
from db import BookingRepository
from tabulate import tabulate
class Scheduler:
    def __init__(self, manager : str = 'Nancy') -> None:
        self.__manager = manager
        self.__twisters : list[str] = []                                # List of Balloon Twisters
        self.__holidays : list[str] = []                                # List of Holidays
        self.__bookings : list[Booking] = []                            # List Of Bookings
                
        self.__waiting_list : list[str] = []
        self.getBalloonTwister()
        #self.getHolidays()
        #self.getSchedule()
        #self.getWaitingList()
    
    #Read and save from and to DB    
    def saveBalloonTwister(self):
        br = BookingRepository()
        br.saveBalloonTwister(self.__twisters)
    def getBalloonTwister(self):
        br = BookingRepository()
        self.__twisters = br.getBalloonTwister()
    def saveHolidays(self):
        br = BookingRepository()
        br.saveHolidays(self.__holidays)
    def getHolidays(self):
        br = BookingRepository()
        self.__holidays = br.getHoliday()
    def saveSchedule(self):
        br = BookingRepository()
        br.saveSchedule(self.__bookings)
    def getSchedule(self):
        br = BookingRepository()
        self.__bookings = br.getSchedule()
    def saveWaitingList(self):
        br = BookingRepository()
        br.saveWaitingList(self.__waiting_list)
    def getWaitingList(self):
        br = BookingRepository()
        self.__waiting_list = br.getWaitingList()    
        
    
    
    
    # 1) Schedule booking
    def scheduleBooking(self, customer : str, holiday : str, reschedule : bool) -> None:
        
        found : bool = True
        for twister in self.__twisters:
            for booking in self.__bookings:
                if booking.balloon_twister not in self.__bookings:
                    found = False
                    b = Booking(customer, holiday, twister)
                    self.__bookings.append(b)
                    
                    
                    self.saveSchedule()
                    if holiday not in self.__holidays:
                        self.__holidays.append(holiday)
                        self.saveHolidays()
                    if reschedule == True:
                        print("There has been a reschedule as Balloon Twister was dropped out!")
                        print(f"Ballon Twister: {twister}, has been rescheduled for customer: {customer}, for {holiday} holiday!")
                    elif reschedule == False:        
                        print(f"Ballon Twister: {twister}, has been booked for customer: {customer}, for {holiday} holiday!")
                    break
        if found == True:
            waiting = [customer, holiday]
            if reschedule == True:
                self.__waiting_list.insert(0, waiting)
                
                print(f"Balloon Twister has been dropped but no new Balloon Twister available at the moment\nCustomer : {customer} for holiday : {holiday} has been added to the TOP of the waiting list")
                print("Here's the waiting list:")
                print(self.__waiting_list)
            elif reschedule == False: 
                self.__waiting_list.append(waiting)
                print(f"Balloon Twister not available at the moment\nCustomer : {customer} for holiday : {holiday} has been added to the waiting list")
                print("Here's the waiting list:")
                print(self.__waiting_list)
            self.saveWaitingList()
            
            
    # 2) Cancel Booking
    def cancelBooking(self, customer : str, holiday : str) -> None:
        found : bool = False
        book : bool = False
        for booking in self.__bookings:
            if booking.customer == customer and booking.holiday == holiday:
                book = True
                self.__bookings.remove(booking)
                
                print(f"Customer : {customer} has canceled booking for the {holiday} holiday!")
                self.saveSchedule()
                
                #check if waiting list is empty or not
                if self.__waiting_list is not None:
                    print("This is the current waiting list: ")
                    print(self.__waiting_list)
                    for data in self.__waiting_list:
                        if data[1] == holiday:
                            found = True
                            book = Booking(data[0], holiday, booking.balloon_twister)
                            self.__bookings.append(book)
                            
                            
                            print(f"Customer : {data[0]} has been removed from the waiting list")
                            print(f"Ballon Twister: {booking.balloon_twister}, has been booked for customer: {data[0]}, for {holiday} holiday!")
                            print("New waiting List: ")
                            self.__waiting_list.remove(data)
                            self.saveWaitingList()
                            self.saveSchedule()
                            print(self.__waiting_list)
                    if found == False:
                        print("The waiting list is unchanged as holiday in the waiting list doesn't match with the holiday for which the booking has been canceled.")    
            
        if book == False:
            print("Sorry Booking can't be canceled, ballon name or holiday name mismatched. Please try again!")                
                            
    #3) Status
    def checkStatus(self, keyWord : str) -> None:
        found = False
        if keyWord in self.__twisters:
            twister_dict = {}
            for booking in self.__bookings:
                if booking.balloon_twister == keyWord:
                    #twister_dict[keyWord] = 
                    print()
                    
                    
                    found = True
                    break
        elif keyWord in self.__holidays:
            holiday_dict = {}
            for booking in self.__bookings:
                if booking.holiday == keyWord:
                    #holiday_dict[keyWord] = 
                    print()
                    #print(tabulate(holiday_dict, headers="keys", tablefmt="grid"))
                    found = True
                    break
        if found == False:
            print("Neither Ballon Twister name nor holiday matches with the booking")
    
    # 5) Add new Balloon Twister
    #add Balloon Twister
    def addBalloonTwister(self, twister : str) -> None:
        if twister not in self.__twisters:
            self.__twisters.append(twister)
            self.saveBalloonTwister()
            print(f"New Balloon Twister {twister} has been added to the List!")
            
           
                
        else:
            print("Balloon Twister is already in the list!")
    
    # 6) Drop out Balloon Twister
    def dropBalloonTwister(self, twister : str) -> None:
        
        if twister in self.__twisters:
            self.__twisters.remove(twister)
            
        
           
                
                
            
                                        
                                        
            
                        
                                        
            
                    
            
            
            
                             
           