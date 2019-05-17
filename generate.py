import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name="montagmodel")

gpt2.generate_to_file(sess, destination_path='montagarticlernn-temp0-5-20samples.txt', nsamples=20, temperature=0.5, run_name="montagmodel")
gpt2.generate_to_file(sess, destination_path='montagarticlernn-temp0-7-20samples.txt', nsamples=20, temperature=0.7, run_name="montagmodel")
gpt2.generate_to_file(sess, destination_path='montagarticlernn-temp1-20samples.txt', nsamples=20, temperature=1.0, run_name="montagmodel")
gpt2.generate_to_file(sess, destination_path='montagarticlernn-temp1-5-20samples.txt', nsamples=20, temperature=1.5, run_name="montagmodel")
