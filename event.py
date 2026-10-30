class Venue:

    def __init__(self,venue_id : int ,venue_name: str,capacity:int ):
        """

        :param venue_id:
        :param venue_name:
        :param capacity:
        :return:
        """
        self.venue_id= venue_id
        self.venue_name = venue_name
        self._capacity = capacity






    def get_venue_id(self)-> int:
        """

        :return:
        """
        return self.venue_id

    def get_venue_name(self)-> str:
        """

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

    def __init__(self,event_id,event_title,start_time,event_date,event_type,cancelled,venue_name ,capacity,ticket_price):

        if event_type.lower() in Event._allowed_events:
            self._event_type = event_type


        if capacity < 0:
            print("Please set apporiate number of attendants")
        else:
            self._capacity = capacity


        self._event_id = event_id
        self.start_time =start_time
        self.cancelled = cancelled
        self.ticket_price =ticket_price
        self.event_date= event_date
        self.event_title = event_title
        self.venue_name = venue_name










    def update_event_details(self,updated_date, updated_time):
        """
        Updates  date and start time for an event
        args  :updated_date:
              :updated_time:
        return : True
        """

        
        self.event_date = updated_date
        self.start_time = updated_time
        return True



    def change_event_type(self,new_type):
        
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
        


    def change_venue(self,new_venue):

        self.venue_name = new_venue




    def cancel_event(self):
        if self.cancelled :
            return True
        else:
            return False


    def __str__(self) -> str:
        return  (f"Event Title:{self.event_title}, Event {self._event_type} Venue {self.venue_name} ,Capacity {self._capacity},Event Date:{self.event_date}  Start Time: {self.start_time},Ticket Price:{self.ticket_price}  ")





