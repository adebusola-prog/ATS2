import csv
import datetime
today = datetime.date.today()

def read_csv(file_name):
    with open(file_name, "r") as x:
        read = csv.DictReader(x)
        return list(read)



def write_log_csv(customer, event):
    with open("customer_activity_logs.csv", "a", newline="\n") as x:
        header = ["Date_Time", "Event", "customer", "Message"]
        write = csv.DictWriter(x, fieldnames=header)

        data = {
            "Date_Time": today,
            "Customer": customer,
            "Event": event,
        }

        if len(read_csv("customer_activity_logs.csv")) < 1:
            write.writeheader()
            write.writerow(data)
        else:
            write.writerow(data)

