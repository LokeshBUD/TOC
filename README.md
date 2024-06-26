# TOC
#                                         TOC PROJECT

|      Name          | Roll Number       |   Contribution                                                   |
|--------------------|-------------------|------------------------------------------------------------------|
| Karthik Krishna    | CB.EN.U4CSE22024  |  2nd type of implementation (TOC FOLDER)                         |
| Lokesh Budda       | CB.EN.U4CSE22026  |  implementation using libraries (NFAtoDFA file)                  |
| Shrish Kumar       | CB.EN.U4CSE22048  |  2nd type of implementation (TOC FOLDER)                         |
| Sai Keerthana      | CB.EN.U4CSE22050  |  implementation using libraries (NFAtoDFA file) & documentation  |
| Senthil Adithya    | CB.EN.U4CSE22054  |  implementation using libraries (NFAtoDFA file)                  |


There are two different implementations.
One is by using the Python libraries(NFAtoDFA file) and the other is by using the logic(TOC FOLDER).

# Libraries we used:

<small><strong>1. Visual Automata:</strong></small>
Visual Automata is a Python 3 library built as a wrapper for the Automata library to add more visualization features.

[Link to the Documentation for Visual Automata](https://pypi.org/project/visual-automata/)

# Example of Visual_automata
<small><strong>Define a visual_automata DFA that can accept any string ending with 01:</strong></small>

```python
new_dfa = VisualDFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'}
)
```


<small><strong>new_dfa.table:</strong></small>
```
       0    1

 →q0  q0  *q1

 *q1  q0   q2

 q2   q2  *q1
 ```
new_dfa.show_diagram()

![](https://github.com/LokeshBUD/TOC/blob/main/state.jpeg)

<small><strong>2. visual_automata.fa.dfa:</strong></small>
This module specifically imports the VisualDFA class from the visual_automata library, which is used to create and visualize deterministic finite automata.




