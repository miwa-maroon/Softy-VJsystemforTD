dests = ops('layer*')
srcs = ops('scene*')

def bootstrap():
	print('---bootstrapping---')
	for count, src in enumerate(srcs):
		for dest in dests:
			dest.inputConnectors[count].connect(src)


def main():
	print('>>> main <<<')
	bootstrap()

main()


