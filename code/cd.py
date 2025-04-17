import os
import sys
import re
import token


"""
def lex(file):
	pass


a = sys.argv[1]

if a[:2] == "--":
	match a[2:]:
		case "lex":
			lex(sys.argv[2])
		case "parse":
			lex(sys.argv[2])
			parse(sys.argv[2])
"""
			
		

prepC = "gcc -E -P " + sys.argv[1] + " -o "

iFile = os.path.dirname(sys.argv[1]) + "/" +  os.path.basename(sys.argv[1]).split('.')[0] + ".i"

prepC = prepC + iFile

if os.system(prepC) == 0:
	#note here you already have a file in the same directory
	#preprocessor file

	with open(iFile, "r") as file:

		buffer = file.read()

		while buffer != r'':
			breakpoint()

			print(buffer)

			is_wspace = r"\s+"
			wspace = re.match(is_wspace, buffer)
			if wspace:
				buffer = wspace.string[wspace.span()[1]:]

			print(buffer)

			is_numeric = r"\d+"
			numeric = re.match(is_numeric, buffer)
			if numeric:
				buffer = numeric.string[numeric.span()[1]:]
				print(buffer)
			else:
				is_alphanumeric = r"[a-zA-Z_]\w+"
				alphanumeric = re.match(is_alphanumeric, buffer)
				if alphanumeric:
					
					match alphanumeric.group():
						case "int":
							#Ta = token.Token(b.group(),TOKENTYPE_INT_KEYWORD) 
							pass
						case "void":
							pass
						case "return":
							pass

					buffer = alphanumeric.string[alphanumeric.span()[1]:]
					print(buffer)
				else:
					is_char = r"[(){};]"
					char = re.match(is_char, buffer)
					if char:
						print(char)
						match char.group():
							case "(":
								pass
							case ")":
								pass
							case "{":
								pass
							case "}":
								pass
							case ";":
								pass
						#aqui tiene que ser keyword
						buffer = char.string[char.span()[1]:]
						print(buffer)
					else:
						if buffer != '':
							print("Error invalid token")




			

		
		
	"""

	#NOTE Here I am looking at the beggining of a word
	b = re.search(r"\bid", a)



	compC = "gcc -S -O -fno-asynchronous-unwind-tables -fcf-protection=none " + iFile + " -o " 
	
	aFile = os.path.dirname(sys.argv[1]) + "/" + os.path.basename(sys.argv[1]).split('.')[0] + ".s"

	print(aFile)
	compC = compC + aFile
	print(compC)
	
	if os.system(compC) == 0:

		#assembly file
		assC = "gcc " + aFile + " -o " + os.path.dirname(sys.argv[1]) + "/" + os.path.basename(sys.argv[1]).split('.')[0]
		
		print(assC)

		os.system(assC)

		os.remove(aFile)
	"""

	os.remove(iFile)


