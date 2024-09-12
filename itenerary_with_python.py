import pyrebase

firebaseConfig ={
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "projectId": "",
  "storageBucket": "",
  "messagingSenderId": ",
  "appId": "",
  "measurementId": 
}# create a firebase realtime database and get the missing information 
firebase= pyrebase.initialize_app(firebaseConfig)
db= firebase.database()


def add_to_database(): 
  # Input for the day
  day = input("Which day are we planning for?: ")

  # Input for the tasks
  input_data = input("Enter the tasks separated by commas: ")

  # Splitting the input into individual tasks and converting to a list
  data4 = [item.strip() for item in input_data.split(',')]

  # Store data in Firebase under the input day
  db.child(day).set(data4)

  print(f"Data for {day} has been saved to Firebase.")
  itenerary()

def get_data():
  day= input("what day are we looking for?")
  tasks=db.child(day).get()
  #check if data exists for friday and print it
  if tasks.val():
    print(f"Tasks for {day}:",tasks.val())
  else:
    ask=input(f"no tasks for {day} would you like to add?[y/n]")
    if ask=="y":
      add_to_database()
    else:
      get_data()
  itenerary()

def retrieve_all():
  all_data=db.get()
  if all_data.each():
    for record in all_data.each():
      print(f"{record.key()}:{record.val()}")
  else:
    print("no data found in the database.")
def delete():
  ans= input("are you sure you want to delete everything?[y/n]")
  if ans=="y":
    db.remove()
    print("all tasks have been cleared.")
  else:
    print("deletiion canceled.")
  itenerary()

def update_data():
  day=input("what day are we updating?")
  data_to_update= input("enter data separated by commas:")
  data5 = [item.strip() for item in data_to_update.split(',')]
  db.child(day).update(data5)
  print(f"tasks for {day} have been updated successfully.")
  itenerary()


def remove_specific_day():
  day=input("what day would you like to remove?")
  db.child(day).remove()
  ans=input("are you sure you want to remove the tasks?[y/n]")
  if ans=="y":
    print(f"data for{day}removed successfully")
  else:
    print("deletion cancelled")
  itenerary()


def remove_specific_activity():
  day=input("what day are we removing")
  task=input("what task are we removing?")
  tasks=db.child(day).get()
  if tasks.val() and task in tasks.val():
    db.child(day).child(task).remove()
    print(f"task{task} removed from {day}")
  else:
    print(f"task{task} does not exist for {day}")
  itenerary()


def search_task():
  task= input("what task are you searching for?")
  all_data=db.get()
  found=False
  if all_data.each():
    for record in all_data.each():
      tasks=record.val()
      if isinstance(tasks, list) and task in tasks:
        print(f"task {task} is scheduled on {record.key()}.")
        found=True
  if not found:
    print(f"task {task} was not found on any day")
  itenerary()

def itenerary():
  ans = input("what would you like to do?  [add/get/all/delete/update/remove/REMOVE/search]")
  if ans == "add":
    add_to_database()
  elif ans == "get":
    get_data()
  elif ans == "all":
    retrieve_all()
  elif ans == "delete":
    delete()
  elif ans == "update":
    update_data()
  elif ans == "remove":
    remove_specific_day()
  elif ans == "REMOVE":
    remove_specific_activity()


  elif ans == "search":
    search_task()

  else:
    print("Invalid input please enter y for adding task, n for seeing specific days or m to see all events.")



itenerary()

















