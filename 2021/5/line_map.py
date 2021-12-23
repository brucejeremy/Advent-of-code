

class Point:

    def __init__(self, x: int, y: int ):
        self.x = x
        self.y = y

class Line:

    def __init__(self, p1: Point, p2: Point ):
        self.start = p1
        self.end = p2
        self.getPoints()

    def getPoints(self):
        self.points = []
        self.isDiag = False
        if self.start.x == self.end.x:
            step = 1 if self.end.y > self.start.y else -1
            for y in range(self.start.y, self.end.y+step, step):
                self.points.append(Point(self.start.x, y))
        elif self.start.y == self.end.y:
            step = 1 if self.end.x > self.start.x else -1
            for x in range(self.start.x, self.end.x+step, step):
                self.points.append(Point(x, self.start.y))
        else: # diagonal
            self.isDiag = True
            stepX = 1 if self.end.x > self.start.x else -1
            stepY = 1 if self.end.y > self.start.y else -1
            for i, x in enumerate( range(self.start.x, self.end.x+stepX, stepX) ):
                self.points.append(Point(x, self.start.y + stepY * i))

lines = []
with open('lines.txt', 'r') as dots:

    for line in dots.readlines():
        p1, p2 = line.split('->')
        x1, y1 = [int(coord.strip()) for coord in p1.split(',')]
        x2, y2 = [int(coord.strip()) for coord in p2.split(',')]
        lines.append(Line( Point(x1,y1), Point(x2,y2) ) )

def getBlankGrid():
    grid = []
    for _ in range(1000):
        grid.append([0 for _ in range(1000)])
    return grid

grid = getBlankGrid()
for line in lines:
    if not line.isDiag:
        for point in line.points:
            grid[point.x][point.y] += 1

print('Part one:')
count2 = 0
for row in grid:
    for num in row:
        if num >= 2: count2 += 1
print(f'There are {count2} points greater than 2 on horizontal or vertical lines')

grid = getBlankGrid()
for line in lines:
    for point in line.points:
        grid[point.x][point.y] += 1

print('\nPart two:')
count2 = 0
for row in grid:
    for num in row:
        if num >= 2: count2 += 1
print(f'There are {count2} points greater than 2 on all lines')