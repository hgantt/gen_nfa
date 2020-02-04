# gen_nfa
A small script that generates the LaTeX code for an NFA. 

# Usage
Run `python gen_nfa.py input.txt`. The file `output.txt` will contain the generated LaTeX code.

# Example
The `input.txt` file should contain two lines. The first line contains a semi-colon delimited list of states and the second line contains a semi-colon delimited list of edges. Here is an example `input.txt`: 
```(1, "start", "");(2, "final", "right of=1")
(1, 1, "a,b", "loop above");(1, 2, "a", "above")```
