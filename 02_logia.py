# LOGIA : an automated theorem prover
# -----------------------------------
# 
# version 0.2, December 13, 2016
# for use with Coq 8.5pl3 (Oct 2016)
# written by wrick
# 
# -----------------------------------
# randomly genned tactics from a static tactics_base
# 2-parent crossover, random mutation
# no natural selection


from numpy.random import randint
from os import system


qed        = False
theorem    = open('/home/wrick/Documents/logia/theorem', 'r').readline()
tactics    = open('/home/wrick/Documents/logia/tactics_base', 'r').read().split('\n')
T          = len(tactics)
population = 10            # constant population size for every generation
maxlength  = 5             # maximum proof length


# create the seeds -- the first organisms/proofs
def seedgen() :
    generation = []

    for i in range(population) :
        length = randint(1, maxlength)
        proof  = []

        for j in range(length) :
            proof.append(randint(T))

        generation.append(proof)

    return(generation)


# define reproduction -- 2-parent crossover, creates a new proof with new length and all
def crossover(proof_tuple) :
    (proof1, proof2) = proof_tuple
    newproof      = []
    prooflength   = randint(1, maxlength)
    combine       = proof1 + proof2
    combinelength = len(combine)

    for i in range(prooflength) :
        newproof.append(randint(0, combinelength))

    return(newproof)


# define mutation -- as random as it can be, no dependencies, doesn't change proof length
def mutagen(proof) :
    mutaprob = 13          # probability of mutation is 1 in 13, 0 means zero probability
    
    for i in proof :
        if randint(mutaprob) == 0 :
            proof[i] = randint(T)

    return(proof)


# the new generation
def generationmap(generation) :
    newgeneration = []
    
    for i in population :
        generation[i] = mutagen(generation[i])

    for i in population :
        proof_tuple = (randint(population), randint(population))
        newproof = crossover(proof_tuple)
        newgeneration.append(newproof)

    return(newgeneration)


# convert integer sequences to tactic strings
def proofgen(sequence) :
    proof = 'Proof.'
    for i in sequence :
        proof += ' ' + tactics[i] + '.'
    proof += ' QED.\n'
    return(proof)


# the program
generation = seedgen()

while qed == False :
    
    for i in population and qed == False :
        Proof = open('/home/wrick/Documents/logia/Proof', 'w')
        Proof.write(theorem + '\n' + proofgen(generation[i]))
        Proof.close()
        system('coqc -compile /home/wrick/Documents/logia/Proof')
        compiled = open('/home/wrick/Documents/logia/Proof.vo', 'r')
        qed = isinstance(compiled, file)

    generation = generationmap(generation)

compiled.close()
system('coqtop /home/wrick/Documents/logia/Proof')


# ---EOF---