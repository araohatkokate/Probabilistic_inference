import sys

# Define the hypotheses and their priors
hypotheses = {
    "h1": 0.10,
    "h2": 0.20,
    "h3": 0.40,
    "h4": 0.20,
    "h5": 0.10
}

# Define the transition probabilities for each hypothesis
transition_probs = {
    "h1": {"C": 1.0, "L": 0.0},
    "h2": {"C": 0.75, "L": 0.25},
    "h3": {"C": 0.50, "L": 0.50},
    "h4": {"C": 0.25, "L": 0.75},
    "h5": {"C": 0.0, "L": 1.0}
}

# Function to update posterior probabilities based on observation
def update_posterior(posterior, observation):
    total_prob = sum(posterior[hypothesis] * transition_probs[hypothesis][observation] for hypothesis in posterior)
    for hypothesis in posterior:
        posterior[hypothesis] *= transition_probs[hypothesis][observation] / total_prob
    return posterior

# Function to calculate the probability of the next observation
def next_observation_probability(posterior, observation):
    prob_C = sum(posterior[hypothesis] * transition_probs[hypothesis]['C'] for hypothesis in posterior)
    prob_L = sum(posterior[hypothesis] * transition_probs[hypothesis]['L'] for hypothesis in posterior)
    return prob_C, prob_L

# Function to compute the posterior probabilities and next observation probabilities
def compute_probabilities(observations):
    posterior = hypotheses.copy()
    with open("result.txt", "w") as file:
        file.write("Observation sequence Q: {}\n".format(observations))
        file.write("Length of Q: {}\n\n".format(len(observations)))
        for i, observation in enumerate(observations):
            posterior = update_posterior(posterior, observation)
            file.write("After Observation {} = {}:\n".format(i + 1, observation))
            for hypothesis in posterior:
                file.write("P({} | Q) = {:.6f}\n".format(hypothesis, posterior[hypothesis]))
            prob_C, prob_L = next_observation_probability(posterior, observation)
            file.write("Probability that the next candy we pick will be C, given Q: {:.5f}\n".format(prob_C))
            file.write("Probability that the next candy we pick will be L, given Q: {:.5f}\n\n".format(prob_L))

# Main function
def main():
    if len(sys.argv) == 2:
        observations = sys.argv[1]
        compute_probabilities(observations)
    else:
        with open("result.txt", "w") as file:
            file.write("No observations provided.")

if __name__ == "__main__":
    main()

