import pygame
from pygame import mixer
import random
import math
from helpers import human_player, computer_player, ball
import time

def diffChoice(click) -> str:
    if (250 <= click[1] <= 350):
        if (150 <= click[0] <= 300):
            return 'easy'
        elif (325 <= click[0] <= 475):
            return "medium"
        elif (500 <= click[0] <= 650):
            return "hard"
    return None

def gameOver(winner):
    exit = False

    # rendering win or lose text
    if winner == 'left':
        game_over_text = header.render("You Lose!", True, (255, 255, 255))
    else:
        game_over_text = header.render("You Win!", True, (255, 255, 255))

    l_score = header.render(str(left_score), True, (255, 255, 255))
    r_score = header.render(str(right_score), True, (255, 255, 255))

    while not exit:
        screen.fill((0, 0, 0))
        screen.blit(game_over_text, (270, 150))
        screen.blit(l_score, (250, 350))
        screen.blit(r_score, (480, 350))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        pygame.display.update()

def menu() -> int:

    screen.fill((0, 0, 0))

    # redering text using font 

    # Mode choices
    solo = font.render("Play", True, (255, 255, 255))
    watch = font.render("Automatic", True, (255, 255, 255))
    modeChoiceLineOne = text.render("Choose 'Play' to play against a computer opponent", True, (255, 255, 255))
    modeChoiceLineTwo = text.render("or choose 'Automatic' to watch the computer play against itself", True, (255, 255, 255))

    # Header and rules text
    head = header.render("PyPong: By Alfred", True, (255, 255, 255))
    rulesLineOne = text.render("Move around using the up and down arrow keys, you'll always be on the right!", True, (255, 255, 255))
    rulesLineTwo = text.render("The goal is to hit the ball behind the other paddle. First to 10 points wins!", True, (255, 255, 255))
    rulesLineThree = text.render("Press any key to continue...", True, (255, 255, 255))

    # Difficulties
    ease = font.render("EASY", True, (255, 255, 255))
    med = font.render("MEDIUM", True, (255, 255, 255))
    har = font.render("HARD", True, (255, 255, 255))

    # creating rectangles for mode choices
    buttonOne = pygame.Rect(200, 225, 190, 150)
    buttonTwo = pygame.Rect(410, 225, 190, 150)

    # creating rectangles for difficulty choice
    easy_button = pygame.Rect(150, 250, 150, 100)
    med_button = pygame.Rect(325, 250, 150, 100)
    hard_button = pygame.Rect(500, 250, 150, 100)


    # diff: marks if difficulty has been chosen, defaults to '' if nothing is chosen
    diff = None
    # auto: marks the mode that the user has selected: true -> no players, false -> 1 player, None -> no selection
    auto = None
    # running: true when menu should keep running, false when menu is terminated
    running = True

    # loops until button is pressed
    while running:
        # filling screen
        screen.fill((0, 0, 0))
        
        # displaying header
        screen.blit(head, (150, 30))

        if auto == None:
            # placing button frames onto screen
            pygame.draw.rect(screen, (21, 21, 21), buttonOne)
            pygame.draw.rect(screen, (21, 21, 21), buttonTwo)

            # placing text onto screen
            screen.blit(solo, (480, 285))
            screen.blit(watch, (240, 285))
            screen.blit(modeChoiceLineOne, (100, 120))
            screen.blit(modeChoiceLineTwo, (100, 150))

        elif diff == None:
            # drawing button frames onto screen
            pygame.draw.rect(screen, (21, 21, 21), easy_button)
            pygame.draw.rect(screen, (21, 21, 21), med_button)
            pygame.draw.rect(screen, (21, 21, 21), hard_button)

            # placing text onto screen
            screen.blit(ease, (175, 290))
            screen.blit(med, (345, 290))
            screen.blit(har, (525, 290))

        else:
            screen.blit(rulesLineOne, (30, 120))
            screen.blit(rulesLineTwo, (30, 150))
            screen.blit(rulesLineThree, (30, 180))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                # getting mouse position during left click
                click = pygame.mouse.get_pos()

                # if still at first screen
                if auto == None:
                    if (200 <= click[0] <= 390) and (225 <= click[1] <= 375):
                        auto = True
                    elif (410 <= click[0] <= 600) and (225 <= click[1] <= 375):
                        auto = False

                # if at difficulty choice
                elif diff == None:
                    diff = diffChoice(click)

            # closes the menu if any key is pressed after all 
            # selections are made 
            if event.type == pygame.KEYDOWN:
                if auto != None and diff != None:
                    running = False


        pygame.display.update()

    return auto, diff



def game(setting):
    # declaring globals
    global left_score  
    global right_score 

    running = True
    while running:
        screen.fill((0, 0, 0))
        
        # rendering scoreboards
        l_score_board = font.render("Score: " + str(left_score), True, (255, 255, 255))
        r_score_board = font.render("Score: " + str(right_score), True, (255, 255, 255))

        # placing scoreboards
        screen.blit(l_score_board, (10, 10))
        screen.blit(r_score_board, (700, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return None

            if event.type == pygame.KEYDOWN:
                if not setting:
                    charTwo.move(event)

            if event.type == pygame.KEYUP:
                if not setting:
                    charTwo.stop()


        charOne.draw(screen)
        charTwo.draw(screen)
        ball.draw(screen)

        # checking for collisions
        if 39 < ball.x < 43:
            charOne.isCollision(ball)
        if 734 < ball.x < 738:
            charTwo.isCollision(ball)

        # moving players
        charOne.move(ball)
        if setting:
            charTwo.move(ball)
        else:
            charTwo.y += charTwo.vector
            charTwo.bound()

        # checking for vertical bounces
        ball.vBounce()
        # moving ball
        ball.move()

        # checking to see if ball is out of bounds
        out = ball.reset()
        # updating scores
        if out == 1:
            left_score += 1
            time.sleep(1)
        elif out == 2:
            right_score += 1
            time.sleep(1)

        if left_score >= 10 or right_score >= 10:
            running = False

        pygame.display.update()

    return 'left' if left_score >= 10 else 'right'

if __name__ == '__main__':

    
    # global variables to store the score
    left_score = 0
    right_score = 0

    # Initializing pygame and mixer
    pygame.init()
    mixer.init()
    # creating display
    screen = pygame.display.set_mode((800, 600))

    # putting on music
    bg_channel = mixer.Channel(1)
    bg_music = mixer.Sound("assets/Coldplay - Viva la Vida [Official Instrumental].mp3")
    bg_channel.set_volume(0.333)
    bg_channel.play(bg_music, -1)

    # Create fonts for rendering text
    font = pygame.font.SysFont('comicsans', 32)
    header = pygame.font.SysFont('Lato', 60)
    text = pygame.font.SysFont('Lato', 22)

    # getting values for the setting and the mode
    setting, mode = menu()

    # Initializing characters and ball according to settings and mode

    ball = ball.Ball(400, 300, [
                     random.choice([0.25, -0.25]) / 3, 
                     random.choice([0.25, 0.20, 0.15, 0.10, -0.10, -0.15, -0.20, -0.25]) / 3])
    charOne = computer_player.ComputerPlayer(40, 250, mode)

    if setting == True:
        charTwo = computer_player.ComputerPlayer(735, 250, mode)
    else:
        charTwo = human_player.HumanPlayer(735, 250)

    winner = game(setting)
    if winner != None:
        gameOver(winner)


