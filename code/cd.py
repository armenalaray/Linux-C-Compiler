import os
import sys
import re
#from lexer import *

import lexer
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

printDebugInfo = False
			
if __name__ == "__main__":	
	#a = parser.ConstInt(2147483648)
	#print(a)

	file = ''
	LastStage = "codeEmission"
	NoLink = False
	library = None

	match len(sys.argv):
		case 1:
			#NOTE: no arguments
			pass
		case 2:
			file = sys.argv[1]	
			
		case 3:
			file = sys.argv[2]
			print(type(sys.argv[1]))

			cCommand = sys.argv[1]

			isLibary = r"-l"
			lMatch = re.match(isLibary, cCommand)
			if lMatch:
				cCommand = lMatch.string[lMatch.span()[1]:]
				print(cCommand)

				library = cCommand
			else:
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
	
			tokenList = lexer.Lex(buffer, iFile)

			if printDebugInfo:
				print(tokenList)

			os.remove(iFile)

			if LastStage == 'lex':
				sys.exit(0)

			pro = parser.parseProgram(tokenList)

			if tokenList != []:
				#raise Exception("Syntax Error Extra code inside program. {0}".format(tokenList))
				print("Syntax Error Extra code inside program. {0}".format(tokenList))
				sys.exit(1)

			if printDebugInfo:
				print(pro.printNode(0))

			if LastStage == 'parse':
				sys.exit(0)

			res = semanticAnalysis.IdentifierResolution(pro)

			if printDebugInfo:
				print(res.printNode(0))
			

			typeChekedProgram, symbolTable = typeChecker.typeCheckProgram(res)

			if printDebugInfo:
				print(typeChekedProgram.printNode(0))
				print(symbolTable)

			loo = loopLabeling.labelProgram(typeChekedProgram)

			if printDebugInfo:
				print(loo.printNode(0))

			if LastStage == 'validate':
				sys.exit(0)

			tac = tacGenerator.TAC_parseProgram(loo, symbolTable)

			if printDebugInfo:
				print(tac)
				print(symbolTable)

			if LastStage == 'tac':
				sys.exit(0)

			ass, backSymbolTable = assemblyGenerator.ASM_parseAST(tac, symbolTable)

			if printDebugInfo:
				print(ass)
				print(backSymbolTable)
			
			ReplacePseudoRegisters.ReplacePseudoRegisters(ass, backSymbolTable)

			if printDebugInfo:
				print(ass)

			FixingUpInstructions.FixingUpInstructions(ass)

			if printDebugInfo:
				print(ass)
		

			if LastStage == 'assemblyGeneration':
				sys.exit(0)


			output = codeEmission.outputAsmFile(ass, symbolTable)

			if printDebugInfo:
				print(output)

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
			

	sys.exit(0)
					

	