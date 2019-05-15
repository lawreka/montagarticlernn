from textgenrnn import textgenrnn
textgen = textgenrnn()

textgen.train_from_file('../datasets/montagtext.txt', num_epochs=100)
