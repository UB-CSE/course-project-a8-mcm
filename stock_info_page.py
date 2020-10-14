import pygame
from pygame.locals import *
from Search import *
from webscrape import *

"""
@Authors: Musaiyab Ali, David Forrest, Sean Brasse
The class that displays stock information when a stock is clicked on. This will mimic
the favorites menu, but will display the line graph and company name
"""


class InfoPage:
    # default sizes for screen resolution
    screenWid = 1280
    screenLen = 720

    # checker variables to keep track of states
    insearchbar = 0
    hamState = 0

    # the text the user is inputing into the search bar
    searchbarText = ""

    # Empty time string
    updatedTimeText = ""

    # Empty company name
    companyInitials = ""

    # Company name
    companyName = ""

    def infoPgInit(self):

        pygame.init()

        # name of the screen
        pygame.display.set_caption('MCM')

        # width then Height
        screen = pygame.display.set_mode((self.screenWid, self.screenLen))

        # background image
        fillerImag = pygame.image.load(
            "../course-project-a8-mcm/images/homepageFiles/Background base.png")

        # menu button
        hamburgermenu = pygame.image.load(
            "../course-project-a8-mcm/images/homepageFiles/HamburgerMenu.png")

        # search bar box
        searchbar = pygame.image.load(
            "../course-project-a8-mcm/images/homepageFiles/SearchBar.png")

        # back button
        backButton = pygame.image.load(
            "../course-project-a8-mcm/images/homepageFiles/back2.png")

        # button and font for search bar
        searchBarButton, searchBarFont, updatedTime, timeFont, companyFont = searchBarInitalize()

        # favorites menu
        # favMenu = pygame.image.load(
        #     "../course-project-a8-mcm/images/homepageFiles/favorites_background.png")

        # screen while program is running
        while True:
            # clears the screen
            screen.fill(0)

            # renders all of the hidden buttons
            pygame.draw.rect(screen, [0, 0, 0], searchBarButton)

            # renders background and menu buttons
            screen.blit(fillerImag, (0, 0))
            screen.blit(searchbar, (0, 0))
            screen.blit(hamburgermenu, (0, 0))
            screen.blit(backButton, (15, 675))

            # render search bar text
            searchtext = searchBarFont.render(
                self.searchbarText, True, [0, 0, 0])
            screen.blit(searchtext, (200, 15))

            # #render Company Name
            compName = companyFont.render(
                self.companyName, True, [255, 255, 255])

            # if self.hamState == 1:
            #     screen.blit(favMenu, (0, 0))

            # render hidden buttons
            hamHidden = pygame.Rect(0, 0, 100, 100)

            # render updated time text
            timeText = timeFont.render(
                self.updatedTimeText, True, [255, 255, 255])
            screen.blit(timeText, (875, 670))
            # )

            # renders line graph box
            lineGraphBox = pygame.Rect(300, 300, 700, 300)
            pygame.draw.rect(screen, [255, 255, 255], lineGraphBox)

            # updates the screen
            screen.blit(compName, (450, 200))
            pygame.display.update()

            # event handler loop
            for event in pygame.event.get():
                # clicking X on window
                if event.type == pygame.QUIT:
                    print("Exiting Window")
                    pygame.quit()
                    exit(0)

                # if user clicked hamburger icon
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if hamHidden.collidepoint(event.pos):
                        if self.hamState == 0:
                            self.hamState = 1
                        else:
                            self.hamState = 0

                # whether user clicked into search bar
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if searchBarButton.collidepoint(event.pos):
                        self.insearchbar = 1
                    else:
                        self.insearchbar = 0

                # if user typed into search bar
                if event.type == pygame.KEYDOWN and self.insearchbar == 1:
                    if event.unicode == "\r":
                        if search(self.searchbarText):
                            temp = get_url(self.searchbarText)
                            self.companyName = get_company_name(temp)
                            self.searchbarText = ""
                            self.updatedTimeText = timeStamp()
                    else:
                        self.searchbarText = updateSearchBarOnKeyPress(
                            event, self.searchbarText)


# calls the method to run the program
test = InfoPage()
test.infoPgInit()
