import sys,shelve
def store_person(db):
    pid = raw_input("Enter unique ID number:")
    person = {}
    person["name"] = raw_input("Enter name:")
    person["age"] = raw_input("Enter age:")
    person["phone"] = raw_input("Enter phone number:")
    db[pid] = person
def lookup_person(db):
    pid = raw_input("Enter ID number:")
    field = raw_input("what would you like to know?(name,age,phone)")
    field = field.strip().lower()
    print field.capitalize() + ':',\
           db[pid][field]
def print_help():
    print "the available commands are:"
    print "store:stores information about a person"
    print "look up :looks up a person from ID number"
    print "quit:save changes and exit"
    print "?:prints this messagte"
def enter_commond():
    cmd = raw_input("Enter command (? for help):")
    cmd = cmd.strip().lower()
    return cmd
def main():
    database = shelve.open("/Users/lh/PycharmProjects/untitled3/test")
    try:
        while True:
            cmd = enter_commond()
            if cmd == "store":
                store_person(database)
            elif cmd == "lookup":
                lookup_person(database)
            elif cmd == "?":
                print_help()
            elif cmd == "quit":
                return
    finally:
        database.close()
if __name__ == '__main__':main()
print "Done!"
