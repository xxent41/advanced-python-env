def all_eq(lst):
    max_len = max(len(s) for s in lst)
    return [s + "_" * (max_len - len(s)) for s in lst]


# example usage
if __name__ == "__main__":
    data = ["cat", "lion", "tiger"]
    print(all_eq(data))