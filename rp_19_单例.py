class MusicPlayer(object):

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        else:
            cls.instance = super().__new__(cls)
            return cls.instance


# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)

player3 = MusicPlayer()
print(player3)
