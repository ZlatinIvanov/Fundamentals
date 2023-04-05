class Party:
    def __init__(self):
        self.people = []
        return


party = Party()
total_people_going = 0
while True:
    names = input()
    if names == "End":
        print(f"Going: {', '.join(party.people)}")
        print(f"Total: {total_people_going}")
        break
    else:
        party.people.append(names)
        total_people_going += 1
