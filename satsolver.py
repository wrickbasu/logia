# SAT Solver for LOGIA
# takes a proposition and outputs the possible cases of propositional variables for which the proposition evaluates to True
# this is to avoid the halting problem and find possible paths of proving a proposition


from sympy import symbols, satisfiable


def satsolver_main():
    prop = open('.../logia/prop', 'r').readline()    # of the form -- Proposition name : forall p q r :Prop, expression.
    expr = prop.split(',')[-1].strip('.')            # expression without leading space or trailing .
    varnames = split(':')[1].strip()[7:].replace(' ', ',')    # store the names of the variables as a string, split with ','
    varlist = list(symbols(varnames))                # create and store the symbols themselves in a list

    try:
        models = []
        sat = satisfiable(expr, all_models = True)
        while True:
            models.append(next(sat))
    except StopIteration:
        pass

    return(models)

satsolver_main()
  
# TO DO: multiple propositions
