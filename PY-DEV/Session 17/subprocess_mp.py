from subprocess import Popen, PIPE





process = Popen(["python", r"C:\Users\Manu\Desktop\CB-LV-DS-Feb21\Session 17\child.py"], stdin=PIPE, stdout=PIPE, stderr=PIPE)

# process.stdin.write(b"Manu")
# process.stdin.close()
# output = process.stdout.read()
# err = process.stderr.read()
# ret = process.wait()

output, err = process.communicate(input=b"Manu")

print(output)




# try:
#     outs, errs = proc.communicate(timeout=15)
# except TimeoutExpired:
#     proc.kill()
#     outs, errs = proc.communicate()