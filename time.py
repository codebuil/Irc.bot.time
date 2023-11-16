import datetime
import time
import socket
import threading

class IRCBot:
    def __init__(self, server, port):
        self.server = server
        self.port = port
        self.nick = "BOTtime"
        self.password = "time"
        self.channel = "#home"
        self.in_bot_mode = False

        

        self._index =0
    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server, self.port))
        self.send_message(f"USER {self.nick} 0 * :{self.nick}\r\n")
        self.send_message(f"NICK {self.nick}\r\n")
        self.send_message(f"JOIN {self.channel}\r\n")
        self.enviar_p()
    def enviar_p(self):
        receive_thread =threading.Thread(target=self.receive_messages)
        receive_thread.start()
        while True:
            # Espera 1 minuto
            time.sleep(60)

            agora = datetime.datetime.now()
            data_hora = agora.strftime("%Y-%m-%d %H:%M:%S")
            data_horas = agora.strftime("%M")
            if data_horas== "48" or data_horas=="00" or data_horas=="0" or data_horas=="30":
            # Envia a mensagem publicitária para o canal
                self.send_message(f"PRIVMSG {self.channel} :{data_hora}\r\n")
            
    def send_message(self, message):
        self.sock.send(message.encode("utf-8"))

   
    def receive_messages(self):
        while True:
            data = self.sock.recv(4096).decode("utf-8")
            if not data:
                break
            print(data)

            

    def start(self):
        try:
            #self.nick = input("Enter your nickname: ")
            #self.password = input("Enter your password: ")
            self.connect()

            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.start()
            self.enviar_p()
            while True:
               pass
                    

        except KeyboardInterrupt:
            print("\nExiting...")
        finally:
            self.sock.close()


print("\x1bc\x1b[43;30mstart application:")

if __name__ == "__main__":
    server_ip = "192.168.1.4"
    server_port = 6667

    irc_bot = IRCBot(server_ip, server_port)
    irc_bot.start()