from project import chatbot

user1 = chatbot()
print(user1.id)

user2 = chatbot()
print(user2.id)
chatbot.set_id(10)
print(chatbot.get_id())

user3 = chatbot()
print(user3.id)

user4 = chatbot()
print(user4.id)
