from labyrinth import Labyrinth

#recursiu
def DFS(lab:Labyrinth):
    print('Starting DFS')
    trail = []

    #TODO

    return trail

#iteratiu
def BFS(lab:Labyrinth):
    print('Starting BFS')
    trail = []
    visited = []
    pending = [] 
    
    #TODO
    pending.append(lab.getStartCell())      # pending = [(1,1)]

    while len(pending) != 0:
        
        # =================== DEBUG =================== #
        print("\n======\nChecking => " + pending[0].__repr__() + "\nPending at the start => ", end = '')
        for p in pending:
            print(p.__repr__() + " ", end = '')
        # =================== DEBUG =================== #

        '''
            1. - Guardem la primera posició de la llista de pendents i l'eliminem de la llista
            2. - Iterem per les caselles veínes, i si són vàlides, les desem a pendents
        '''

        tmp = pending[0]                    # tmp = [(1,1)] => [(1,2)]
        visited.append(pending[0])          # visited = [(1,1)] => [(1,1), (1,2)]
        pending = pending[1:]               # pending = [] => [(2,1)]

        for c in tmp.getChildren():
            if c not in visited:
                pending.append(c)           # pending = [(1,2), (2,1)] => [(2,1),(1,3)]

        # =================== DEBUG =================== #
        print("\nPending at the end => ", end = '')
        for p in pending:
            print(p.__repr__() + " ", end = '')
        # =================== DEBUG =================== #

    return trail

if __name__ == '__main__':
    algo_choices = ['BFS', 'DFS']
    algo_funcs = [BFS, DFS]

    import argparse
    argp = argparse.ArgumentParser()
    argp.add_argument('labyrinth_file')
    argp.add_argument('algo', choices=algo_choices)

    args = argp.parse_args()
    laby = Labyrinth.load_from_file(args.labyrinth_file)
    print(laby)
    result_trail = algo_funcs[algo_choices.index(args.algo)](laby)
    if result_trail:
        print(f'{args.algo} found solution that has {len(result_trail)} steps:')
        print(result_trail)
