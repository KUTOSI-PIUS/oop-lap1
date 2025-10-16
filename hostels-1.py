class Hostel:
    def __init__(self, name, location, room_number, capacity):
        self.name = name
        self.location = location
        self.room_number = room_number
        self.capacity = capacity  # Maximum number of guests
        self.guests = []  # List to store guests
        self.visitors = {}  # Dictionary to store visitors by room number

    def check_in(self, guest_name):
        if len(self.guests) < self.capacity:
            if guest_name not in self.guests:  # Prevent duplicate check-ins
                self.guests.append(guest_name)
                return f"{guest_name} has been checked in."
            else:
                return f"{guest_name} is already checked in."
        else:
            return "Hostel is full."
    def check_out(self, guest_name):
        if guest_name in self.guests:
            self.guests.remove(guest_name)
            return f"{guest_name} has been checked out."
        else:
            return f"{guest_name} is not found in the hostel."

    def get_guest_list(self):
        return self.guests

    def record_visitor(self, visitor_name, guest_name, room_number):
        if guest_name in self.guests:
            if room_number not in self.visitors:
                self.visitors[room_number] = []
            self.visitors[room_number].append(visitor_name)
            return f"Visitor {visitor_name} has been recorded for {guest_name} in room {room_number}."
        else:
            return f"Guest {guest_name} is not checked in."

    def get_visitors(self, room_number):
        return self.visitors.get(room_number, [])
    
    def get_hostel_details(self):
        return f"Hostel Name: {self.name}, Location: {self.location}, Room Number: {self.room_number}, Capacity: {self.capacity}"
hostel = Hostel("Sunny Hostel", "Beach Road", 101, 10)
hostel.check_in("Alice")
print(hostel.record_visitor("Bob", "Alice", 101))  # Bob visits Alice
print(hostel.get_visitors(101))  # Get visitors for room 101
print(hostel.get_guest_list())  # List of current guests
print(hostel.get_hostel_details())  # Hostel details
