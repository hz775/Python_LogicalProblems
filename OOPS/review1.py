class Train:
    def __init__(self, train_name, date, coach_type, total_seats):
        self.train_name = train_name
        self.date = date
        self.coach_type = coach_type
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            print("Confirmed")
        elif self.booked_seats < self.total_seats + 2:
            self.booked_seats += 1
            print("Rac")
        elif self.booked_seats < self.total_seats + 4:
            self.booked_seats += 1
            print("Waitlist")

    def display_status(self):
        return f"Train: {self.train_name}, Date: {self.date}, Coach: {self.coach_type}, Booked: {self.booked_seats}"

    
class Passenger(Train):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.add_passenger=[]
    
    def add_passenger(self,a):
        self.add_passenger.append(a)
    
    def list_passenger(self):
        if not self.add_passenger:
            return f"passenger is not there"
        else:
            for que in self.add_passenger:
                return que
        

class Coach(Passenger):
    no_of_coaches=[]
    def __init__(self,name,age,coach_no):
        super().__init__(name,age)
        self.coach_no=coach_no
        
    
    def display_coach(self):
        return f"{self.name} and coach no:{self.coach_no}"
        
class Booking(Coach):
    def __init__(self):
        self.is_booking=True
    
    def booking_details(self):
        return f"{self.name} and {self.coach_no}"
    
train1=Train("VandeBharat","12/10/2001","Unreserved",3)
train1.book_seat()
train1.display_status()




    
