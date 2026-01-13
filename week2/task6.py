def all_eq(lst):
    m = max(len(s) for s in lst)
    return [s.ljust(m, '_') for s in lst]


# example usage
if __name__ == "__main__":
    data = ["cat", "lion", "tiger"]
    print(all_eq(data))