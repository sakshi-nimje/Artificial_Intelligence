'''def Joint_Distribution(S,D,A,B,F,Sophia,David,Alarm,Burglary,Fire):
    for s in Sophia:
        if(s[0]==A and s[1]==S):
            m=s[2] 
            break
    for d in David:
        if(d[0]==A and d[1]==D):
            n=d[2]
            break
    for a in Alarm:
        if(a[0]==B and a[1]==F and a[2]==A):
            o=a[3]
            break
    for b in Burglary:
        if(b[0]==B):
            p=b[1]
            break        
    for f in Fire:
        if(f[0]==F):
            q=f[1]
            break

    return m*n*o*p*q                        

Burglary=[["T",0.002],["F",0.998]]
Fire=[["T",0.001],["F",0.999]]
#[burglary,fire,alarm,prob]
Alarm=[
    ["T","T","T",0.94],
    ["T","T","F",0.06],
    ["T","F","T",0.95],
    ["T","F","F",0.05],
    ["F","T","T",0.31],
    ["F","T","F",0.69],
    ["F","F","T",0.001],
    ["F","F","F",0.999]]
#[alarm,call,prob]
David=[
    ["T","T",0.91],
    ["T","F",0.09],
    ["F","T",0.05],
    ["F","F",0.95]]
Sophia=[
    ["T","T",0.75],
    ["T","F",0.25],
    ["F","T",0.02],
    ["F","F",0.98]]

#[S,D,A,B,F]

for d in David:
    if(d[0]=="T" and d[1]=="T"):
        i=d[2]
        break
for a in Alarm:
    if(a[0]=="T" and a[2]=="T"):
        i*=a[3]
for b in Burglary:
    if(b[0]=="T"):
        b[0]=i
    else:
        b[0]==round(1-i,3)       

print("\nIf Alarm was triggered and David called then probability of happening of burglary will be:",round(i,3))

for a in Alarm:
    if(a[0]=="T" and a[1]=="T"):
        i=a[3]
for s in Sophia:
    if(s[0]=="T" and s[1]=="T"):
        i*=s[2]
for s in Sophia:
    if(s[0]=="T" and s[1]=="T"):
        s[2]=i
    elif(s[0]=="T" and s[1]=="F"):
        s[2]=round(1-i,3)    

print("\nIf Fire has occured and Alarm was triggered then probability of Sophia called is:",round(i,3),"\n")
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
print("The probability that the alarm has sounded but neither a burglary nor an fire has occurred, and both David and Sophia call : " , alarm_sounded_probability)

#print(probability.values)
