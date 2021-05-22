import pygame




class Player:
    MARGIN = 50
    def __init__(self, name, age, money=2000):
        self.name = name
        self.age = age
        self.money = money
        self.cards = []
        self.dir = 2
        # self.img


    def __str__(self):
        return f"{self.name} has ${self.money}"

    def checkCards(self):
        if len(self.cards) > 2:
            raise RuntimeError("Player has more than 2 cards")

    # def getMoneyFrom(self, otherPlayer, quantity):
    #     if (otherPlayer.money < quantity):
    #         raise RuntimeError(f"{otherPlayer.__str__()} is {quantity - otherPlayer.money} short")
    #     self.money += quantity
    #     otherPlayer.money -= quantity
    #
    # def giveMoneyTo(self, otherPlayer, quantity):
    #     if (self.money < quantity):
    #         raise RuntimeError(f"{self.__str__()} is {quantity - self.money} short")
    #     otherPlayer.money += quantity
    #     self.money -= quantity

    def assignPosOnScreen(self, dir):
        """
        assigns where each player will be positioned for the gui.
        :param dir: 0:North 1:East 2:South 3:West
        :return: None
        """
        self.dir = dir


    def assignCenter4drawIcon(self, size):
        width, height = size
        if (self.dir == 2): return [width/2 - 20 , height - 80 ]
        elif (self.dir == 1): return [width - 70, height/2]
        elif (self.dir == 3): return [70, height/2]


    def assignCenter4drawName(self, size):
        width, height = size
        if (self.dir == 2): return [width/2, height - 70 - 80]
        elif (self.dir == 1): return [width - 70 - 80 , height/2]
        elif (self.dir == 3): return [70 + 80, height/2]



    def assignCenter4drawCard(self, size):
        width, height = size
        if (self.dir == 2): return [width/2, height - 70 - 100]
        elif (self.dir == 1): return [width - 70 - 100 , height/2]
        elif (self.dir == 3): return [70 + 100, height/2]



    def getAngleRot(self):
        if (self.dir == 1): return -90.0
        elif (self.dir == 2): return 0.0
        elif (self.dir == 3): return 90.0



    def drawIcon(self, screen, size):
        """
            invariant: the r of this circ needs to be smaller than the margin to from the screen
        """
        pygame.draw.circle(screen,
                           (255,255,255),
                           self.assignCenter4drawIcon(size),
                           60,
                           1
                           )
        font = pygame.font.SysFont("Sans", 24)

        user_name_to_be_displayed = font.render(self.name, True, (255,255,255))

        pygame.transform.rotate(user_name_to_be_displayed, self.getAngleRot())



        screen.blit(user_name_to_be_displayed, self.assignCenter4drawName(size))

        # font = pygame.font.SysFont(None, 24)
        #
        # img = font.render(self.name, True, (0, 0, 255))
        #
        # if dir == 0:
        #
        # screen.blit(img, (20, 20))


    # def timed_bet(self):
    #     timer = 10


