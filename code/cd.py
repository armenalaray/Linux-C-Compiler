import os
import sys
from lexer import *

import parser
import assemblyGenerator
import codeEmission
import semanticAnalysis
import tacGenerator
import typeChecker
import loopLabeling
import ReplacePseudoRegisters
import FixingUpInstructions
import ASTDebug

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
	#a = parser.ConstInt(2147483648)
	#print(a)

	file = ''
	LastStage = "codeEmission"
	NoLink = False

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
				case "--validate":
					LastStage = "validate"
				case "--tacky":
					LastStage = "tac"
				case "--codegen":
					LastStage = "assemblyGeneration"
				case "-c":
					NoLink = True
				case _:
					print("Error Invalid command option.")
					sys.exit(1)

		case 4:
			file = sys.argv[3]
			#como sabes que no modificaste el mismo

			#if sys.argv[2] == sys.argv[1]:


			match sys.argv[1]:
				case "--lex":
					LastStage = "lex"
				case "--parse":
					LastStage = "parse"
				case "--validate":
					LastStage = "validate"
				case "--tacky":
					LastStage = "tac"
				case "--codegen":
					LastStage = "assemblyGeneration"
				case "-c":
					NoLink = True
					pass
				case _:
					print("Error Invalid command option.")
					sys.exit(1)

			match sys.argv[2]:
				case "--lex":
					LastStage = "lex"
				case "--parse":
					LastStage = "parse"
				case "--validate":
					LastStage = "validate"
				case "--tacky":
					LastStage = "tac"
				case "--codegen":
					LastStage = "assemblyGeneration"
				case "-c":
					NoLink = True
					pass
				case _:
					print("Error Invalid command option.")
					sys.exit(1)

		case _:
			print("Error Invalid command option.")
			sys.exit(1)

	#lexonly
	
	print("File: ", file)
	print("Last Stage: ", LastStage)
	print("NoLink: ", NoLink)

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

			print(pro.printNode(0))

			if LastStage == 'parse':
				sys.exit(0)

			res = semanticAnalysis.IdentifierResolution(pro)

			print(res.printNode(0))
			

			typeChekedProgram, symbolTable = typeChecker.typeCheckProgram(res)

			print(typeChekedProgram.printNode(0))

			print(symbolTable)

			loo = loopLabeling.labelProgram(typeChekedProgram)

			print(loo.printNode(0))
			#print(loo)

			if LastStage == 'validate':
				sys.exit(0)

			tac = tacGenerator.TAC_parseProgram(loo, symbolTable)

			print(tac)

			print(symbolTable)

			if LastStage == 'tac':
				sys.exit(0)

			ass = assemblyGenerator.ASM_parseAST(tac, symbolTable)

			print(ass)
			
			ReplacePseudoRegisters.ReplacePseudoRegisters(ass, symbolTable)

			print(ass)

			FixingUpInstructions.FixingUpInstructions(ass)

			print(ass)
		

			if LastStage == 'assemblyGeneration':
				sys.exit(0)


			output = codeEmission.outputAsmFile(ass, symbolTable)

			asmFile = os.path.dirname(file) + "/" + os.path.basename(file).split('.')[0] + '.s'
			#print(asmFile)
			aFile = open(asmFile, 'w')
			aFile.write(output)
			aFile.close()

			if NoLink:
				assC = "gcc -c " + asmFile + " -o " + os.path.dirname(file) + "/" + os.path.basename(file).split('.')[0] + '.o'

				print(assC)

				os.system(assC)

				pass
			else:	
				assC = "gcc " + asmFile + " -o " + os.path.dirname(file) + "/" + os.path.basename(file).split('.')[0]
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
