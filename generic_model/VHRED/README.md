### Generating Twitter dataset
in twitter_dataset folder: python3 id2tweet.py TweetIDs_Test.txt [twitter id file] [twitter output file]
i.e. python3 id2tweet.py TweetIDs_Test.txt tweets_test_final.csv
Note: script can only fetch 450 tweets / 15 minutes

### Loading Pretrained weights
VHRED Model: Download Pretrained Model, then place all files in a folder named ./vhred
https://drive.google.com/file/d/0B-nb1w_dNuMLY0Fad3N1YU9ZOU0/view?usp=sharing



### Model Sampling & Testing

To generate model responses using beam search run:

    THEANO_FLAGS=mode=FAST_RUN,floatX=float32,device=gpu python sample.py <model_name> <contexts> <model_outputs> --beam_search --n-samples=<beams> --ignore-unk --verbose

where &lt;model_name&gt; is the name automatically generated during training, &lt;contexts&gt; is a file containing the dialogue contexts with one dialogue per line, and &lt;beams&gt; is the size of the beam search. The results are saved in the file &lt;model_outputs&gt;.

To compute the embedding-based metrics on the generated responses run:

    python Evaluation/embedding_metrics.py <ground_truth_responses> <model_outputs> <word_emb> 

where &lt;ground_truth_responses&gt; is a file containing the ground truth responses, &lt;model_outputs&gt; is the file generated above and &lt;word_emb&gt; is the path to the binarized word embeddings. For the word embeddings, we recommend to use Word2Vec trained on the GoogleNews Corpus: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM.



### Citation

If you build on this work, we'd really appreciate it if you could cite our papers:

    A Hierarchical Latent Variable Encoder-Decoder Model for Generating Dialogues. Iulian Vlad Serban, Alessandro Sordoni, Ryan Lowe, Laurent Charlin, Joelle Pineau, Aaron Courville, Yoshua Bengio. 2016. http://arxiv.org/abs/1605.06069

    Building End-To-End Dialogue Systems Using Generative Hierarchical Neural Network Models. Iulian V. Serban, Alessandro Sordoni, Yoshua Bengio, Aaron Courville, Joelle Pineau. 2016. AAAI. http://arxiv.org/abs/1507.04808.


### Datasets

The pre-processed Ubuntu Dialogue Corpus and model responses used by Serban et al. (2016a) are available at: http://www.iulianserban.com/Files/UbuntuDialogueCorpus.zip. These can be used with the model states "prototype_ubuntu_LSTM", "prototype_ubuntu_HRED", and "prototype_ubuntu_VHRED" (see state.py) to reproduce the results of Serban et al. (2016a) on the Ubuntu Dialogue Corpus.

The original Ubuntu Dialogue Corpus as released by Lowe et al. (2015) can be found here: http://cs.mcgill.ca/~jpineau/datasets/ubuntu-corpus-1.0/

Unfortunately due to Twitter's terms of service we are not allowed to distribute Twitter content. Therefore we can only make available the tweet IDs, which can then be used with the Twitter API to build a similar dataset. The tweet IDs and model test responses can be found here: http://www.iulianserban.com/Files/TwitterDialogueCorpus.zip.

The MovieTriples script is also available for research purposes only by contacting Iulian Vlad Serban by email, although we strongly recommend researchers to benchmark their models on Ubuntu and Twitter, since these datasets are substantially larger and represent more well-defined tasks.

### References

    A Hierarchical Latent Variable Encoder-Decoder Model for Generating Dialogues. Iulian Vlad Serban, Alessandro Sordoni, Ryan Lowe, Laurent Charlin, Joelle Pineau, Aaron Courville, Yoshua Bengio. 2016a. http://arxiv.org/abs/1605.06069

    Multiresolution Recurrent Neural Networks: An Application to Dialogue Response Generation. Iulian Vlad Serban, Tim Klinger, Gerald Tesauro, Kartik Talamadupula, Bowen Zhou, Yoshua Bengio, Aaron Courville. 2016b. http://arxiv.org/abs/1606.00776.

    Building End-To-End Dialogue Systems Using Generative Hierarchical Neural Network Models. Iulian V. Serban, Alessandro Sordoni, Yoshua Bengio, Aaron Courville, Joelle Pineau. 2016c. AAAI. http://arxiv.org/abs/1507.04808.

    The Ubuntu Dialogue Corpus: A Large Dataset for Research in Unstructured Multi-Turn Dialogue Systems. Ryan Lowe, Nissan Pow, Iulian Serban, Joelle Pineau. 2015. SIGDIAL. http://arxiv.org/abs/1506.08909.
