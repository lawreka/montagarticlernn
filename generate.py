import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name="montagmodel")

gpt2.generate(sess, run_name="montagmodel", prefix="The future is ", temperature=0.5)
