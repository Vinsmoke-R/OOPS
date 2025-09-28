class chatbot:

    __user_id = 0

    def __init__(self):
        self.id = chatbot.__user_id
        chatbot.__user_id +=1
        #self.id = ''
        self.__name = "Default name"
        self.password = ''
        self.loggedin = False
        #self.menu()
    @staticmethod
    def get_id():
        return chatbot.__user_id
    
    @staticmethod
    def set_id(value):
        chatbot.__user_id = value

    def menu(self):
        user_input = input(""""Welcome to Chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           -> """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.post()
        elif user_input == "4":
            self.msg()
        else:
            exit()

    def signup(self):
        uid = input("Enter your email here :")
        pwd = input("Type your password :")
        self.id = uid
        self.password = pwd
        print("you have signed in succesfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.id == '' and self.password == '':
            print("You are not signed in , please log in first !")
        else : 
            uid = input("Enter your user id")
            pwd = input("Enter your password")
            if self.id==uid and self.password==pwd:
                print("Your have signed in succefully")
                self.loggedin = True
            else:
                print("uid or pwd is incorrect")
        print("\n")
        self.menu()

    def post(self):
        if self.loggedin == True:
            text = input("Enter your message to text")
            print(f"you have uploaded the {text}")
        else:
            print("you need to log in first in order to post")
        print("\n")
        self.menu()
    
    def msg(self):
        if self.loggedin==True:
            msg = input("Enter your message")
            friend = input("Whom you want to send")
            print(f"your message {msg} is sent to your friend {friend}")
        else:
            print("You need to log in first")

        print("\n")
        self.menu()

user = chatbot()        