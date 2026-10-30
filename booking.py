from datetime import date


class Booking:
    #Stores one booking for an attendee and an event.
    def __init__(self, booking_id, attendee, event, booking_date,cancelled):
        #Create a booking and check its details
        valid = None
        if booking_id <= 0:
            print("Booking ID must be positive.")
        if attendee is None:
            print("Error: you must provide an event")
            valid = False
        elif event is None:
            print("Error: You must provide an event.")
            valid = False
        elif booking_date > date.today():
            print("Error: The booking date cannot be in the future.")
            valid = False
        if valid:
            self.booking_id = booking_id
            self._attendee = attendee
            self.event = event
            self.booking_date = booking_date
            self.cancelled = cancelled

    

