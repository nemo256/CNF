import networkx as nx
import matplotlib.pyplot as plt

filename = 'clauses.txt'

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
                if literal > 0 and assignment[literal]:
                    clause_satisfied = True
                    break
                elif literal < 0 and not assignment[-literal]:
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
                satisfiable_solutions.append(assignment[1:].copy())  # Skip the first variable (x0)
            else:
                non_satisfiable_solutions.append(assignment[1:].copy())  # Skip the first variable (x0)
            return

        for value in [False, True]:
            assignment[var_index] = value
            backtrack(assignment, var_index + 1)

    num_variables = max([abs(literal) for clause in cnf for literal in clause])
    assignment = [None] * (num_variables + 1)
    satisfiable_solutions = []
    non_satisfiable_solutions = []
    backtrack(assignment, 1)  # Start indexing from 1
    return satisfiable_solutions, non_satisfiable_solutions

def parse_cnf_from_file(filename):
    """
    Parse CNF expressions from a text file.
    :param filename: Name of the text file containing CNF expressions.
    :return: List of CNF expressions, each expression represented as a list of clauses.
    """
    cnf = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # If the line is not empty
                literals = []
                for literal in line.split():
                    try:
                        literals.append(int(literal))
                    except ValueError:
                        pass  # Skip non-integer literals
                cnf.append(literals)
    return cnf

# Programme principal
cnf = parse_cnf_from_file(filename)
satisfiable_solutions, non_satisfiable_solutions = solve_binary_cnf(cnf)  # Résolution de l'expression CNF

if satisfiable_solutions:
    print("\033[32mSolutions satisfaisantes: ", len(satisfiable_solutions))
    for solution in satisfiable_solutions:
        print("Affectation :", solution)
else:
    print("\033[31mAucune solution satisfaisante trouvée.")

# if non_satisfiable_solutions:
#     print("\033[31mSolutions non satisfaisantes: ", len(non_satisfiable_solutions))
#     for solution in non_satisfiable_solutions:
#         print("Affectation :", solution)

