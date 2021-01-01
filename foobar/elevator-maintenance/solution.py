def solution(l):
    int_revs = []
    for rev in l:
        int_rev = [int(x) for x in rev.split(".")]
        int_rev = int_rev + [-1]*(3 - len(int_rev))
        int_revs.append(int_rev)

    int_revs.sort()
    sorted_revs = [".".join([str(x) for x in int_rev if x != -1]) for int_rev in int_revs]
    return sorted_revs
    
