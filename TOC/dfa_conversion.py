#Done by Shrish Kumar and Karthik Krishna (Roll Numbers: 22048. 22024)
import itertools
import csv

def rows_to_col():
    temp_states = []
    temp_input_0_output = []
    temp_input_1_output = []

    states = []
    input_0_output = []
    input_1_output = []

    csv_file_path = "TOC/inputcsv.csv"

    line = 0
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if line == 0:
                line += 1
            else:
                states.append(row[0])
                temp_input_0_output.append(row[1])
                temp_input_1_output.append(row[2])
                line += 1

    for item in temp_input_0_output:
        item = item.split(',')
        input_0_output.append(item)

    for item in temp_input_1_output:
        item = item.split(',')
        input_1_output.append(item)

    states = [[x] for x in states]

    s_dfa = []
    i_0_o_dfa = []
    i_1_o_dfa = []

    dfa_transitions = initial(states, input_0_output, input_1_output, s_dfa, i_0_o_dfa, i_1_o_dfa)
    print_dfa_transitions(dfa_transitions)


def initial(s_nfa, i_0_o_nfa, i_1_o_nfa, s_dfa, i_0_o_dfa, i_1_o_dfa):
    s_dfa.append(s_nfa[0])
    i_0_o_dfa.append(i_0_o_nfa[0])
    i_1_o_dfa.append(i_1_o_nfa[0])

    temp_new_states = []
    temp_new_states.append(i_0_o_nfa[0])
    temp_new_states.append(i_1_o_nfa[0])

    return create_dfa(temp_new_states, s_nfa, i_0_o_nfa, i_1_o_nfa, s_dfa, i_0_o_dfa, i_1_o_dfa)


def create_dfa(temp_new_states_list, s_nfa, i_0_o_nfa, i_1_o_nfa, s_dfa, i_0_o_dfa, i_1_o_dfa):
    dfa_transitions = {}  # Dictionary to store transitions

    # Loop through the newly items added in temp_new_states_list:
    while temp_new_states_list:
        # Get the first item only and then deleted it by index
        temp_new_state = temp_new_states_list[0]
        del temp_new_states_list[0]
        # Check the length of the state, if one item, proceed
        if len(temp_new_state) == 1:
            # Add the state if not found in the dfa
            if temp_new_state not in s_dfa:
                s_dfa.append(temp_new_state)
                state_nfa = 0
                # Iterate through state_nfa list to get the item index
                while state_nfa < len(s_nfa):
                    # if item is found, get the output for each input from nfa
                    if temp_new_state == s_nfa[state_nfa]:
                        i_0_o_dfa.append(i_0_o_nfa[state_nfa])
                        i_1_o_dfa.append(i_1_o_nfa[state_nfa])
                        temp_new_states_list.append(i_0_o_nfa[state_nfa])
                        temp_new_states_list.append(i_1_o_nfa[state_nfa])
                        state_nfa += 1
                        break
                    else:
                        state_nfa += 1
            # Do nothing if the state found in the DFA
            else:
                pass

            
        ## if temp_new_states_list > 1
        else:
            # Check if already exists in s_dfa
            if temp_new_state not in s_dfa:
                # Create combo states
                combo_i0o = []
                combo_i1o = []
                s_dfa.append(temp_new_state)
                # Loop through each item in that state
                for each in range(len(temp_new_state)):
                    # Get Each value
                    each_single_in_new_state = []
                    each_single_in_new_state.append(temp_new_state[each])
                    state_nfa = 0
                    while state_nfa < len(s_nfa):
                        if (each_single_in_new_state == s_nfa[state_nfa]):
                            # create Combo result for i0o
                            if i_0_o_nfa[state_nfa] != ['na']:
                                combo_i0o.append(i_0_o_nfa[state_nfa])
                            else:
                                pass
                            if i_1_o_nfa[state_nfa] != ['na']:
                                combo_i1o.append(i_1_o_nfa[state_nfa])
                            else:
                                pass
                            state_nfa += 1
                        else:
                            state_nfa += 1
                # Combine the result into one list sort and remove redundancy
                combo_i0o = list(set(list(itertools.chain.from_iterable(combo_i0o))))
                combo_i1o = list(set(list(itertools.chain.from_iterable(combo_i1o))))
                combo_i0o.sort()
                combo_i1o.sort()
                # Add the new combo states to dfa outputs
                i_0_o_dfa.append(combo_i0o)
                i_1_o_dfa.append(combo_i1o)
                temp_new_states_list.append(combo_i0o)
                temp_new_states_list.append(combo_i1o)
            # If the state already exists in s_dfa, do nothing
            else:
                pass

    # Create a dictionary for easy output
    for i in range(len(s_dfa)):
        dfa_transitions[str(s_dfa[i])] = {
            "Transition 0": i_0_o_dfa[i],
            "Transition 1": i_1_o_dfa[i]
        }

    return dfa_transitions


def print_dfa_transitions(dfa_transitions):
    print("\n--- DFA Transition Diagram ---\n")
    for state, transitions in dfa_transitions.items():
        print(f"State: {state}")
        print(f"  - Transition 0: {transitions['Transition 0']}")
        print(f"  - Transition 1: {transitions['Transition 1']}")
        print()


def main():
    rows_to_col()


if __name__ == "__main__":
    main()
