

class Logger():
    def __init__(self) -> None:
        pass
    
    def R(self):
        return open('logs/bot.log', 'r').read()
    
    def A(self, msg):
        with open('logs/bot.log', 'a') as file:
            file.write(msg + "\n")
    
    def W(self, msg):
        with open('logs/bot.log', 'w') as file:
            file.write(msg + "\n")
    
    def log(self, msg):
        self.A(msg)

    def reset(self):
        with open('logs/bot.log', 'w') as file:
            file.write("Session Started \n----------------\n")
 
