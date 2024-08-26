

class AppointmentsHandler:
    def __init__(self, bot):
        self.bot = bot

    def appointments_bnt_handler(self):
        pass

class AddAppointmentHandler:
    def __init__(self, bot):
        self.bot = bot
        self.APPOINTMENT_HISTORY = {}

    def add_appointment_bnt_handler(self):
        pass

    def check_appointment_availability(self):
        pass

    def appointment_availability_handler(self):
        pass

    def get_currency_rate(self):
        pass  # Отримання актуального курсу валюти

class ViewAppointmentHandler:
    def view_appointments(self):
        pass  # Перегляд наявних записів

    def delete_appointment(self):
        pass  # Видалення запису

class DeleteAppointmentHandler:
    def view_appointments(self):
        pass  # Перегляд наявних записів

    def delete_appointment(self):
        pass  # Видалення запису