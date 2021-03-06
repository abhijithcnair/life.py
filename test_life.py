import life

def test_life():
	grid=[[0,0,0],[1,1,1],[0,0,0]]
	assert life.life( grid,0,0)==False
def test_alive_neighbours():
	grid= [[0,1,0],
	       [0,1,1],
	       [0,0,0]]
        
        assert life.alive_neighbours(grid,0,0)==2
        assert life.alive_neighbours(grid,0,1)==2
        assert life.alive_neighbours(grid,0,2)==3
        assert life.alive_neighbours(grid,1,0)==2
        assert life.alive_neighbours(grid,1,1)==2
        assert life.alive_neighbours(grid,1,2)==2
        assert life.alive_neighbours(grid,2,0)==1
        assert life.alive_neighbours(grid,2,1)==2
        assert life.alive_neighbours(grid,2,2)==2

def test_make_alive():
        grid= [[0,1,0],
	       [0,1,1],
	       [0,0,0]]
        if life.make_alive(grid,0,0):
                
                assert grid[0][0]==1

def test_kill_it():
        grid= [[0,1,0],
	       [0,1,1],
	       [0,0,0]]
        if life.kill_it(grid,0,0):
                assert grid[0][0]==0
        
        
        
        
        
        

        
        

