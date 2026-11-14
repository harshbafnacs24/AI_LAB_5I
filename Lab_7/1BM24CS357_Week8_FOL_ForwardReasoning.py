
# Week 8: FOL Forward Chaining

# Initial Knowledge Base
KB = {
    ("American", "Robert"),
    ("Missile", "T1"),
    ("Owns", "A", "T1"),
    ("Enemy", "A", "America")
}


# Forward Chaining Algorithm
def forward_chaining(KB):

    print("INITIAL KNOWLEDGE BASE")
    for fact in sorted(KB):
        print(fact)

    print("\nFORWARD CHAINING STARTED")

    while True:

        new_facts = set()

        # Rule 1: Missile(x) -> Weapon(x)
        for fact in KB:
            if fact[0] == "Missile":
                x = fact[1]
                new_facts.add(("Weapon", x))

        # Rule 2: Missile(x) AND Owns(A,x)
        #         -> Sells(Robert,x,A)
        for m in KB:
            for o in KB:

                if (m[0] == "Missile" and
                    o[0] == "Owns" and
                    m[1] == o[2] and
                    o[1] == "A"):

                    new_facts.add(
                        ("Sells", "Robert", m[1], "A")
                    )

        # Rule 3: Enemy(x,America) -> Hostile(x)
        for fact in KB:
            if (fact[0] == "Enemy" and
                fact[2] == "America"):

                new_facts.add(("Hostile", fact[1]))

        # Rule 4: American(p) AND Weapon(q)
        # AND Sells(p,q,r) AND Hostile(r)
        # -> Criminal(p)

        for a in KB:
            for w in KB:
                for s in KB:
                    for h in KB:

                        if (a[0] == "American" and
                            w[0] == "Weapon" and
                            s[0] == "Sells" and
                            h[0] == "Hostile" and
                            a[1] == s[1] and
                            w[1] == s[2] and
                            h[1] == s[3]):

                            new_facts.add(
                                ("Criminal", a[1])
                            )

        # Remove facts already present
        new_facts = new_facts - KB

        if not new_facts:
            break

        print("\nNew Facts Generated:")
        for fact in sorted(new_facts):
            print(fact)

        KB.update(new_facts)

    print("\nFINAL KNOWLEDGE BASE")
    for fact in sorted(KB):
        print(fact)

    # Check the goal
    goal = ("Criminal", "Robert")

    print("\nQUERY: Criminal(Robert)")

    if goal in KB:
        print("Result: TRUE")
        print("Robert is a Criminal.")
    else:
        print("Result: FALSE")
        print("Goal could not be proved.")


# Execute
forward_chaining(KB)
