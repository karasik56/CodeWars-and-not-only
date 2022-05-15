#[1,2,3,4,[12,34,45,[78,90]]]

def solve(multy_list, flag):
    global res
    if flag is not True:
        res = []
    for i in multy_list:
        if isinstance(i, list):
            return solve(i, flag=True)
        res.append(i)
    return res





print(solve([1,2,3,4,[12,34,45,[78,90,[100]]]], False))