from objects.class_Player import Player
from objects.class_Platform import Platform


def load_level():
    levelFile = open('levels/level1.txt', 'r')
    height = int(levelFile.readline())
    width = int(levelFile.readline())
    print(height, width)
    platforms = []
    player = ""
    x = 0
    for line in levelFile:
        if line[0] != '[' and line[0] != ']':
            for i in range(len(line)):
                if line[i] == '-':
                    platforms.append(Platform(x * height, i * width, height, width))
                if line[i] == 'P':
                    player = Player(x * height, i * width, height, width)
        x += 1
    return [player, platforms]
