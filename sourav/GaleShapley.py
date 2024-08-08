pref = {"men": {}, "women": {}}

n = int(input("Enter the number of couples: "))

for i in range(n):
    pref["men"].update(
        {
            input(f"Enter the name and preference of man {i+1}: "): [input() for _ in range(n)]
        }
    )
for i in range(n):
    pref["women"].update(
        {
            input(f"Enter the name and preference of woman {i+1}: "): [input() for _ in range(n)]
        }
    )

def gale_shapley(pref):
    free_men = list(pref["men"].keys())
    couples = {}

    while free_men:
        proposer = free_men.pop(0)

        for woman in pref["men"][proposer]:
            if woman not in couples:
                couples[woman] = proposer
                break

            elif pref["women"][woman].index(proposer) < pref["women"][woman].index(couples[woman]):
                free_men.append(couples[woman])
                couples[woman] = proposer
                break
        
        pref["men"][proposer].pop(0)
    return couples

print(gale_shapley(pref))
                
