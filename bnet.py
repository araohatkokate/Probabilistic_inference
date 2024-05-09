import sys
class BayesianNetwork:
    def __init__(self):
        # Define probabilities
        self.prob_B = 0.001
        self.prob_E = 0.002
        self.prob_A_given_BE = {
            (True, True): 0.95,
            (True, False): 0.94,
            (False, True): 0.29,
            (False, False): 0.001
        }
        self.prob_J_given_A = {True: 0.90, False: 0.05}
        self.prob_M_given_A = {True: 0.70, False: 0.01}

    def compute_probability(self, b, e, a, j, m):
        # Compute joint probability
        joint_probability = self.prob_B * self.prob_E * self.prob_A_given_BE[(b, e)] \
                            * self.prob_J_given_A[j] * self.prob_M_given_A[m]
        return joint_probability

    def compute_conditional_probability(self, b, e, a, j, m, given_b=None, given_e=None, given_a=None, given_j=None, given_m=None):
        # Compute conditional probability
        if given_b is not None:
            conditional_probability = self.compute_probability(b, e, a, j, m) / self.compute_probability(given_b, given_e, given_a, given_j, given_m)
        else:
            conditional_probability = self.compute_probability(b, e, a, j, m)
        return conditional_probability


# Main function
def main():
    # Create Bayesian network object
    bayesian_network = BayesianNetwork()

    # Parse command line arguments
    arguments = sys.argv[1:]
    b, e, a, j, m = False, False, False, False, False
    given_b, given_e, given_a, given_j, given_m = None, None, None, None, None

    for arg in arguments:
        if arg[0] == 'B':
            if arg[1] == 't':
                b = True
            else:
                b = False
        elif arg[0] == 'E':
            if arg[1] == 't':
                e = True
            else:
                e = False
        elif arg[0] == 'A':
            if arg[1] == 't':
                a = True
            else:
                a = False
        elif arg[0] == 'J':
            if arg[1] == 't':
                j = True
            else:
                j = False
        elif arg[0] == 'M':
            if arg[1] == 't':
                m = True
            else:
                m = False
        elif arg == 'given':
            pass  # Ignore 'given' keyword
        else:
            given_event = arg
            if given_event[0] == 'B':
                if given_event[1] == 't':
                    given_b = True
                else:
                    given_b = False
            elif given_event[0] == 'E':
                if given_event[1] == 't':
                    given_e = True
                else:
                    given_e = False
            elif given_event[0] == 'A':
                if given_event[1] == 't':
                    given_a = True
                else:
                    given_a = False
            elif given_event[0] == 'J':
                if given_event[1] == 't':
                    given_j = True
                else:
                    given_j = False
            elif given_event[0] == 'M':
                if given_event[1] == 't':
                    given_m = True
                else:
                    given_m = False

    # Check if conditional probability is requested
    if given_b is not None:
        conditional_probability = bayesian_network.compute_conditional_probability(b, e, a, j, m, given_b, given_e, given_a, given_j, given_m)
        print(f"Conditional Probability: {conditional_probability}")
    else:
        probability = bayesian_network.compute_probability(b, e, a, j, m)
        print(f"Probability: {probability}")


if __name__ == "__main__":
    main()