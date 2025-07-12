# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
def dose(needs):
    #YOUR SOLUTION STARTS HERE
    total = sum(needs)
    if total>500:
        return "No medicine given"
        
    medicine = []
    give = ()

    for i in range (len (needs)):
        if needs[i] >=250:
            return "No medicine given"
            
        if needs[i]%10 == 0:
            give = (int (needs[i]/10),0)
        else:
            give = (int (needs[i]/10+1), (10-needs[i]%10))
        medicine.append (give)
    return medicine
            


#medicine = dose ([251, 0, 120, 0, 0, 0])
#medicine = dose ([9, 250, 120, 0, 0, 0])
#medicine = dose ([0, 0, 120, 0, 0, 250])
#medicine = dose ([10, 20, 30, 40, 50, 0])
#medicine = dose ([249, 38, 47, 56, 5, 14])

# if medicine != None:
#     print (medicine) 
    

            
            
    

    #YOUR SOLUTION ENDS HERE

