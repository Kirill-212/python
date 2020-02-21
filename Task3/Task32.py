class PO:
    name = ""
    lang = ""
    version = ""

    def __init__(self, name, lang, version):
        self.name = name
        self.lang = lang
        self.version = version

    def PrintPO(self):
        print("version->" + self.version + "\nname->" + self.name + "\nlang->" + self.lang)


class Developer:
    nameD = ""
    ageD = 0
    langD = ""

    def __init__(self, name, age, lang):
        self.langD = lang
        self.nameD = name
        self.ageD = age

    def PrintDev(self):
        print("name->" + self.nameD + "\nage->" + str(self.ageD) + "\nlang->" + self.langD)


class TextProcess(PO, Developer):
    nameTextProcess = ""
    typeTextProcess = ""

    def __init__(self, nametextprocess, typetextprocess, name, lang, versionD, nameD, langD, ageD, version):
        PO.__init__(self, name, lang, version), Developer.__init__(self, nameD, ageD, langD)
        if lang == langD:
            self.lang = lang
            self.name = name
            self.version = versionD
            self.ageD = ageD
            self.langD = langD
            self.nameD = nameD
            self.nameTextProcess = nametextprocess
            self.typeTextProcess = typetextprocess
        else:
            print("Разработчик не может программировать на другом языке программирования")
            self.lang = ""
            self.name = ""
            self.version = ""
            self.ageD = ""
            self.langD = ""
            self.nameD = ""
            self.nameTextProcess = ""
            self.typeTextProcess = ""

    def PrintAllInf(self):
        print("*" * 10 + "Dev" + "*" * 10)
        self.PrintDev()
        print("*" * 10 + "Use PO" + "*" * 10)
        self.PrintPO()
        print("*" * 10 + "Create PO" + "*" * 10)
        print("name TextProcess:" + self.nameTextProcess + "\ntype  TextProcess:" + self.typeTextProcess)
        print("*" * 34)


class Word(TextProcess):
    def __init__(self, nametextprocess, typetextprocess, name, lang, versionD, nameD, langD, ageD, version):
        TextProcess.__init__(self, nametextprocess, typetextprocess, name, lang, versionD, nameD, langD, ageD, version)
        self.nameTextProcess = "WORD ULTIMAIT"
        self.typeTextProcess = "super Text PO"


class Game(Developer):
    nameGame = ""
    buy = 0
    Style = ""

    def __init__(self, nameGame, buy, style, name, age, lan):
        Developer.__init__(self, name, age, lan)
        self.nameGame = nameGame
        self.Style = style
        if buy < 0:
            self.buy = (-1) * buy
        else:
            self.buy = buy

    def PrintGame(self):
        print("#" * 20)
        self.PrintDev()
        print("#" * 20)
        print("nameGame->" + self.nameGame + "\n buy->" + str(self.buy) + "\n Style->" + self.Style)
        print("#" * 20)

    def Buyornot(self):
        if self.buy > 100:
            print("may be you don't buy this game")
        else:
            print("Buy this game")


class Virys(Developer):
    ForWhat = ""
    aim = ""
    buy = 0

    def __init__(self, ForWhat, aim, buy, name, age, lan):
        Developer.__init__(self, name, age, lan)
        self.buy = buy
        self.aim = aim
        self.ForWhat = ForWhat

    def Print(self):
        self.PrintDev()
        print("Aim " + self.aim)
        print("buy " + str(self.buy))
        print("ForWhat " + self.ForWhat)

    def popular(self):
        if self.buy > 2000:
            print("is popular")
        else:
            print("this is not popular")


class Saper(Game):
    version = ""

    def __init__(self, version, buy, name, age, lan):
        Game.__init__(self, "Saper", buy, "RPG", name, age, lan)
        self.version = version

    def Print(self):
        self.PrintDev()
        self.PrintGame()
        print("Version game->" + self.version)


d = TextProcess("Word", "TextProcess 1", "Visual Studio 2019", "C++", "1.1", "Alex", "C++", "19", "1.3.4")
d.PrintAllInf()
wor = Word("Word", "TextProcess 1", "Visual Studio 2017", "C#", "1.1", "Make", "C#", 20, "1.3.1")
wor.PrintAllInf()
g = Game("rust", 100, "RPG", "Anton", 10, "Python")
g.Buyornot()
g.PrintGame()
v = Virys("for internet", "Delete internet", 10000, "Alex", 32, "C")
v.Print()
v.popular()

s = Saper("3.2.4", 200, "Make", 30, "C/C++")
s.Print()
