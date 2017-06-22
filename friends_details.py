from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class Chat_Message:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('alpha', 'Mr.', 22, 3.0)

friend_one = Spy('tango', 'Mr.', 24, 4.8)
friend_two = Spy('charlie', 'Ms.', 26, 4.7)
friend_three = Spy('jojo', 'Dr.', 28, 4.9)


friends = [friend_one, friend_two, friend_three ]


