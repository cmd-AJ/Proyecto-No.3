
import sys
import imtf
import pandas as pd



def search(input_char, lst):
    """
    Returns the index of the character in the list.
    """
    for i in range(len(lst)):
        if lst[i] == input_char:
            return i
    return -1  # Just in case


def move_to_front(curr_index, lst):
    """
    Moves the character at curr_index to the front.
    """
    char = lst.pop(curr_index)
    lst.insert(0, char)


def mtf_access_cost(config_list, access_sequence):
    """
    Simulates MTF access cost and prints step-by-step info.
    """
    lst = config_list[:]
    total_cost = 0

    data = []

    for step, item in enumerate(access_sequence, start=1):
        before = lst[:]
        index = search(item, lst)
        cost = index + 1
        total_cost += cost
        move_to_front(index, lst)

        # Store the step data into a list of dicts
        data.append({
            "Paso": step,
            "Lista antes": before,
            "Solicitud": item,
            "Costo": cost,
            "Lista después": lst[:],  # Copy current list
        })

    df = pd.DataFrame(data)
    print(df.to_string(index=False))  # Pretty print without index
    print("\nCosto total de acceso:", total_cost)



# sys.argv is a list of command-line arguments

# First argument is always the script name
if len(sys.argv) > 1:
    print("Inciso Number:", sys.argv[1])

    if int(sys.argv[1]) == 1:
        config = [0, 1, 2, 3, 4]
        sequence = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

        print("Configuracion: ",config)
        print("Secuencia: ",sequence)
        # Computes Move to Front transform of given array of numbers
        mtf_access_cost(config, sequence)

    if int(sys.argv[1]) == 2:
        config = [0, 1, 2, 3, 4]
        sequence = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
        # Computes Move to Front transform given array of numbers
        mtf_access_cost(config, sequence)
    

    #BEST CASE FOR MTF ALL ZEROS
    if int(sys.argv[1]) == 3:
        config = [0, 1, 2, 3, 4]
        sequence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0]
        # Computes Move to Front transform given array of numbers
        mtf_access_cost(config, sequence)

    #WORST CASE FOR MTF ALL SORTED FROM HIGH TO LOW, 4 TIMES
    if int(sys.argv[1]) == 4:
        config = [0, 1, 2, 3, 4]
        sequence = [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0]
        # Computes Move to Front transform given array of numbers
        mtf_access_cost(config, sequence)


    if int(sys.argv[1]) == 5:
        config = [0, 1, 2, 3, 4]
        sequence = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        # Computes Move to Front transform given array of numbers
        mtf_access_cost(config, sequence)


    if int(sys.argv[1]) == 6:
        config = [0, 1, 2, 3, 4]
        sequence = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        # Computes Move to Front transform given array of numbers
        mtf_access_cost(config, sequence)

    
    #Best case to prove that it has a lower cost
    if int(sys.argv[1]) == 7:
        config = [0, 1, 2, 3, 4]
        sequence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0]
        # Computes Move to Front transform given array of numbers
        imtf.imtf_cost(sequence, config)


    #Best case to prove that it has a lower cost
    if int(sys.argv[1]) == 8:
        config = [0, 1, 2, 3, 4]
        sequence =  [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0]
        # Computes Move to Front transform given array of numbers
        imtf.imtf_cost(sequence, config)


