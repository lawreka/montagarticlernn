import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.generate_to_file(sess, destination_path='montagbyai.txt', prefix="The future is ", model_name="spell/runs/181/models/117M/", temperature=1.0)
