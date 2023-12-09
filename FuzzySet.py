def fuzzy_union(setA, setB):
    result = {}
    for key in setA.keys():
        result[key] = max(setA[key], setB.get(key, 0))
    for key in setB.keys():
        if key not in result:
            result[key] = setB[key]
    return result

def fuzzy_intersection(setA, setB):
    result = {}
    for key in setA.keys():
        result[key] = min(setA[key], setB.get(key, 0))
    return result

def fuzzy_complement(setA):
    result = {}
    for key in setA.keys():
        result[key] = 1 - setA[key]
    return result

def fuzzy_difference(setA, setB):
    complement_setB = fuzzy_complement(setB)
    return fuzzy_intersection(setA, complement_setB)

def algebraic_sum(setA, setB):
    result = {}
    for key in setA.keys():
        result[key] = setA[key] + setB.get(key, 0)
    for key in setB.keys():
        if key not in result:
            result[key] = setB[key]
    return result

def algebraic_product(setA, setB):
    result = {}
    for key in setA.keys():
        result[key] = setA[key] * setB.get(key, 0)
    return result

def bounded_sum(setA, setB):
    result = {}
    for key in setA.keys():
        result[key] = min(1, setA[key] + setB.get(key, 0))
    for key in setB.keys():
        if key not in result:
            result[key] = min(1, setB[key])
    return result

def bounded_difference(setA, setB):
    result = {}
    for key in setA.keys():
        result[key] = max(0, setA[key] - setB.get(key, 0))
    for key in setB.keys():
        if key not in result:
            result[key] = max(0, -setB[key])
    return result

# Example usage:
setX = {'A': 1.0, 'B': 0.5, 'C': 0.3, 'D': 0.4}
setY = {'A': 0.4, 'B': 0.2,  'C': 0.7, 'D': 0.1}

print("Fuzzy Set X : " , setX)
print("\nFuzzy Set Y : " , setY)
print("\nFuzzy Union:", fuzzy_union(setX, setY))
print("\nFuzzy Intersection:", fuzzy_intersection(setX, setY))
print("\nFuzzy Complement of setX:", fuzzy_complement(setX))
print("\nFuzzy Complement of setY:", fuzzy_complement(setY))
print("\nFuzzy Difference (setX - setY):", fuzzy_difference(setX, setY))
print("\nFuzzy Difference (setY - setX):", fuzzy_difference(setY, setX))
print("\nAlgebraic Sum:", algebraic_sum(setX, setY))
print("\nAlgebraic Product:", algebraic_product(setX, setY))
print("\nBounded Sum:", bounded_sum(setX, setY))
print("\nBounded Difference (setX - setY):", bounded_difference(setX, setY))
print("\nBounded Difference (setY - setX):", bounded_difference(setY, setX))
 