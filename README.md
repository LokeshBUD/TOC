# TOC
TOC PROJECT

|      Name          | Roll Number       |   Contribution                                                 |
|--------------------|-------------------|----------------------------------------------------------------|
| Karthik Krishna    | CB.EN.U4CSE22024  |  2nd type of implementation(TOC FOLDER)                        |
| Lokesh Budda       | CB.EN.U4CSE22026  |  implemetation using libraries(NFAtoDFA file)                  |
| Shrish Kumar       | CB.EN.U4CSE22048  |  2nd type of implementation(TOC FOLDER)                        |
| Sai Keerthana      | CB.EN.U4CSE22050  |  implemetation using libraries(NFAtoDFA file) & documentation  |
| Senthil Adithya    | CB.EN.U4CSE22054  |  implemetation using libraries(NFAtoDFA file)                  |


There are two different implementations.
One is by using the Python libraries(NFAtoDFA file) and the other is by using the logic(TOC FOLDER).

Visual Automata:
Visual Automata is a Python 3 library built as a wrapper for the Automata library to add more visualization features.
.
Define a visual_automata DFA that can accept any string ending with 00 or 11:
dfa = VisualDFA(
    states={"q0", "q1", "q2", "q3", "q4"},
    input_symbols={"0", "1"},
    transitions={
        "q0": {"0": "q3", "1": "q1"},
        "q1": {"0": "q3", "1": "q2"},
        "q2": {"0": "q3", "1": "q2"},
        "q3": {"0": "q4", "1": "q1"},
        "q4": {"0": "q4", "1": "q1"},
    },
    initial_state="q0",
    final_states={"q2", "q4"},
)
new_dfa.table
      0    1
→q0  q0  *q1
*q1  q0   q2
q2   q2  *q1
new_dfa.show_diagram()
![](https://github.com/LokeshBUD/TOC/blob/main/state.jpeg)
