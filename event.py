class Venue:

    def __int__(self,venue_id : int ,venue_name: str,capacity:int ):
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

    def __int__(self,event_id,event_title,start_time,event_date,_event_type,cancelled,capacity,ticket_price):

        self._event_id = event_id
        self








    def update_event_details(self,updated_date, updated_time):
        """
        Updates time and date for an event
        :args:
         updated_date:
         updated_time:
        :return:
            True
        """

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
        



    def change_venue(self):
        """

        :return:
        """

    def cancel_event(self):
        """

        :return:
        """


    def __str__(self) -> str: