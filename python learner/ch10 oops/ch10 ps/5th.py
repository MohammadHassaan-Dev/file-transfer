# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways(or can be Pakistani Railways)

from random import randint

class Train:
    def book_ticket(self, fro, to, trainno):
        print(f"Your ticket is booked in Train No {trainno} from {fro} to {to}")

    def get_status(self, trainno):
        print(f"Train {trainno} is running on time")

    def fare_info(self, trainno, fro, to):
        print(f"Ticket fare in Train {trainno} from {fro} to {to} is ${randint(500, 5000)}")


o = Train()
o.book_ticket("LHR", "FSD", 43468)
o.get_status(57657)
o.fare_info(57657, "LHR", "FSD")


