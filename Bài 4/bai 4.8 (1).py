def find_min_max(values):
    if not values:
        return None, None
    min_val = min(values)
    max_val = max(values)
    return min_val, max_val

def sort_list(values):
    return sorted(values)