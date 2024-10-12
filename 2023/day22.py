from collections import deque

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    @staticmethod
    def range_intersects(p1, p2):
        return max(p1[0], p2[0]) <= min(p1[1], p2[1])

class Brick:
    def __init__(self, p1, p2):
        #p1 -> bottom left
        #p2 -> top right
        self.p1 = p1
        self.p2 = p2
        
    def __str__(self):
        return f"(P1: {str(self.p1)}, P2: {str(self.p2)})"

    def drop(self, n):
        dist_dropped = self.p2.z - n
        self.p2.z -= dist_dropped
        self.p1.z = n

    def min_coord(self, key):
        match key:
            case 'x':
                return self.p2 if self.p2.x < self.p1.x else self.p1
            case 'y':
                return self.p2 if self.p2.y < self.p1.y else self.p1
            case 'z':
                return self.p2 if self.p2.z < self.p1.z else self.p1

    def max_coord(self, key):
        match key:
            case 'x':
                return self.p2 if self.p2.x > self.p1.x else self.p1
            case 'y':
                return self.p2 if self.p2.y > self.p1.y else self.p1
            case 'z':
                return self.p2 if self.p2.z > self.p1.z else self.p1

    def do_overlap(self, other):
        return not (self.p2.x < other.p1.x
                or self.p1.x > other.p2.x
                or self.p2.y < other.p1.y
                or self.p1.y > other.p2.y)

def parse_brick(line):
    points = []
    for coord in line.split('~'):
        x,y,z = [ int(n) for n in coord.split(',') ]
        points.append( Point(x,y,z))
    return Brick(points[0], points[1])

def drop_bricks(bricks):
    bricks.sort(key= lambda x : x.min_coord('z').z)

    for i, current_brick in enumerate(bricks):
        new_z = 1
        for dropped_brick in bricks[:i]:
            if current_brick.do_overlap(dropped_brick):
                new_z = max(new_z, dropped_brick.p2.z + 1)
        current_brick.drop(new_z)
        
    bricks.sort(key= lambda x : x.min_coord('z').z)

def is_sole_supporter(supporter, dependent, supports, depends):
    return len(depends[dependent]) == 1 and depends[dependent][0] == supporter
    
def get_total_disintegrated(supports, depends):
    fallen = 0
    for current_brick in range(len(supports)):
        q = deque()
        fell = set()
        fell.add(current_brick)
        
        for dependent in supports[current_brick]:
            if is_sole_supporter(current_brick, dependent, supports, depends):
                q.append(dependent)
                
        while q:
            brick = q.popleft()
            fell.add(brick)
            fallen += 1
            for dependent in supports[brick]:
                if all( [d in fell for d in depends[dependent]] ) and dependent not in fell:
                    q.append(dependent)
    return fallen
        
def process_lines(lines):
    bricks = [parse_brick(line) for line in lines]
    drop_bricks(bricks)
    
    supports = [[] for i in range(len(bricks))]
    depends =  [[] for i in range(len(bricks))]
    for i, brick in enumerate(bricks):
        for j in range(i+1, len(bricks)):
            above_brick = bricks[j]
            if brick.do_overlap(above_brick) and above_brick.p1.z == (brick.p2.z + 1):
                supports[i].append(j)
                depends[j].append(i)

    disintegrated = set()
    for i, support in enumerate(supports):
        for j in support:
            if len(depends[j]) == 1:
                break
        else:
            disintegrated.add(i)
    print('total: ', len(disintegrated))
    print(get_total_disintegrated(supports, depends))

            
def main():
    with open("input/input_22_small.txt") as f:
        lines = [line.strip('\n') for line in f.readlines()]
        process_lines(lines)

if __name__ == "__main__":
    main()
