from objects.class_Player import Player
from objects.class_Platform import Platform


def load_level():
    levelFile = open('levels/level1.txt', 'r')
    height = int(levelFile.readline())
    width = int(levelFile.readline())
    print(height, width)
    platforms = []
    player = ""
    y = 0
    for line in levelFile:
        if line[0] != '[' and line[0] != ']':
            for x in range(len(line)):
                if line[x] == '-':
                    platforms.append(Platform(x * width, y * height, width, height))
                if line[x] == 'P':
                    player = Player(x * width, y * height, width, height)
        y += 1
    return [player, platforms]
