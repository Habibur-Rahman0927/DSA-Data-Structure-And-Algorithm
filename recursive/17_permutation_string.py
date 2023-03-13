def permute(s):
    
    out = []

    # Base Case 
    if len(s) == 1:
        out = [s]
    else:
        # for every letter in string
        for i, let in enumerate(s):
            # for every permutation resulting from step 2 and 3
            for perm in permute(s[:i] + s[i+1:]):
                out += [let + perm]

    return out


print(permute('123'))
