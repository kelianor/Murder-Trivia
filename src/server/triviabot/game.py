DB_FILE = "../data/users.txt"
import murder_trivia_pb2
users = set()
players = {}
game_started = False

try:
    with open(DB_FILE, "r") as file:
        for line in file:
            cleaned = line.strip()
            if cleaned:
                users.add(int(cleaned))
except FileNotFoundError:
    print("Файл data/users.txt не сущетсвует, ничего не записываем")


def addUser(userID): # True - пользователь добавлен в список, False - пользователь уже сущетсвует
    if userID not in users:
        with open(DB_FILE, "a+") as file:
            users.add(murder_trivia_pb2.PlayerInfo(userID, murder_trivia_pb2.UNSPECIFIED))
            file.write(str(userID) + '\n')
            return True
    else:
         return False