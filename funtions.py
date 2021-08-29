from random import randint,choice



class Game:

    @staticmethod
    def kaccm(author):
        uzunluk = randint(0, 60)
        msg = ""
        if str(author) == "<@!463688414135451680>":
            return author + " mesaj."
        else:
            bolum = int(uzunluk / 2)
            for i in range(1, bolum + 1):
                msg += "="
            msg = "Ɛ" + msg + ">"
            return str(author).strip('@') + " mesaj " + str(uzunluk) + " cm\n" + msg

    @staticmethod
    def kufret():
        kufur=["...",
               "...",
               "...",
               "...",
               "...",
               "...",
               "...",
               "..."]
        return choice(kufur)