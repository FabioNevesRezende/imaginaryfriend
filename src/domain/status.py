from .abstract_entity import AbstractEntity
from src.utils import deep_get_attr
from src.component.config import config


class Status(AbstractEntity):
    """
    Special class for message which contains info about status change
    """
    def __init__(self, message):
        super(Status, self).__init__(message)
        self.bot_name = config['bot']['name']

    def is_bot_kicked(self):
        """
        Returns True if the bot was kicked from group.
        """
        user_name = deep_get_attr(self.message, 'left_chat_member.username')

        return user_name == self.bot_name

    def is_bot_added(self):
        """
        Returns True if the bot was added to group.
        """
        new_members = self.message.new_chat_members
        if new_members is None:
            return False

        return any(self.bot_name == m.username for m in new_members)
