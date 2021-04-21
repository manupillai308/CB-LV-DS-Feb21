import sys
import os
import subprocess
import time
# import resource
# import psutil <- install using pip: pip install psutil
import multiprocessing

def run(python_file, input_file, correct_out_file, test_case_no):
	input_data = open(input_file).read()
	init_time = time.time()
	pipe = subprocess.Popen([sys.executable, python_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	try:
		output, error = pipe.communicate(input_data.encode("utf-8"), timeout=5)
	except subprocess.TimeoutExpired:
		pipe.kill()
		return (test_case_no, "Timeout", time.time() - init_time)

	final_time = time.time()

	if pipe.returncode != 0:
		return (test_case_no, "Run Error", error.decode("utf-8"))

	output = output.decode("utf-8")
	output = output.replace("\r", "")

	running_time = final_time - init_time
	correct_output = open(correct_out_file).read()

	result = "Fail"
	if running_time < 1.0 and correct_output == output:
		result = "Pass"
	elif running_time > 1.0:
		result = "Time Limit Exceeded"

	return (test_case_no, result, running_time)


if __name__ == "__main__":

	test_case_dir = sys.argv[1]

	args = []
	for test_case_no in os.listdir(test_case_dir):
		root = os.path.join(test_case_dir, test_case_no)
		arg = ("./my_program.py", os.path.join(root, "input.txt"), os.path.join(root, "correct_output.txt"), test_case_no)
		args.append(arg)

	p = multiprocessing.Pool(min(len(args), 5))

	results = p.starmap(run, args)
	import tabulate #<- pip install tabulate

	print(tabulate.tabulate(results, headers=["Test Case", "Result", "Time Taken/Error Description"], tablefmt="grid"))
