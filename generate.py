import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name="runs/181/checkpoint/run1")

gpt2.generate_to_file(sess, destination_path='montagbyai.txt', prefix="The future is ", temperature=1.0)
