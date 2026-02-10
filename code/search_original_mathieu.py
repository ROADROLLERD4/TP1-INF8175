# ============================================================================
# SAUVEGARDE DU CODE ORIGINAL DE MATHIEU - depthFirstSearch
# Date: 21 janvier 2026
# ============================================================================

def depthFirstSearch(problem):
    """
    Version originale avec mes commentaires d'apprentissage.
    """
    currentState = None
    parent = {}
    initialState = problem.getStartState() 
    listFringe = util.Stack()
    listExplored = []

    listFringe.push((initialState, None, None))
    parent[initialState] = None
    
    while not listFringe.isEmpty():
        #utiliser seulemetn pour la sortie si nous trouvons une solution
        path = []
        #prendre le prochain etat dans la li parent[initialState] = Noneste fringe
        newState = listFringe.pop()

        #ajouter le parent qui nous a conduit a cet etat et mettre newState comme etat courant
        if currentState is not None:
            parent[newState[0]] = (currentState[0], newState[1]) # on mt newState[1] car la position parent a choise la position de newstate pour y arrvier
        currentState = newState

        #ajouter le nouvel etat dans la memoire pour ne pas revenir dessus
        listExplored.append(currentState[0])

        #verifier si l'etat est final
        if problem.isGoalState(currentState[0]):
            path.append(currentState[1])
            while currentState[0] != initialState: 
                currentState = parent[currentState[0]]
                path.append(currentState[1])
            path.reverse()
            return path
        else:
            successorsList = problem.getSuccessors(currentState[0]) #la fonction prends une position alors currentState[0[]]
            for node in successorsList: #liste de tuples (successor, action, stepCost)
                if node[0] not in listExplored :
                    listFringe.push(node)
    return []
