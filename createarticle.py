import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name="montagmodel")

gpt2.generate_to_file(sess, destination_path='article.txt', temperature=0.5, run_name="montagmodel")
