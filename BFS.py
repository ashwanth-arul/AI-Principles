import sys
import time

if sys.argv==[''] or len(sys.argv)<2:
  import TowerOfHanoi as Problem
else:
  import importlib
  Problem = importlib.import_module(sys.argv[1])


print("\nWelcome to BFS")
COUNT = None
BACKLINKS = {}

#DO NOT CHANGE THIS FUNCTION
def runBFS():
  initial_state = Problem.CREATE_INITIAL_STATE()
  print("Initial State:")
  print(initial_state)
  global COUNT, BACKLINKS
  COUNT = 0
  BACKLINKS = {}
  path, name = IterativeBFS(initial_state)
  print(str(COUNT)+" states examined.")
  return path, name

# DO NOT CHANGE THE NAME OR THE RETURN VALUES
# TODO: implement the core BFS algorithm
def IterativeBFS(initial_state):
    global COUNT, BACKLINKS

    OPEN = [initial_state]
    CLOSED = []
    BACKLINKS[initial_state] = -1

    while OPEN != []:
        S = OPEN[0]
        del OPEN[0]
        CLOSED.append(S)

        # DO NOT CHANGE THIS SECTION
        # the goal test, return path if reached goal
        if Problem.GOAL_TEST(S):
            print("\n"+Problem.GOAL_MESSAGE_FUNCTION(S))
            path = backtrace(S)
            return path, Problem.PROBLEM_NAME

        # DO NOT CHANGE THE CODE ABOVE

        # TODO: finish BFS implementation
        COUNT += 1
        L = []
        for op in Problem.OPERATORS:
            if op.precond(S):
                new_state = op.state_transf(S)
                if not (new_state in OPEN) and not (new_state in CLOSED):
                    L.append(new_state)
                    BACKLINKS[new_state] = S

        OPEN = OPEN + L


# returns a list of states
# DO NOT CHANGE
def backtrace(S):
  global BACKLINKS
  path = []
  while not S == -1:
    path.append(S)
    S = BACKLINKS[S]
  path.reverse()
  print("Solution path: ")
  for s in path:
    print(s)
  print("\nPath length = "+str(len(path)-1))
  return path

if __name__=='__main__':
  start_time = time.time()
  path, name = runBFS()
  end_time = time.time()
  time_taken = end_time - start_time
  print("\nTime taken to run", time_taken)