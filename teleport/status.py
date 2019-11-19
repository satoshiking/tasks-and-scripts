import sys

import requests
import json

from postamat import Postamat


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Exactly one argument is needed ...")
        print("Usage: python status.py \"id_list\"." +
              "Example: python status.py \"10, 20, 30, 55\"")
        sys.exit()
    else:
        id_list = [e.strip() for e in sys.argv[1].split(',')]
        print(id_list)
        print("Postamat status:")

        for id in id_list:
            url = "https://api.tport.online/v2/public-stations/" + str(id)
            r = requests.get(url)
            d = json.loads(r.text)

            if not d.get("detail"):
                p = Postamat(
                    d["id"], d["address"], d["is_automated"], d["accept_cash"],
                    d["accept_card"], d.get("bank_terminal"), d["status_code"],
                    d["lat"], d["lng"], d["description"], type=d.get("type"),
                    address_struct=d["address_struct"], status=d["status"],
                    accept_payments=d["accept_payments"],
                    working_hours=d["working_hours"])

                print(" ID={:<5} STATUS_CODE={:< 5} WORKING_NOW={}".
                      format(p.id, p.status_code, p.is_working()))
            else:
                print(" ID={:<5} {: <18}".format(id, d.get("detail")))
