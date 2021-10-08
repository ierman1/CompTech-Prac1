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
    pending.append([lab.getStartCell()])
    visited.append(lab.getStartCell())

    while len(pending) != 0:

        tmp = pending.pop(0)

        if (tmp[-1] == lab.getEndCell()):
            trail = tmp
            break

        for c in tmp[-1].getChildren():
            if c not in visited:
                pending.append(tmp + [c])
                visited.append(c)

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
