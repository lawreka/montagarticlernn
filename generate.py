import gpt_2_simple as gpt2

<<<<<<< HEAD
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

gpt2.generate_to_file(sess, destination_path='montagbyai.txt', prefix="The future is ", temperature=1.0)
=======
model = "montagmodel"
gpt2.generate_to_file(sess, destination_path='montagbyai.txt'), prefix="The future is ", model_name=model, temperature=1.0)
>>>>>>> parent of 7c39a15... fixed bad parentheses
