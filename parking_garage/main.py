# main.py
from enums import PaymentMethod
from models.entry import Entry
from models.exit import Exit
from models.floor import Floor
from models.payment import Payment
from models.spot import CompactSpot, LargeSpot, MediumSpot
from models.user import Customer
from models.vehicle import Car, Truck, TwoWheeler
from parking_lot import ParkingLot


def main():
    # Initialize parking lot
    parking_lot = ParkingLot()

    # Create floors and spots
    floor1 = Floor([])
    floor1_id = "F1"

    # Add spots to floor
    for i in range(10):
        floor1.add_parking_spot(CompactSpot(floor1_id))
    for i in range(10):
        floor1.add_parking_spot(MediumSpot(floor1_id))
    for i in range(5):
        floor1.add_parking_spot(LargeSpot(floor1_id))

    # Add floor to parking lot
    parking_lot.floors.append(floor1)

    # Create entry and exit points
    entry = Entry(parking_lot)
    exit_point = Exit(parking_lot)

    # Customer arrives with a car
    car = Car("KA01HK4497")
    customer = Customer("John Doe", car)

    # Get ticket
    ticket = entry.get_ticket(customer, car)
    print(f"Ticket issued: {ticket.ticket_id}")

    # Customer leaves
    # Simulate payment
    payment = Payment(500, ticket, PaymentMethod.CASH)
    exit_result = exit_point.process_exit(ticket, payment)
    print(f"Exit processed successfully: {exit_result}")


if __name__ == "__main__":
    main()
