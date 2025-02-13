
class User():

    _id_counter = 0
    _Level = {"Unverified", "Verified", "Nitro"}

    def __init__(self, level):
        User._id_counter += 1
        self.instance_id = User._id_counter
        self.message_log = []
        if level not in self._Level:
            self.level = "Unverified"
        else:
            self.level = level

    def add_message(self, message):
        self.message_log.append(message)
    

    def view_message(self):
        print(f"Messages from User {self.instance_id}:")
        for message in self.message_log:
            print(f" - {message}")


class Channel():

    def __init__(self):
        self.message_channel = []

    def add_message(self, user, message, pin):
        if user.level == "Verified":
            if len(message) > 100:
                print(user.id, "Message too long")
            else:
                self.message_channel.append((user, message))
        elif user.level == "Nitro":
            if pin:
                self.message_channel.insert(0, (user, message))
            else:
                self.message_channel.append((user,message))
        else:
            print("Invalid user", user.instance_id)


    def display_channel(self):
        print("--- View Channel ---")
        for user, message in self.message_channel:
            print(f"User {user.instance_id} ({user.level}): {message}")


def test_discord():
    channel = Channel()
    user1 = User("Nitro")
    user2 = User("Verified")
    user3 = User("Unverified")
    channel.add_message(user1, "Message 1 from Nitro", False)
    channel.add_message(user1, "Message 2 from Nitro", False)
    channel.add_message(user2, "Message from Verified User", False)
    channel.add_message(user1, "Pinned!", True)
    channel.add_message(user3, "Message 3 from Nitro", False)
    channel.display_channel()
    print()
    user1.view_message()
    user2.view_message()
    user3.view_message()

test_discord()
