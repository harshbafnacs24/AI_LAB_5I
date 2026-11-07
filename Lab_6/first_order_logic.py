
# Week 7: First Order Logic
# Unification Algorithm

# Split arguments of an expression
def split_args(s):

    args = []
    level = 0
    start = 0

    for i, ch in enumerate(s):

        if ch == '(':
            level += 1

        elif ch == ')':
            level -= 1

        elif ch == ',' and level == 0:
            args.append(s[start:i].strip())
            start = i + 1

    args.append(s[start:].strip())

    return args


# Convert expression into terms
def parse(s):

    s = s.strip()

    if '(' not in s:
        return s

    name = s[:s.index('(')].strip()
    inside = s[s.index('(') + 1:-1]

    return (name, [parse(x) for x in split_args(inside)])


# Check whether a term is a variable
def is_variable(x):
    return isinstance(x, str) and x[0].islower()


# Apply substitutions
def apply(term, subs):

    if isinstance(term, str):

        if term in subs:
            return apply(subs[term], subs)

        return term

    name, args = term

    return (name, [apply(x, subs) for x in args])


# Check variable occurrence
def occurs(var, term, subs):

    term = apply(term, subs)

    if term == var:
        return True

    if isinstance(term, tuple):
        return any(occurs(var, x, subs) for x in term[1])

    return False


# Unification function
def unify(a, b, subs):

    a = apply(a, subs)
    b = apply(b, subs)

    if a == b:
        return True

    if is_variable(a):

        if occurs(a, b, subs):
            return False

        subs[a] = b
        return True

    if is_variable(b):

        if occurs(b, a, subs):
            return False

        subs[b] = a
        return True

    if isinstance(a, tuple) and isinstance(b, tuple):

        if a[0] != b[0] or len(a[1]) != len(b[1]):
            return False

        for x, y in zip(a[1], b[1]):

            if not unify(x, y, subs):
                return False

        return True

    return False


# Main program
exp1 = input("Enter first expression: ")
exp2 = input("Enter second expression: ")

a = parse(exp1)
b = parse(exp2)

subs = {}

if unify(a, b, subs):

    print("\nUnification Successful!")
    print("Substitutions:")

    for key, value in subs.items():
        print(key, "=", value)

    print("\nUnified Expression:")
    print(apply(a, subs))

else:

    print("\nUnification Failed!")
