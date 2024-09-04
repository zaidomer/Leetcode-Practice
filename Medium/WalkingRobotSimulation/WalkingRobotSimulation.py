# https://leetcode.com/problems/walking-robot-simulation/

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        x = 0
        y = 0
        currDir = 0
        obs = set()
        for i in range(len(obstacles)):
            obs.add((obstacles[i][0], obstacles[i][1]))
        dist = 0

        for i in range(len(commands)):
            if commands[i]==-1:
                currDir = (currDir + 1) % 4
            elif commands[i]==-2:
                currDir = (currDir - 1) % 4
            else:
                dx, dy = directions[currDir]
                for j in range(commands[i]):
                    if (x+dx,y+dy) in obs:
                        break
                    x+=dx
                    y+=dy
                dist = max(dist, x**2+y**2)
        return dist
