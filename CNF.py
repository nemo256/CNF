import networkx as nx
import matplotlib.pyplot as plt


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


def plot_decision_tree(satisfiable_solutions, non_satisfiable_solutions):
    """
    Plot the decision tree with color-coded nodes for satisfiable and non-satisfiable solutions.
    """
    G = nx.Graph()
    pos = {}
    color_map = []

    # Add nodes for satisfiable solutions
    for i, solution in enumerate(satisfiable_solutions):
        node_label = f"S{i + 1}"
        G.add_node(node_label)
        pos[node_label] = (i, 1)
        color_map.append('green')

    # Add nodes for non-satisfiable solutions
    for i, solution in enumerate(non_satisfiable_solutions):
        node_label = f"NS{i + 1}"
        G.add_node(node_label)
        pos[node_label] = (i, 0)
        color_map.append('red')

    # Add edges between nodes
    for i in range(min(len(satisfiable_solutions), len(non_satisfiable_solutions))):
        G.add_edge(f"S{i + 1}", f"NS{i + 1}")

    # Plot the decision tree
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=5000, node_color=color_map, font_size=10, font_weight='bold')
    plt.title("Decision Tree")
    plt.show()


# Programme principal
cnf = parse_cnf()  # Analyse de l'expression CNF saisie par l'utilisateur
satisfiable_solutions, non_satisfiable_solutions = solve_binary_cnf(cnf)  # Résolution de l'expression CNF

if satisfiable_solutions:
    print("\033[32mSolutions satisfaisantes: ", len(satisfiable_solutions))
    for solution in satisfiable_solutions:
        print("Affectation :", solution)
else:
    print("\033[31mAucune solution satisfaisante trouvée.")

if non_satisfiable_solutions:
    print("\033[31mSolutions non satisfaisantes: ", len(non_satisfiable_solutions))
    for solution in non_satisfiable_solutions:
        print("Affectation :", solution)

# Plot the decision tree
plot_decision_tree(satisfiable_solutions, non_satisfiable_solutions)
