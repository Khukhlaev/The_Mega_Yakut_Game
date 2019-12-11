from objects.class_Player import Player
from objects.class_Platform import Platform


def load_level(level_number):
    level_file = open('levels/level' + str(level_number) + '.txt', 'r')
    platform_height = int(level_file.readline().split()[0])
    platform_width = int(level_file.readline().split()[0])
    player_height = int(level_file.readline().split()[0])
    player_width = int(level_file.readline().split()[0])
    level_length = platform_width * int(level_file.readline().split()[0])
    platforms = []
    player = ""
    y = 0
    for line in level_file:
        if line[0] != '[' and line[0] != ']':
            for x in range(len(line)):
                if line[x] == '-':
                    platforms.append(Platform(x * platform_width, y * platform_height, platform_width, platform_height))
                if line[x] == 'P':
                    player = Player(x * platform_width, y * player_height, player_width, player_height)
        else:
            y -= 1
        y += 1
    return [level_length, player, platforms]
