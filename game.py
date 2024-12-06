# step3 : show tree, move tree
import pygame
import sys

pygame.init()
pygame.display.set_caption('Jumping dino')
MAX_WIDTH = 800
MAX_HEIGHT = 400


def main():
    # set screen, fps
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    # dog
    imgdog1 = pygame.image.load('dogwalk1.png')
    imgdog2 = pygame.image.load('dogwalk2.png')
    dog_height = imgdog1.get_size()[1]
    dog_bottom = MAX_HEIGHT - dog_height
    dog_x = 50
    dog_y = dog_bottom
    jump_top = 200
    leg_swap = True
    is_bottom = True
    is_go_up = False
    jump_speed=12
    gravity=1

    # tree
    imgTree = pygame.image.load('tree.png')
    tree_height = imgTree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGHT - tree_height

    while True:
        screen.fill((255, 255, 255))

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if is_bottom:
                    is_go_up = True
                    is_bottom = False

        # dog move
        if is_go_up:
            dog_y -= 4.0
        elif not is_go_up and not is_bottom:
            dog_y += 4.0

        if is_go_up:
            jump_speed -= gravity
            dog_y -= jump_speed
            if jump_speed <= 0:
                is_go_up = False
        else:
            jump_speed += gravity  # 하강 속도 점점 증가
            dog_y += jump_speed

        if dog_y >= dog_bottom:
            dog_y = dog_bottom
            is_bottom = True
            jump_speed = 12 

        # dog top and bottom check
        if is_go_up and dog_y <= jump_top:
            is_go_up = False

        if not is_bottom and dog_y >= dog_bottom:
            is_bottom = True
            dog_y = dog_bottom

        # tree move
        tree_x -= 12.0
        if tree_x <= 0:
            tree_x = MAX_WIDTH

        # draw tree
        screen.blit(imgTree, (tree_x, tree_y))

        # draw dino
        if leg_swap:
            screen.blit(imgdog1, (dog_x, dog_y))
            leg_swap = False
        else:
            screen.blit(imgdog2, (dog_x, dog_y))
            leg_swap = True

        # update
        pygame.display.update()
        fps.tick(20)


if __name__ == '__main__':
    main()