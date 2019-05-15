from textgenrnn import textgrenrnn
textgen = textgenrnn()

textgen.train_from_file('montagtext.txt', num_epochs=100)
