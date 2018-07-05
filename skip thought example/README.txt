
This is just an example of running the sent2vec model discribed in the skip-thoughts paper. You first have to follow the basic setup instructions. It uses Python 2.7 and Theano.

## Getting started

download the model files and word embeddings. The embedding files (utable and btable) are quite large (>2GB) so make sure there is enough space available. The encoder vocabulary can be found in dictionary.txt.

	wget http://www.cs.toronto.edu/~rkiros/models/dictionary.txt
    wget http://www.cs.toronto.edu/~rkiros/models/utable.npy
    wget http://www.cs.toronto.edu/~rkiros/models/btable.npy
    wget http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz
    wget http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz.pkl
    wget http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz
    wget http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz.pkl
	
clone the skipthoughts repository: https://github.com/ryankiros/skip-thoughts

Once these are downloaded, open skipthoughts.py and set the paths of the variables: (path_to_models and path_to_tables) to the above files location. You are all set.

Note: - you can use a pickle file to save your converted sentences so that you don't have to rerun your code everytime. 

