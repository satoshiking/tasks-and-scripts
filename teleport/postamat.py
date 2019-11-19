import requests
import json
from datetime import datetime

def pretty_print_json(data):
    for st in data:
        print(json.dumps(st, indent="   ",ensure_ascii=False, sort_keys=True))


class Postamat:

    def __init__(self, 
                 id, address, is_automated, accept_cash, accept_card, bank_terminal,
                 status_code=99, lat=None, lng=None, description="",
                 **kwargs):
        self.id = id
        self.address = address
        self.is_automated = is_automated
        self.accept_cash = accept_cash
        self.accept_card = accept_card
        self.bank_terminal = bank_terminal
        self.status_code = status_code
        self.lat = lat
        self.lng = lng
        self.description = description
        self.type = kwargs.get("type")

        # Read-only attributes
        self._name = kwargs.get("name")
        self._address_struct = kwargs.get("address_struct")
        self._status = kwargs.get("status")
        self._accept_payments = kwargs.get("accept_payments")
        self._working_hours = kwargs.get("working_hours")


    @property
    def name(self):
        return self._name

    @property
    def address_struct(self):
        return self._address_struct
    
    @property
    def status(self):
        return self._status

    @property
    def accept_payments(self):
        return self._accept_payments

    @property
    def working_hours(self):
        return self._working_hours

    def is_working(self):
        day = datetime.today().weekday()        
        time = datetime.today().strftime("%H:%M")
        if len(self.working_hours) > day:
            time_open = self.working_hours[day].get("time_open")
            time_close = self.working_hours[day].get("time_close")

            if time_open <= time <= time_close:
                return "Yes"
            else:
                return "No"
        else:
            return "no information"

"""
if __name__ == '__main__':
    r = requests.get("https://api.tport.online/v2/public-stations")
    data = json.loads(r.text)
    
    id_list = []
    for d in data:
        id_list.append(d["id"])

    print(id_list)
    #pretty_print_json(data[:1])
"""