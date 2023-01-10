from booking import Booking
import csv

class BookingRepository:
    def __init__(self, file1 : str = "Balloon Twisters.dat", file2 : str = "Holidays.dat", file3: str = "Schedule.csv", file4 : str = "Waiting.csv") -> None:
        self.__file1 = file1
        self.__file2 = file2
        self.__file3 = file3
        self.__file4 = file4
    
    #Balloon Twister read and write    
    
    def getBalloonTwister(self) -> list[str]:
        balloonTwister : list[str] = []
        with open(self.__file1, newline='') as file:
            reader = file.readlines()
            for row in reader:
                balloonTwister.append(row.strip("\r\n"))
        
                
        return balloonTwister
    def saveBalloonTwister(self, balloonTwister : list[str]) -> None:
        with open(self.__file1, "w", newline='') as file:
            # writer = csv.writer(file)
            # writer.writerow(balloonTwister)
            for line in balloonTwister:
                file.write(line)
                file.write("\n")
            
    
    #Holiday read and write
    def getHoliday(self) -> list[str]:
        holidays : list[str] = []
        with open(self.__file2, newline="") as file:
            reader = file.readlines()
            for row in reader:
                holidays.append(row.strip("\r\n"))
        return holidays
    def saveHolidays(self, holidays : list[str]) -> None:
        with open(self.__file2, "w", newline="") as file:
            for line in holidays:
                file.write(line)
                file.write("\n")
    
    #Schedule read and write
    def getSchedule(self) -> list[str]:
        schedule : list[str] = []
        with open(self.__file3, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                read = Booking(row[0], row[1], row[2])
                schedule.append(read)
        return schedule
    
    def saveSchedule(self, schedule : list[Booking]) -> None:
        with open(self.__file3, "w", newline="") as file:
            writer = csv.writer(file)
            for data in schedule:
                attributes : list[str] = [data.customer, data.holiday, data.balloon_twister]
                writer.writerow(attributes)
    
    #waiting list read and write
    def getWaitingList(self) -> list[str]:
        waiting : list[str] = []
        with open(self.__file4, 'r') as file:
            
            for row in file:
                data = row[:-1]
                waiting.append(data)
                
        return waiting
    def saveWaitingList(self, waiting : list[str]) -> None:
        with open(self.__file4, "w") as file:
            
            for data in waiting:
                #attributes : list[str] = [data[0], data[1]]
            
                file.write(f'{data}\n')                                
            
    
    
def main():
    b = BookingRepository()
    twister: list[str] = b.getBalloonTwister()
    print(twister)
    print("List of Balloon Twister after new Balloon Twister is added")
    b1, b2, b3, b4, b5 = "Shadman", "Aya", "Susan", "Alla", "Aya"
    l : list[str] = [b1, b2, b3, b4, b5]
    b.saveBalloonTwister(l)
    # b.saveBalloonTwister(["Wasif"])
    # b.saveBalloonTwister(["Alla"])
    twister: list[str] = b.getBalloonTwister()
    print(twister)
    print("List of holidays:")
    holidays : list[str] = b.getHoliday()
    print(holidays)
    
if __name__ == "__main__":
    main()                    
        