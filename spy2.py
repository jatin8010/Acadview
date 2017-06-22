from friends_details import spy, Spy, Chat_Message, friends
from steganography.steganography import Steganography
from datetime import datetime
# import detais from above mentioned functions


status_message= ['plata o plomo']


print "Hello! Let\'s go"
#displayed message
question = "would you like to continue as " + spy.salutation + " " + spy.name + " (Yes/No)? "
existing = raw_input(question)


def add_status():
#defining function add_status
   updated_status_message = None

   if spy.current_status_message != None:
       print 'Your status message is %s \n' % (spy.current_status_message)
   else:
       print 'You have no status message currently \n'
#displaying if-else condition
   default = raw_input('Select from the older status (Y/N)?')

   if default.upper() == "N":
        new_status_message = raw_input("New status message ")


        if len(new_status_message) > 0:
            status_message.append(new_status_message)
            updated_status_message = new_status_message
#using len() to display length of characters
   elif default.upper() == 'Y':

        item_position = 1

        for message in status_message:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))
#select status above mentioned messages

        if len(status_message) >= message_selection:
            updated_status_message = status_message[message_selection - 1]

        else:
            print 'This option is invalid! Say yes or no.'

   if updated_status_message:
        print 'updated status message is: %s' % (updated_status_message)
   else:
        print 'You current don\'t have a status update'
#print update status message
   return updated_status_message



def add_friend():

    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input(" enter friend's name: ")
    new_friend.salutation = raw_input(" Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)
# defining friend spy name, age, rating
    if len(new_friend.name) > 0 and new_friend.age > 45  and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Invalid entry. spy can\'t be added with the provided details '

    return len(friends)


def select_a_friend():
    item_number = 0
# selecting friend
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1,
                                                                friend.salutation,
                                                                friend.name,
                                                                friend.age,
                                                                friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():

    friend_choice = select_a_friend()
# selecting friend to send secret message
    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)
# encoding steganographic image
    new_chat = Chat_Message(text,True)

    friends[friend_choice].chats.append(new_chat)

    print "encoded content ready!"
# encoded content ready to send

def read_message():
# reading a message
    sender = select_a_friend()

    output_path = raw_input("enter file name ")

    secret_text = Steganography.decode(output_path)

    new_chat = Chat_Message(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "secret message saved!"

# decoding encoded secret messaqe
def read_chat_history():
# defining function to read chat history
    read_for = select_a_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


def close():
    print 'Your application is closed'




def start_chat(spy):
# staert a chat with another friend
    spy.name = spy.salutation + " " + spy.name


    if spy.age >  20 and spy.age < 45 :


        print " Welcome " + spy.name + " age: " \
              + str(spy.age) + \
              " and rating of: "\
              + str(spy.rating) + \
              " Nice to see you "

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n " \
                           "1. Add a status update \n " \
                           "2. Add a friend \n " \
                           "3. Send a secret message \n " \
                           "4. Read a secret message \n " \
                           "5. Read Chats from a user \n " \
                           "6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                elif menu_choice == 6:
                    close()
                else:
                    show_menu = False
# opening menu and selecting choices
    else:
        print ' you are not of the correct age to be a spy'

if existing == "Yes":
    start_chat(spy)
else:

    spy = Spy('','',0,0.0)


    spy.name = raw_input("Welcome spy , enter spy name: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("enter your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("enter spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please add a valid spy name'

# end of program
