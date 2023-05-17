'''
going to make a calendar
that can be viewed
that can be updated
that can be deleted events
'''

from time import sleep, strftime

fName = "Stephen"
calendar= {}

def welcome():
  print "Welcome to your calendat %s" % fName
  print "Opening your Calendar..."
  sleep(1)
  print "Today is: " + strftime("%A %B %d, %Y")
  print "Time is: " + strftime("%I")
  sleep(1)
  print "What would you like to do?"


def start_calendar():
  welcome()
  start = True
  while start == True:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "Calendar empty."
      else:
        print calendar
    elif user_choice == "U":
      date = raw_input("What Date?")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Update Successful.."
      print calendar
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print "date invalid"
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print "Calendar Empty."
      else:
        event = raw_input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "Calendar Event Deleted."
            print calendar
          else:
            print "no event to delete"
    elif user_choice == "X":
      start = False
    else:
      print "Invalid Range."
      start = False

start_calendar()
