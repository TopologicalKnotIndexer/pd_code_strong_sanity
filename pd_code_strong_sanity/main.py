import pd_code_to_diagram

def sanity(pd_code:list[list[int]]) -> bool:
    try:
        pd_code_to_diagram.get_diagram_from_pd_code(pd_code)
        suc = True
    except:
        suc = False
    return suc
