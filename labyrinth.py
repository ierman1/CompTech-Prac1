class Cell:
    '''Represents a Cell in a labyrinth'''

    def __init__(self, id_cell, children, isWall):
        self.idC = id_cell
        self.isWall = isWall
        self._children = children

    def __repr__(self):
        return f'{self.idC}'
        #return f'{self.idC}--{self.isWall}--{list(map(lambda x: x.idC, self.getChildren()))}'

    def getChildren(self):
        '''Returns the list of children nodes (neighboring cells to this one, that are not wall)'''
        return list(filter(lambda x: not x.isWall, self._children))

class Labyrinth:
    '''Represents a Labyrinth to implement path-finding algorithms'''

    def __init__(self, num_rows, num_cols, grid, start, end):
        self.nrows = num_rows
        self.ncols = num_cols
        self._grid = grid
        self._start_cell = start
        self._end_cell = end

        #process each cell, assign children
        for row in range(self.nrows):
            for col in range(self.ncols):
                this_cell = (col, row)
                possible_neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                this_children = []
                for neigh in possible_neighbors:
                    neigh_X = this_cell[0] + neigh[0]
                    neigh_Y = this_cell[1] + neigh[1]
                    if neigh_X >= 0 and neigh_X < self.ncols and neigh_Y >= 0 and neigh_Y < self.nrows:
                        this_children.append(self._grid[(neigh_X, neigh_Y)])
                self._grid[this_cell]._children = this_children

    def __repr__(self):
        to_ret_str = ''
        for row in range(self.nrows):
            for col in range(self.ncols):
                this_cell = (col, row)
                the_char = '_'
                if self._grid[this_cell] == self._start_cell:
                    the_char = 'S'
                elif self._grid[this_cell] == self._end_cell:
                    the_char = 'E'
                elif self._grid[this_cell].isWall:
                    the_char = '#'
                to_ret_str += the_char
            to_ret_str += '\n'
        return to_ret_str[:-1]

    def getStartCell(self) -> Cell:
        '''Returns the starting cell'''
        return self._start_cell

    def getEndCell(self) -> Cell:
        '''Returns the goal/exit cell'''
        return self._end_cell

    @classmethod
    def load_from_file(cls, path_to_file):
        '''Load a labyrinth from a file into an instance of the class'''
        with open(path_to_file) as laby:
            start_node, end_node = None, None
            grid = {}
            rows, cols = 0, -1
            for line_idx, line in enumerate(laby):
                the_line = line[:-1] # Avoid newline character
                if cols == -1:
                    cols = len(the_line)
                else:
                    assert cols == len(the_line), f'Line {line_idx + 1} in labyrinth file has a different number of elements than the first line.'
                for id_col, char in enumerate(the_line):
                    id_cell = (id_col, rows)
                    if char == '#': ## WALL
                        grid[id_cell] = Cell(id_cell, None, True)
                    elif char == '_': ## EMPTY
                        grid[id_cell] = Cell(id_cell, None, False)
                    elif char == 'S': ## START
                        if not start_node:
                            grid[id_cell] = Cell(id_cell, None, False)
                            start_node = grid[id_cell]
                        else:
                            raise RuntimeError(f'Only one start cell is allowed.')
                    elif char == 'E': ## END
                        if not end_node:
                            grid[id_cell] = Cell(id_cell, None, False)
                            end_node = grid[id_cell]
                        else:
                            raise RuntimeError(f'Only one end cell is allowed.')
                    else:
                        raise RuntimeError(f'Invalid character {char} found in labyrinth file. Line {line_idx + 1}.')
                rows += 1

        this_labyrinth = cls(rows, cols, grid, start_node, end_node)

        return this_labyrinth
