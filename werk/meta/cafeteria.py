'''
A cafeteria table consists of a row of NN seats, numbered from 11 to NN from left to right.
Social distancing guidelines require that every diner be seated such that KK seats to their left and KK seats to their right (or all the remaining seats to that side if there are fewer than KK) remain empty.

There are currently MM diners seated at the table, the iith of whom is in seat S_i or S[i].
No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.

Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
Please take care to write a solution which runs within the time limit.
'''

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  S.sort()
  
  extra_diner = 0
  i = 0
  while i < M-1:
    start = S[i] + (K+1)
    end = S[i+1] - (K+1)
    extra_diner += get_extra_diner(start, end, K)
    i += 1
    
  extra_diner_start = get_extra_diner(1, S[0]-(K+1), K)
  extra_diner_end = get_extra_diner(S[-1] + (K+1), N, K)
  return extra_diner_start + extra_diner + extra_diner_end

def get_extra_diner(start, end, K):
  if end < start:
    return 0
  seats = end - start + 1
  out = int(seats / (K+1))
  if seats % (K+1) != 0:
    out += 1
  return out

print(getMaxAdditionalDinersCount(15, 2, 3, [11, 6, 14]))
