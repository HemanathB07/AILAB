import itertools
class PropositionalLogic:
    def __init__(self):
        self.clauses = []
    def add_clause(self, clause):
        self.clauses.append(clause)
    def pl_resolution(self):
        """Perform propositional logic resolution to determine satisfiability."""
        new = set()
        while True:
            n = len(self.clauses)
            pairs = [(self.clauses[i], self.clauses[j]) for i in range(n) for j in range(i + 1, n)]
            for (ci, cj) in pairs:
                resolvents = self.pl_resolve(ci, cj)
                if [] in resolvents:
                    return False  # Found an empty clause, unsatisfiable
                for res in resolvents:
                    new.add(tuple(res))
            if new.issubset(set(map(tuple, self.clauses))):
                return True  # No new clauses added, satisfiable
            for clause in new:
                if list(clause) not in self.clauses:
                    self.clauses.append(list(clause))
            new = set()
    def pl_resolve(self, ci, cj):
        """Resolve two clauses to produce a set of resolvents."""
        resolvents = []
        for di in ci:
            for dj in cj:
                if di == -dj:
                    resolvent = list(set(ci) - {di}) + list(set(cj) - {dj})
                    resolvents.append(resolvent)
        return resolvents
# Example usage
pl = PropositionalLogic()
# Adding clauses for the problem (example: (A or B) and (not A or C) and (not B or not C))
pl.add_clause([1, 2])     # A or B
pl.add_clause([-1, 3])    # not A or C
pl.add_clause([-2, -3])   # not B or not C
# Checking for satisfiability
is_satisfiable = pl.pl_resolution()
if is_satisfiable:
    print("The knowledge base is satisfiable.")
else:
    print("The knowledge base is not satisfiable.")
