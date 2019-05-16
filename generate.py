import gpt_2_simple as gpt2

model = "montagmodel"
gpt2.generate_to_file(sess, destination_path='montagbyai.txt', prefix="The future is ", model_name=model, temperature=1.0)
