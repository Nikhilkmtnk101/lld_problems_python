from parking_lot.entities.ticket import Ticket


class TicketDao:
    def __init__(self):
        self.tickets = {}

    def get_tickets(self) -> dict:
        return self.tickets

    def set_tickets(self, tickets: dict):
        self.tickets = tickets

    def get_ticket_by_id(self, ticket_id: str) -> Ticket:
        return self.tickets.get(ticket_id, None)

    def add_ticket(self, ticket: Ticket):
        self.tickets[ticket.get_ticket_id()] = ticket
