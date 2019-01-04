import sys

#print(sys.argv)

message1 = "Praneesh gets a full time job in {} as a {}"

message2 = "Praneesh gets a full time as a {}"
job_title = sys.argv[2:]

if sys.argv[1] == "Microsoft":
	job_title = sys.argv[2]
	print(message1.format(sys.argv[1], job_title))
else :
	job_title = sys.argv[1]
	print(message2.format(job_title))


# a = int(sys.argv[1])
# b = int(sys.argv[2])

# len_argv = len(sys.argv)

# print("Sum of input is {} and length is {}".format(a + b, len_argv))

