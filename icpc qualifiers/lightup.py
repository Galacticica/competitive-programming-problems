size = int(input())
array = []





def adjBulb( x,  y, grigri, grid):
    bulbCount = 0
    if(x+1<=size):    
        if (grid[x+1][y] == '?'):
            bulbCount += 1
    if(y+1<=size):    
        if (grid[x][y+1] == '?'):
            bulbCount += 1
    if(x-1<0):    
        if (grid[x-1][y] == '?'):
            bulbCount += 1
    if(x+1<0):    
        if (grid[x][y-1] == '?'):
            bulbCount += 1
        
    if (bulbCount != grigri):
        print(0)
        exit(0)




def findBulb(x, y, dir, grid):














for i in range(size):
    row = input()
    array.append(row)


for i in range (size):
    for j in range (size):
        grid = str(array[i][j])
        #if is wall or bulb
        if (grid == 'X' or grid == '?'):
            pass
        
        elif(grid== '.'):
            findBulb(i,j,'n', array)
            

        elif (grid.isnumeric()):
            adjBulb(i,j, grid, array)




print(1)