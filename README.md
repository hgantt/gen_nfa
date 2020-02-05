# gen_nfa
A small script that generates the LaTeX code for an NFA. 

# Usage
Run `python gen_nfa.py input.txt`. The file `output.txt` will contain the generated LaTeX code.

# Example
The `input.txt` file should contain two lines. The first line should be a semi-colon delimited list of states and the second line should be a semi-colon delimited list of edges. Here is an example `input.txt`.
```
    (1, "start", "");(2, "final", "right of=1")
    (1, 1, "a,b", "loop above");(1, 2, "a", "above")
```

The format of the states is `(name, type, options)`. 

The format of the edges is `(starting node, ending node, name, options)`. 

A state that is neither a start state nor a final state should have an empty string as the middle parameter. 

The following is the content of the resulting `output.txt` after running the program.
```
    \title{NFA Buffer}
    \documentclass[12pt]{article}
    \usepackage[english]{babel}
    \usepackage[utf8x]{inputenc}
    \usepackage{amsmath}
    \usepackage{tikz}
    \usetikzlibrary{automata, positioning, arrows}\begin{document}
    \tikzset{->,>=stealth',node distance=3cm,every state/.style={thick,fill=gray!10},initial text=$ $}
    \begin{tikzpicture}
        \node[state, initial, ] (1) {};
        \node[state, accepting, right of=1] (2) {};

        \draw
        (1) edge[loop above] node{a,b} (1)
        (1) edge[above] node{a} (2)
    ;
    \end{tikzpicture}
    \end{document}
```

The resulting NFA looks like this.
![alt text][nfa]
[nfa]: http://github.com/saadiqks/gen_nfa/nfa.png
