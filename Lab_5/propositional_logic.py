
# Week 6: Propositional Logic
# Truth Table Enumeration

from itertools import product

# Generate all possible truth values
values = [True, False]

print("P Q R | KB | R | R->P | Q->R")
print("--------------------------------")

entails_R = True
entails_RP = True
entails_QR = True

for P, Q, R in product(values, repeat=3):

    # Knowledge Base
    KB = ((not Q or P) and
          (not P or not Q) and
          (Q or R))

    # Queries
    query1 = R
    query2 = (not R or P)
    query3 = (not Q or R)

    print(P, Q, R, "|", KB, "|",
          query1, "|", query2, "|", query3)

    # Check entailment
    if KB and not query1:
        entails_R = False

    if KB and not query2:
        entails_RP = False

    if KB and not query3:
        entails_QR = False


print("\nENTAILMENT RESULTS")

print("KB entails R:", entails_R)
print("KB entails R -> P:", entails_RP)
print("KB entails Q -> R:", entails_QR)
