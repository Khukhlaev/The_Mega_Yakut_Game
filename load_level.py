from objects.class_Player import Player
from objects.class_Platform import Platform
from objects.class_Dog import Dog
from objects.class_Policeman import Policeman


def load_level(level_number):
    """
    Create a level structure using the txt layout
    Args: level number
    """
    level_file = open('levels/level' + str(level_number) + '.txt', 'r')
    platform_height = int(level_file.readline().split()[0])
    platform_width = int(level_file.readline().split()[0])
    player_height = int(level_file.readline().split()[0])
    player_width = int(level_file.readline().split()[0])
    dog_height = int(level_file.readline().split()[0])
    dog_width = int(level_file.readline().split()[0])
    policeman_height = int(level_file.readline().split()[0])
    policeman_width = int(level_file.readline().split()[0])
    platforms = []
    enemies = []
    player = ""
    y = 0
    length = 0
    for line in level_file:
        if line[0] != '[' and line[0] != ']':
            for x in range(len(line)):
                if line[x] == '-':
                    platforms.append(Platform(x * platform_width, y * platform_height, platform_width, platform_height))
                elif line[x] == 'P':
                    player = Player(x * platform_width, y * platform_height, player_width, player_height)
                elif line[x] == 'D':
                    enemies.append(Dog(x * platform_width, y * platform_height, dog_width, dog_height))
                elif line[x] == 'M':
                    enemies.append(Policeman(x * platform_width, y * platform_height,
                                             policeman_width, policeman_height))
                elif line[x] == "|":
                    length = max(length, x)
        else:
            y -= 1
        y += 1
    level_height = y * platform_height
    level_length = length * platform_width
    return [level_length, level_height, player, platforms, enemies]
