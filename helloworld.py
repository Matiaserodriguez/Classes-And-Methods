class Hello_World:
    def __init__(self, word1, word2):
        self.__word1 = word1
        self.__word2 = word2

    def hello_world(self):
        print(self.__word1, self.__word2)

if __name__ == '__main__':
    greeting = Hello_World('Hello', 'World')
    greeting.hello_world()