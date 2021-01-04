import sys
from ast import literal_eval as make_tuple

def tuple_to_matrix(s):
    return f"$\\begin{{matrix}}\n{s[0]} \\\\ \n{s[1]}\n \\end{{matrix}}$"

# Adding intro stuff to NFA file
doc_latex = "\\title{NFA Buffer}\n\\documentclass[12pt]{article}\n"
doc_latex += "\\usepackage[english]{babel}\n\\usepackage[utf8x]{inputenc}\n"
doc_latex += "\\usepackage{amsmath}\n\\usepackage{tikz}\n"
doc_latex += "\\usetikzlibrary{automata, positioning, arrows}"

doc_latex += "\\begin{document}\n\\tikzset{->, >=stealth', node distance=3cm,"
doc_latex += "every state/.style={thick, fill=gray!10}, initial text=$ $}\n\\begin{tikzpicture}\n"

# Reading file
f = open(str(sys.argv[1]), "r")

lines = f.readlines()

wsos = "*" in lines[1]

states = lines[0][:-1].split(";")
states = list(map(lambda x: make_tuple(x), states))

edges = lines[1][:-1].split(";")
edges = list(map(lambda x: make_tuple(x), edges))

f.close()

# Every state is of the form (name, type, options)
# Every edge is of the form (from, to, symbol, options)

# Adding states 
nfa_string = ""

for state in states:
    if state[1] == "":
        nfa_string += f"\t\\node[state, {state[2]}] ({state[0]}) {{}};\n"
    elif state[1] == "start":
        nfa_string += f"\t\\node[state, initial, {state[2]}] ({state[0]}) {{}};\n"
    elif state[1] == "final":
        nfa_string += f"\t\\node[state, accepting, {state[2]}] ({state[0]}) {{}};\n"
    elif state[1] == "start, final":
        nfa_string += f"\t\\node[state, initial, accepting, {state[2]}] ({state[0]}) {{}};\n"

nfa_string += "\n\t\\draw\n"

# Adding edges
for edge in edges:
    if wsos:
        e = tuple_to_matrix(edge[2])
        nfa_string += f"\t({edge[0]}) edge[{edge[3]}] node" + "{" + e + "}" + f" ({edge[1]})\n"
    else:
        nfa_string += f"\t({edge[0]}) edge[{edge[3]}] node" + "{$" + edge[2] + "$}" + f" ({edge[1]})\n"

nfa_string += ";\n"

doc_latex += nfa_string
doc_latex += "\\end{tikzpicture}\n\\end{document}\n"

f = open("output.tex", "w")
f.write(doc_latex)
f.close()
