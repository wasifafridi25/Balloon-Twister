class Booking:
    def __init__(self, customer : str, holiday : str, balloon_twister : str) -> None:
        self.__customer = customer
        self.__balloon_twister = balloon_twister
        self.__holiday = holiday
    
    @property
    def customer(self) -> str:
        return self.__customer
    @property
    def balloon_twister(self) -> str:
        return self.__balloon_twister
    @property
    def holiday(self) -> str:
        return self.__holiday
    
    
    
    
    
    def display(self):
        print(f"Customer name = {self.__customer}, Balloon Twister name = {self.__balloon_twister}, Holiday = {self.__holiday}")
    
    def __str__(self) -> str:
        return f"Customer name = {self.__customer}, Balloon Twister name = {self.__balloon_twister}, Holiday = {self.__holiday}"    
    def __repr__(self) -> str:
        return str(self)
    
            