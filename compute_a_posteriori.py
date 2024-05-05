import sys

# Define the hypotheses and their priors
hypotheses = {
    'h1': 0.10,
    'h2': 0.20,
    'h3': 0.40,
    'h4': 0.20,
    'h5': 0.10
}

# Define the transition probabilities
transition_probs = {
    'h1': {'C': 1.0, 'L': 0.0},
    'h2': {'C': 0.75, 'L': 0.25},
    'h3': {'C': 0.50, 'L': 0.50},
    'h4': {'C': 0.25, 'L': 0.75},
    'h5': {'C': 0.0, 'L': 1.0}
}

# Function to compute posterior probabilities
def compute_posterior(sequence):
    probabilities = {hypothesis: prior for hypothesis, prior in hypotheses.items()}
    for observation in sequence:
        for hypothesis in hypotheses:
            probabilities[hypothesis] *= transition_probs[hypothesis][observation]
        total_prob = sum(probabilities.values())
        for hypothesis in probabilities:
            probabilities[hypothesis] /= total_prob
    return probabilities

# Function to compute the probability of the next observation
def compute_next_observation_prob(sequence, observation):
    probabilities = compute_posterior(sequence)
    next_observation_prob_C = sum(probabilities[hypothesis] * transition_probs[hypothesis]['C'] for hypothesis in probabilities)
    next_observation_prob_L = sum(probabilities[hypothesis] * transition_probs[hypothesis]['L'] for hypothesis in probabilities)
    return next_observation_prob_C, next_observation_prob_L

# Main function
def main():
    # Get the observation sequence from command line argument
    if len(sys.argv) > 1:
        observation_sequence = sys.argv[1]
    else:
        observation_sequence = ''

    # Compute posterior probabilities
    posterior_probabilities = compute_posterior(observation_sequence)

    # Write results to a text file
    with open("result.txt", "w") as f:
        f.write(f"Observation sequence Q: {observation_sequence}\n")
        f.write(f"Length of Q: {len(observation_sequence)}\n\n")
        for i, observation in enumerate(observation_sequence, start=1):
            f.write(f"After Observation {i} = {observation}:\n")
            for hypothesis, probability in posterior_probabilities.items():
                f.write(f"P({hypothesis} | Q) = {probability:.5f}\n")
            next_observation_prob_C, next_observation_prob_L = compute_next_observation_prob(observation_sequence, observation)
            f.write(f"Probability that the next candy we pick will be C, given Q: {next_observation_prob_C:.5f}\n")
            f.write(f"Probability that the next candy we pick will be L, given Q: {next_observation_prob_L:.5f}\n\n")

if __name__ == "__main__":
    main()

