# depan = "rifandi"
# belakang = "winarya"
# full = f"{depan} {belakang}"
# print(full)

from datetime import datetime

today = datetime.now()

date_time = today.strftime("%Y-%m-%d-%H-%M-%S")
print(date_time)