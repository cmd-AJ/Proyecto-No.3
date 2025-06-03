import pandas as pd

def search(item, lst):
    return lst.index(item)

def move_to_front(index, lst):
    item = lst.pop(index)
    lst.insert(0, item)

def imtf_cost(sequence, config):
    lst = config[:]
    total_cost = 0
    data = []

    for step, item in enumerate(sequence):
        before = lst[:]
        index = search(item, lst)
        cost = index + 1
        total_cost += cost

        # Look-ahead: próximos (index - 1) elementos
        lookahead = sequence[step+1 : step+index]
        if item in lookahead:
            move_to_front(index, lst)

        after = lst[:]
        data.append({
            "Paso": step + 1,
            "Lista antes": before,
            "Solicitud": item,
            "Costo": cost,
            "Lista después": after,
        })

    df = pd.DataFrame(data)
    print(df.to_string(index=False))  # Pretty print without index
    print("\nCosto total de acceso:", total_cost)
