from path_finder import PathFinder

finder = PathFinder("mazes/maze00")
print str(finder.start_state.x) + "," + str(finder.start_state.y)
print str(finder.end_state.x) + "," + str(finder.end_state.y)
print finder.grid
