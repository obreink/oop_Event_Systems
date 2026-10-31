import datetime

class Venue:

    def __init__(self,venue_id : int ,venue_name: str,capacity:int ):
        """
        Creates a venue
        :param venue_id: id for the venue
        :param venue_name: name for the venue
        :param capacity: maximum number of people a venue can host

        """
        self._venue_id= venue_id
        self.venue_name = venue_name
        self._capacity = capacity






    def get_venue_id(self)-> int:
        """
        gets the id of the venue
        :return: venue id
        """
        return self.venue_id

    def get_venue_name(self)-> str:
        """
        Prints out the name of the venue
        :return:
        """

        return self.venue_name

    def get_venue_capacity(self)-> int:
        """

        :return:
        """
        return self._capacity


    def __str__(self) -> str:
        return f"{self.venue_id}  ({self.venue_name}),capacity {self._capacity}"


class Event:
    _allowed_events :list[str] = ["workshop","conference","open day","convention"]
    ticket_prices:dict[str,float] ={

    }

    def __init__(self,event_id :int ,event_title :str,start_time:datetime.time,event_date:datetime.date,event_type :str,cancelled :bool,venue_name: str ,capacity :int,ticket_price: float):

        if event_type.lower() in Event._allowed_events:
            self._event_type = event_type


        if capacity < 0:
            print("Please set apporiate number of attendants")
        else:
            self._capacity = capacity


        self._event_id = event_id
        self._start_time = start_time
        self.cancelled = cancelled
        self.ticket_price=ticket_price
        self.event_date= event_date
        self.event_title = event_title
        self.venue_name = venue_name


    def update_event_details(self,updated_date :datetime.date , updated_time:datetime.time)-> bool:
        """
        Updates  date and start time for an event
        args  :updated_date: new date for the event
              :updated_time: new time the event will start on.
        return : True
        """


        self.event_date = updated_date
        self._start_time = updated_time
        return True



    def change_event_type(self,new_type: str)-> bool:
        
        """
        Changes the existing event type to a new event type but only in the allowed event type list
        args:
            new_type

        :return:
           True if the new type is in the allowed event type
           False if the new type is a type of event not found in the list of allowed events
        """
        
        if new_type in Event._allowed_events:
            self._event_type = new_type
            return True
        else:
            return  False
        


    def change_venue(self,new_venue :str):
        """
        Updates or changes the venue for an event
        :param new_venue: new venue name

        """

        self.venue_name = new_venue

    def print_active_events(self,events:str )-> bool:
        """
        Prints out all active events by selecting all events that are not cancelled
        :param events: events a list of all events
        :return: active events
        """
        active_event= []
        for event in events:
            if not self.cancelled:
                active_event.append(event)

        return active_event


    def cancel_event(self)-> bool:
        """
        checks if event is event has been cancelled
        :return: True if event is cancelled
               : False if the event has not been cancelled
        """
        if self.cancelled :
            return True
        else:
            self.cancelled = False


    def __str__(self) -> str:
        """
        Prints out string information about the event
        :return: Event details
        """
        return (f"Event ID: {self._event_id},Event Title:{self.event_title}, Event {self._event_type} Venue {self.venue_name} ,Capacity {self._capacity},Event Date:{self.event_date}  Start Time: {self.start_time},Ticket Price:{self.ticket_price}  ")

if __name__ == "__main__":
    Venue1=Venue(1,"Faulkner hall",20)
    event1 =Event(3,"Work camp", 1000, 2026,"workshop",cancelled= False,venue_name=Venue1,capacity=20,ticket_price=20.99)
    event1.cancel_event()


