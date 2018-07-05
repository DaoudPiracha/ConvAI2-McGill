import sys

# make sure the cloned GitHub repo is in the system path
sys.path.append("C:/Users/pnwar/OneDrive/Documents/GitHub/skip-thoughts") # change this path !

import skipthoughts

# create model
model = skipthoughts.load_model()
encoder = skipthoughts.Encoder(model)

# encode desired sentences into vectors.
phrases = ['hello friend, how are you?','I don\'t know','sit down, be humble.']
vectors = encoder.encode(phrases)

print(vectors)