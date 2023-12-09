'''def Joint_Distribution(S, D, A, B, F, Sophia, David, Alarm, Burglary, Fire):
    # Calculate m, n, o, p, and q based on given data
    m, n, o, p, q = 1, 1, 1, 1, 1

    for s in Sophia:
        if s[0] == A and s[1] == S:
            m = s[2]

    for d in David:
        if d[0] == A and d[1] == D:
            n = d[2]

    for a in Alarm:
        if a[0] == B and a[1] == F and a[2] == A:
            o = a[3]

    for b in Burglary:
        if b[0] == B:
            p = b[1]

    for f in Fire:
        if f[0] == F:
            q = f[1]

    return m * n * o * p * q

Burglary = [["T", 0.002], ["F", 0.998]]
Fire = [["T", 0.001], ["F", 0.999]]

Alarm = [
    ["T", "T", "T", 0.94],
    ["T", "T", "F", 0.06],
    ["T", "F", "T", 0.95],
    ["T", "F", "F", 0.05],
    ["F", "T", "T", 0.31],
    ["F", "T", "F", 0.69],
    ["F", "F", "T", 0.001],
    ["F", "F", "F", 0.999]
]

David = [
    ["T", "T", 0.91],
    ["T", "F", 0.09],
    ["F", "T", 0.05],
    ["F", "F", 0.95]
]

Sophia = [
    ["T", "T", 0.75],
    ["T", "F", 0.25],
    ["F", "T", 0.02],
    ["F", "F", 0.98]
]

i = 1
# Calculate the probability of burglary if the Alarm was triggered and David called
for d in David:
    if d[0] == "T" and d[1] == "T":
        i *= d[2]

for a in Alarm:
    if a[0] == "T" and a[2] == "T":
        i *= a[3]

for b in Burglary:
    if b[0] == "T":
        b[1] = i
    else:
        b[1] = round(1 - i, 3)

print("If Alarm was triggered and David called, the probability of a burglary happening is:", round(i, 3))

# Calculate the probability of Sophia calling if Fire occurred and the Alarm was triggered
i = 1
for a in Alarm:
    if a[0] == "T" and a[1] == "T":
        i = a[3]

for s in Sophia:
    if s[0] == "T" and s[1] == "T":
        i *= s[2]

for s in Sophia:
    if s[0] == "T" and s[1] == "T":
        s[2] = i
    elif s[0] == "T" and s[1] == "F":
        s[2] = round(1 - i, 3)

print("If a Fire has occurred and the Alarm was triggered, the probability of Sophia calling is:", round(i, 3))


from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the Bayesian network structure
model = BayesianNetwork([('B', 'A'), ('E', 'A'), ('A', 'J'), ('A', 'M')])

# Define Conditional Probability Distributions (CPDs)
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.002], [0.998]])
cpd_e = TabularCPD(variable='E', variable_card=2, values=[[0.999], [0.001]])
cpd_a = TabularCPD(variable='A', variable_card=2, 
                   values=[[0.999, 0.05, 0.69, 0.06],
                           [0.001, 0.95, 0.31, 0.94]],
                   evidence=['B', 'E'], evidence_card=[2, 2])  # Fix evidence_card
cpd_j = TabularCPD(variable='J', variable_card=2, 
                   values=[[0.95, 0.09],
                           [0.05, 0.91]],
                   evidence=['A'], evidence_card=[2])
cpd_m = TabularCPD(variable='M', variable_card=2, 
                   values=[[0.98, 0.25],
                           [0.02, 0.75]],
                   evidence=['A'], evidence_card=[2])

# Add CPDs to the model
model.add_cpds(cpd_b, cpd_e, cpd_a, cpd_j, cpd_m)

# Check if the model is valid
assert model.check_model()

# Create an inference object
inference = VariableElimination(model)

# Calculate the conditional probability P(J | B=True, E=True)
# conditional_probability = inference.query(variables=['J'], evidence={'B': 1, 'E': 1}, show_progress=False)

# Calculate the probability P(A=True, B=False, E=False, J=True, M=True)
probability = inference.query(variables=['A', 'J', 'M'], evidence={'B': 0, 'E': 0}, show_progress=False)

print(probability.values)


#print(conditional_probability.values)
'''

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the Bayesian network structure
model = BayesianNetwork([('Fire', 'Alarm'), ('Alarm', 'David call'), ('Alarm', 'Sophia call'), ('Burglary', 'Alarm')])

# Define Conditional Probability Distributions (CPDs)
cpd_fire = TabularCPD(variable='Fire', variable_card=2, values=[[0.999], [0.001]])
cpd_alarm = TabularCPD(variable='Alarm', variable_card=2, 
                   values=[[0.999, 0.05, 0.69, 0.06], [0.001, 0.95, 0.31, 0.94]],
                   evidence=['Fire', 'Burglary'], evidence_card=[2, 2])
cpd_burglary = TabularCPD(variable='Burglary', variable_card=2, values=[[0.002] , [0.998]])
cpd_david_call = TabularCPD(variable='David call', variable_card=2, 
                   values=[[ 0.95 , 0.09],
                           [0.05 , 0.91]],
                   evidence=['Alarm'], evidence_card=[2])
cpd_sophia_call = TabularCPD(variable='Sophia call', variable_card=2, 
                   values=[[0.98 , 0.25],
                           [ 0.02 , 0.75]],
                   evidence=['Alarm'], evidence_card=[2])

# Add CPDs to the model
model.add_cpds(cpd_fire, cpd_alarm, cpd_burglary, cpd_david_call, cpd_sophia_call)

# Check if the model is valid
assert model.check_model()

# Create an inference object
inference = VariableElimination(model)

# Calculate the probability that the alarm has sounded but neither a burglary nor an earthquake has occurred, and both David and Sophia call.
#probability = inference.query(variables=['Alarm'], evidence={'Burglary': 0, 'Fire': 0, 'Sophia call': 1, 'David call': 1}, show_progress=False)

result = inference.query(variables=['Alarm'], evidence={'Burglary': 0, 'Fire': 0, 'Sophia call': 1, 'David call': 1}, show_progress=True)
alarm_sounded_probability = result.values[1]
print(alarm_sounded_probability)

#print(probability.values)
