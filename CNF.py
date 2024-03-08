def solve_binary_cnf(cnf):
    """
    Résout une expression CNF binaire.
    :param cnf: Expression CNF sous forme d'une liste de listes, chaque liste représentant une clause.
    :return: Liste de toutes les affectations satisfaisantes des variables ou une liste vide si aucune solution trouvée.
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
        :return: Liste de toutes les affectations satisfaisantes des variables ou une liste vide si aucune solution trouvée.
        """
        if var_index == len(assignment):
            if is_satisfiable(assignment):
                satisfiable_solutions.append(assignment.copy())
            else:
                non_satisfiable_solutions.append(assignment.copy())
            return

        for value in [False, True]:
            assignment[var_index] = value
            backtrack(assignment, var_index + 1)

    num_variables = max([abs(literal) for clause in cnf for literal in clause])
    assignment = [None] * (num_variables + 1)
    satisfiable_solutions = []
    non_satisfiable_solutions = []
    backtrack(assignment, 1)
    return satisfiable_solutions, non_satisfiable_solutions


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
cnf = parse_cnf()  # Analyse de l'expression CNF saisie par l'utilisateur
satisfiable_solutions, non_satisfiable_solutions = solve_binary_cnf(cnf)  # Résolution de l'expression CNF

if satisfiable_solutions:
    for solution in satisfiable_solutions:
        print("\033[32mSatisfaisante :", solution)
else:
    print("\033[31mAucune solution satisfaisante trouvée.")

if non_satisfiable_solutions:
    for solution in non_satisfiable_solutions:
        print("\033[31mNon Satisfaisante :", solution)
          
