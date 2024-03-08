# Programme: Résolveur CNF

# Fonction: solve_binary_cnf
# Entrée: CNF (expression CNF sous forme d'une liste de listes)
# Sortie: Liste représentant une affectation satisfaisante des variables ou None si impossible à trouver

def solve_binary_cnf(cnf):
    """
    Résout une expression CNF binaire.
    :param cnf: Expression CNF sous forme d'une liste de listes, chaque liste représentant une clause.
    :return: Liste représentant une affectation satisfaisante des variables ou None si impossible à trouver.
    """
    def is_satisfiable(assignment):
        """
        Vérifie si une affectation satisfait toutes les clauses de l'expression CNF.
        :param assignment: Affectation de variables sous forme d'une liste de valeurs booléennes.
        :return: True si l'affectation satisfait toutes les clauses, False sinon.
        """
        for clause in cnf:
            clause_satisfied = False
            for literal in clause:
                if literal > 0 and assignment[abs(literal)]:
                    clause_satisfied = True
                    break
                elif literal < 0 and not assignment[abs(literal)]:
                    clause_satisfied = True
                    break
            if not clause_satisfied:
                return False
        return True

    def backtrack(assignment, var_index):
        """
        Fonction de rétrogradation utilisée pour rechercher toutes les affectations possibles.
        :param assignment: Affectation de variables sous forme d'une liste de valeurs booléennes.
        :param var_index: Index de la variable à affecter.
        :return: Affectation satisfaisante des variables ou None si aucune solution trouvée.
        """
        if var_index == len(assignment):
            return assignment if is_satisfiable(assignment) else None

        for value in [False, True]:
            assignment[var_index] = value
            result = backtrack(assignment, var_index + 1)
            if result:
                return result

        # Si aucune solution trouvée, rétrogradation
        assignment[var_index] = None
        return None

    # Détermine le nombre de variables dans l'expression CNF
    num_variables = max([abs(literal) for clause in cnf for literal in clause])

    # Ajouter 1 pour tenir compte de l'indexation à partir de 0
    assignment = [None] * (num_variables + 1)
    return backtrack(assignment, 1)


def parse_cnf():
    """
    Analyse une expression CNF saisie par l'utilisateur et la convertit en une liste de listes.
    :return: Expression CNF sous forme d'une liste de listes, chaque liste représentant une clause.
    """
    cnf = []
    print("Entrez les clauses CNF (ligne vide pour terminer)")
    while True:
        clause_str = input("Clause (séparez les littéraux par des espaces) : ")
        if not clause_str.strip():
            break
        clause = [int(literal) for literal in clause_str.split()]
        cnf.append(clause)
    return cnf


# Programme principal
print("Entrez l'expression CNF")
cnf = parse_cnf() # Analyse de l'expression CNF saisie par l'utilisateur
solution = solve_binary_cnf(cnf) # Résolution de l'expression CNF

if solution:
    print("Affectation satisfaisante :", solution)
else:
    print("Impossible de trouver une solution.")

