from datetime import datetime
from time import sleep

# simple application to countdown until an event

print("This is an application that will allow you to countdown until a certain event")
print("Enter what you want your event to be called, the start date, and a time (if desired)\n")


def date_difference(user_entered_date, user_entered_time):
    future_date = datetime.strptime(user_entered_date + " " + user_entered_time, "%m/%d/%Y %H:%M:%S")
    now = datetime.now().replace(microsecond=0)

    while future_date > now:
        timedelta = future_date - now
        print(timedelta)
        sleep(1)
        now = datetime.now().replace(microsecond=0)


def main():
    event = input('Event name: ')
    date = input('Start date e.g.(06/10/1998): ')

    while True:
        start_time = input("Does your event have a start time? Enter yes or no: ")
        if start_time.lower() == "yes":
            time = input('Time event starts: e.g.(05:21:13: ')
            break

        elif start_time.lower() == "no":
            time = "00:00:00"
            break

        else:
            print("You did not enter a valid response. Please try again!")
            continue

    print(f"\n{event} countdown:")

    date_difference(date, time)


main()
