import life

grid= [[0,0,0],[1,1,1],[0,0,0]]

def life(grid, x,y):
    return grid[x][y]==1

def alive_neighbours(grid, x,y,):
    count=0
    for gx in (-1,0,1):
        for gy in (-1,0,1):
            if gx==gy==0:
                continue
            
            nx,ny= x+gx,y+gy
            if nx<0 or ny<0:
                continue
            try:
                count= count+grid[nx][ny]
            except IndexError:
                continue
  return count
def make_alive(grid,x,y):
    grid[x][y]==1

def kill_it(grid,x,y):
    grid[x][y]==0
               
            
            
