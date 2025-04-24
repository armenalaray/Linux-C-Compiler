import os
import sys
from ctoken import *

import parser
import assemblyGenerator
import codeEmission

import tacGenerator

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
			
if __name__ == "__main__":	

	file = ''
	LastStage = "codeEmission"

	match len(sys.argv):
		case 1:
			#NOTE: no arguments
			pass
		case 2:
			file = sys.argv[1]
			
			
		case 3:
			file = sys.argv[2]

			match sys.argv[1]:
				case "--lex":
					LastStage = "lex"
				case "--parse":
					LastStage = "parse"
				case "--tacky":
					LastStage = "tac"
				case "--codegen":
					LastStage = "assemblyGeneration"
				case _:
					print("Error Invalid command option.")
					sys.exit(1)

		case _:
			print("Error Invalid command option.")
			sys.exit(1)

	#lexonly
	
	print("File: ", file)
	print("Last Stage: ", LastStage)

	#NOTE: you have an archive
	prepC = "gcc -E -P " + file + " -o "

	iFile = os.path.dirname(file) + "/" +  os.path.basename(file).split('.')[0] + ".i"

	prepC = prepC + iFile

	if os.system(prepC) == 0:
		#note here you already have a file in the same directory
		#preprocessor file

		with open(iFile, "r") as preprocessedfile:

			buffer = preprocessedfile.read()
	
			tokenList = Lex(buffer)

			os.remove(iFile)
			if LastStage == 'lex':
				sys.exit(0)

			pro = parser.parseProgram(tokenList)

			if tokenList != []:
				#raise Exception("Syntax Error Extra code inside program. {0}".format(tokenList))
				print("Syntax Error Extra code inside program. {0}".format(tokenList))
				sys.exit(1)
			
			print(pro)

			if LastStage == 'parse':
				sys.exit(0)

			tac = tacGenerator.TAC_parseProgram(pro)

			print(tac)

			if LastStage == 'tac':
				sys.exit(0)

			ass = assemblyGenerator.ASM_parseAST(tac)

			print(ass)

			offset = assemblyGenerator.ReplacePseudoRegisters(ass)

			print(ass)

			assemblyGenerator.FixingUpInstructions(ass, offset)

			print(ass)

			if LastStage == 'assemblyGeneration':
				sys.exit(0)


			output = codeEmission.outputAsmFile(ass)

			asmFile = os.path.dirname(file) + "/" + os.path.basename(file).split('.')[0] + '.s'
			#print(asmFile)
			aFile = open(asmFile, 'w')
			aFile.write(output)
			aFile.close()

			
			#assembly file
			assC = "gcc " + asmFile + " -o " + os.path.dirname(file) + "/" + os.path.basename(file).split('.')[0]
			
			#print(assC)

			os.system(assC)
			
			
			
		"""
		print(pro.function.iden)
		print(pro.function.statement)
		print(pro.function.statement.expression.intValue)
		"""

	sys.exit(0)
					

			
			
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
