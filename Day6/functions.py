from fontTools.misc.cython import returns


def step(step_number):
    print(f"Step {step_number}: Stepping forward")


def rest(step_number):
    print(f"Step{step_number}: Resting...")


for steps in range(1, 7):
    step(steps)
    if steps % 3 == 0:
        rest(steps)

maze = ['R', '.', '#', '.', '.', '#', '.', 'G']
robot_pos = 0
"""maze as a row of boxes with items inside
robot_pos as a number telling you which box the robot is standing at
Even though they are separate — you can say:
“Go to the box with index robot_pos and change it.”
Because the robot’s position tells you which box to act on 
and that’s the magic of using variables together."""
def move():
    global robot_pos
    maze[robot_pos] = '.'
    robot_pos += 1
    if robot_pos < len(maze):
        maze[robot_pos] = 'R'

move()
print(maze)
print("Robot is at index:", robot_pos)

def jump():
    global robot_pos
    maze[robot_pos] = '.'
    robot_pos += 2
    if robot_pos < len(maze):
        maze[robot_pos] = 'R'

jump()
print(maze)
print("Robot is at index:", robot_pos)

def wall_in_front():
    if robot_pos + 1 >= len(maze):
        return False
    elif maze[robot_pos + 1] == '#':
        return True
    else:
        return False


while robot_pos < len(maze) and maze[robot_pos] != 'G':
    if wall_in_front():
        jump()
    else:
        move()

print(maze)
print("Robot is at index:", robot_pos)


class Solution(object):
    def subtractProductAndSum(self, n):
        product = 1
        total_sum = 0

        while n > 0:
            digit = n % 10
            product *= digit
            total_sum += digit
            n //= 10

        return product - total_sum

result = Solution()
print(result.subtractProductAndSum(234))

