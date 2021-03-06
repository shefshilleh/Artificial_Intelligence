from heapq import heappush, heappop
from Planning.ClosedList import ClosedList

class BestFirstSearch:

    @staticmethod
    def plan(start_state):
        expand_count = 0
        open = []
        closed = ClosedList()
        heappush(open, start_state)
        closed.insert(start_state)
        while open:
            u = heappop(open)
            if u.is_goal():
                ans = []
                u.get_plan(ans)
                # return plan
                print("Expanded {} states".format(expand_count))
                expand_count = 0
                print(len(ans))
                return ans
            else:
                successors = u.expand()
                for v in successors:
                    #  if v is in closed
                    if v in closed:
                        # if v.f >= closed(v).f
                        if v >= closed.get(v):
                            # continue
                            continue
                        else:
                            closed.remove(v)
                    # insert v to open and closed
                    heappush(open, v)
                    closed.insert(v)
                expand_count += 1
        raise ValueError('No valid path exist from %s' % start_state)