class TrainBooking:
    def __init__(self):
        self.trains = {
            "10080": {"name": "Chennai Express", "seats": 10},
            "12079": {"name": "Janashatabdi Express", "seats": 8},
            "11223": {"name": "Superfast 3", "seats": 15},
            "48996": {"name": "Rajdhani 4", "seats": 5},
        }
        self.bookings = {}

    # Admin Functions
    def add_train(self, train_num, name, seats):
        if train_num in self.trains:
            print("Train number already exists!")
        else:
            self.trains[train_num] = {"name": name, "seats": seats}
            print(f"Train {train_num} - {name} added successfully!")

    def remove_train(self, train_num):
        if train_num in self.trains:
            del self.trains[train_num]
            print(f"Train {train_num} removed successfully!")
        else:
            print("Train number not found!")

    def modify_train(self, train_num, name=None, seats=None):
        if train_num in self.trains:
            if name:
                self.trains[train_num]["name"] = name
            if seats:
                self.trains[train_num]["seats"] = seats
            print(f"Train {train_num} updated successfully!")
        else:
            print("Train number not found!")

    def view_train_bookings(self, train_num):
        if train_num in self.bookings:
            print(f"Bookings for Train {train_num}: {self.bookings[train_num]}")
        else:
            print("No bookings for this train!")

    def reset_bookings(self):
        self.bookings.clear()
        print("All bookings have been cleared!")

    # Passenger Functions
    def show_available_trains(self):
        print("\n--- Available Trains ---")
        for train_num, details in self.trains.items():
            print(f"Train {train_num}: {details['name']} | Seats Left: {details['seats']}")

    def book_ticket(self, train_num, passenger_name, date):
        if train_num in self.trains and self.trains[train_num]['seats'] > 0:
            self.trains[train_num]['seats'] -= 1
            if train_num not in self.bookings:
                self.bookings[train_num] = []
            self.bookings[train_num].append({"name": passenger_name, "date": date})
            print(f"Ticket booked for {passenger_name} on {self.trains[train_num]['name']} for {date}!")
        else:
            print("Sorry, train not found or no seats left!")

    def cancel_ticket(self, train_num, passenger_name, date):
        if train_num in self.bookings:
            for booking in self.bookings[train_num]:
                if booking["name"] == passenger_name and booking["date"] == date:
                    self.bookings[train_num].remove(booking)
                    self.trains[train_num]['seats'] += 1
                    print(f"Ticket canceled for {passenger_name} on Train {train_num} for {date}.")
                    return
        print("Cancellation failed. No such booking found!")

    def modify_booking(self, old_train, new_train, passenger_name, old_date, new_date):
        self.cancel_ticket(old_train, passenger_name, old_date)
        self.book_ticket(new_train, passenger_name, new_date)

    def show_reservations(self):
        print("\n--- Current Reservations ---")
        if not self.bookings:
            print("No reservations yet!")
        else:
            for train_num, passengers in self.bookings.items():
                print(f"Train {train_num} ({self.trains[train_num]['name']}):")
                for booking in passengers:
                    print(f"  - {booking['name']} on {booking['date']}")

# Main menu loop
if __name__ == "__main__":
    system = TrainBooking()
    user_type = input("Are you an Admin or a Passenger? (Enter 'admin' or 'passenger'): ").strip().lower()

    if user_type == "admin":
        while True:
            print("\n=== Admin Panel ===")
            print("6. Add Train")
            print("7. Remove Train")
            print("8. Modify Train")
            print("9. View Train Bookings")
            print("10. Reset All Bookings")
            print("0. Exit")
            choice = input("Choose an option: ")

            if choice == "6":
                train_no = input("Enter New Train Number: ")
                name = input("Enter Train Name: ")
                seats = int(input("Enter Number of Seats: "))
                system.add_train(train_no, name, seats)
            elif choice == "7":
                train_no = input("Enter Train Number to Remove: ")
                system.remove_train(train_no)
            elif choice == "8":
                train_no = input("Enter Train Number to Modify: ")
                name = input("Enter New Train Name (Press Enter to skip): ")
                seats = input("Enter New Seat Count (Press Enter to skip): ")
                seats = int(seats) if seats else None
                system.modify_train(train_no, name, seats)
            elif choice == "9":
                train_no = input("Enter Train Number to View Bookings: ")
                system.view_train_bookings(train_no)
            elif choice == "10":
                system.reset_bookings()
            elif choice == "0":
                print("Exiting Admin Panel...")
                break
            else:
                print("Invalid choice, please try again!")

    elif user_type == "passenger":
        while True:
            print("\n=== Passenger Menu ===")
            print("1. View Available Trains")
            print("2. Book a Ticket")
            print("3. Cancel a Ticket")
            print("4. Modify Booking")
            print("5. View Reservations")
            print("0. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                system.show_available_trains()
            elif choice == "2":
                train_no = input("Enter Train Number: ")
                pname = input("Enter Passenger Name: ")
                date = input("Enter Travel Date (YYYY-MM-DD): ")
                system.book_ticket(train_no, pname, date)
            elif choice == "3":
                train_no = input("Enter Train Number: ")
                pname = input("Enter Passenger Name: ")1
                date = input("Enter Travel Date (YYYY-MM-DD): ")
                system.cancel_ticket(train_no, pname, date)
            elif choice == "4":
                old_train = input("Enter Current Train Number: ")
                new_train = input("Enter New Train Number: ")
                pname = input("Enter Passenger Name: ")
                old_date = input("Enter Current Travel Date: ")
                new_date = input("Enter New Travel Date: ")
                system.modify_booking(old_train, new_train, pname, old_date, new_date)
            elif choice == "5":
                system.show_reservations()
            elif choice == "0":
                print("Exiting Passenger Menu...")
                break
            else:
                print("Invalid choice, please try again!")
