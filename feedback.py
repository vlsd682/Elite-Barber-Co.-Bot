from commands import StandardCommands, FeedbacksCommands, AppointmentCommands
from messages import FeedbacksMessages

class FeedbacksHandler:
    '''
    Class for handling command: /feedbacks.

    Attributes:
    bot -- the instance used to interact with the Telegram API
    '''
    def __init__(self, bot):
        '''Initializes ViewFeedback with a bot instance.'''
        self.bot = bot
        self.CommandHistory = bot.CommandHistory
        self.FeedbacksButtons = FeedbacksButtons()


    def feedbacks_btn_handler(self):
        @self.bot.telegram_bot.message_handler(commands=['feedbacks'])
        @self.CommandHistory.command_decorator
        def feedbacks(msg):
            self.bot.send_message(msg.chat.id, FeedbacksMessages.FEEDBACKS_MSG, self.FeedbacksButtons.feedbacks_btns())


class ViewFeedbackHandler:
    '''
    Class for handling command: /view_feedback.

    Attributes:
    bot -- the instance used to interact with the Telegram API
    '''
    def __init__(self, bot):
        '''Initializes ViewFeedback with a bot instance.'''
        self.bot = bot

    def view_feedback_bnt_handler(self):
        pass

    def check_correctness_recipient(self):
        pass

    def show_feedback_recipient(self):
        pass

class AddFeedbackHandler:
    def __init__(self, bot):
        self.bot = bot
        self.ADD_FEEDBACK_HISTORY = {}

    def add_feedback_btn_handler(self):
        pass

    def check_correctness_recipient(self):
        pass

    def feedback_text_verification(self):
        pass

    def add_feedback_to_db(self):
        pass

    def clean_add_feedback_history(self):
        pass

    def clean_user_history(self):
        pass

    def validate_feedback_length(self, feedback):
        pass

    def check_profanity(self, feedback):
        pass

class DeleteFeedbackHandler:
    def __init__(self, bot):
        '''Initializes ViewFeedback with a bot instance.'''
        self.bot = bot

    def delete_feedback_bnt_handler(self):
        pass

    def check_feedback_availability(self):
        pass

    def absence_feedback_handler(self):
        pass

    def delete_feedback_confirmation(self):
        pass

    def delete_feedback_from_db(self):
        pass

    def clean_user_history(self):
        pass

class FeedbacksButtons:
    '''
    Class for generating buttons for the Feedbacks.
    '''
    def feedbacks_btns(self):
        return [
            StandardCommands.HELP_BTN,
            AppointmentCommands.VIEW_APPOINTMENT_BTN,
            AppointmentCommands.ADD_APPOINTMENT_BTN,
            AppointmentCommands.DELETE_APPOINTMENT_BTN,
            StandardCommands.START_BTN,
            StandardCommands.BACK_BTN
            ]
