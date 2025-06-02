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

    print(f"{'Paso':<4} | {'Lista antes':<20} | {'Solicitud':<10} | {'Costo':<5} | {'Lista después'}")
    print("-" * 70)

    for step, item in enumerate(access_sequence, start=1):
        before = lst[:]
        index = search(item, lst)
        cost = index + 1
        total_cost += cost
        move_to_front(index, lst)
        print(f"{step:<4} | {str(before):<20} | {item:^10} | {cost:^5} | {lst}")

    print("\nCosto total de acceso:", total_cost)


import sys

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

