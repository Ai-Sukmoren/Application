def TVM(pv: int = 0, r: float = 0, n: int = 0) -> float:
    r = (r/100)
    fv = round(pv * (1 + r) ** n,2)
    return F'${fv}'

print(TVM(1000,5,3))