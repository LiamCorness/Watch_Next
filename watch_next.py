# Write title and descriptions into a dictionary
# Compare similarity of target description to descriptions in the dict
# Find the description with highest score
# Print the corresponing title to the description with highest similarity score

import spacy
nlp = spacy.load("en_core_web_md")

def watch_next(description):

    model_description = nlp(description)
    # List to store title and similarity scores
    similar_dict = {}

    for title, desc in watch_history_descriptions.items():
        similarity = nlp(desc).similarity(model_description)
        similar_dict[title] = similarity
    
    # find highest similarity score and return corresponding title
    highest_score = max(similar_dict.values())
    for title,score in similar_dict.items():
        if score == highest_score:
            return title

# Dict to store titles and descriptions
watch_history_descriptions = {}

with open ("movies.txt", "r") as movies:
    # For each line in the text file create keys with the titles and assign values with the descriptions
    for line in movies:
        line = line.strip().split(":")
        title = line[0]
        desc = line[1]
        watch_history_descriptions[title] = desc

# The film I want to find the most similar film to
description = "Planet Hulk : Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unforunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

print(f"The movie most similar is {watch_next(description)}")
