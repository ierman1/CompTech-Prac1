from labyrinth import Labyrinth, Cell

def keepSearching(c:Cell, lab:Labyrinth, trail, visited):

    ''' A mesura que accedim a aquesta funció, s'afegeix al trail la cel·la actual. '''
    trail.append(c)

    if c == lab.getEndCell():
        return trail


    '''
        Una vegada afegida, accedim a la primera cel·la veína que no hagi sigut visitada "X"
        i executem un altre cop la funció prenent com a cel·la actual "X".
    '''
    for child in c.getChildren():
        if child not in visited:
            visited.append(child) 
            return keepSearching(child, lab, trail, visited)
    
    '''
        En el moment en que trobem una cel·la que no té d'altres cel·les veínes no visitades,
        sortim del bucle i executem la funció, prenent com a cel·la actual el pare de l'anterior,
        fent així "backtracking".
    '''
    return keepSearching(trail[-2], lab, trail[:-2], visited)

#recursiu
def DFS(lab:Labyrinth):
    print('Starting DFS')
    return keepSearching(lab.getStartCell(), lab, [], [])

#iteratiu
def BFS(lab:Labyrinth):
    print('Starting BFS')

    trail = []
    visited = []
    pending = []
    
    pending.append([lab.getStartCell()])
    visited.append(lab.getStartCell())

    '''
        Gestionem la pila (pending) i l'anem omplint amb les pròximes cel·les
        a visitar. A la vegada les afegim a la llista de visitades per no repetir-les.
        El format de la pila de pendents és una array d'arrays, amb els camins
        necessaris per arribar a la cel·la de l'última posició.
    '''
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
