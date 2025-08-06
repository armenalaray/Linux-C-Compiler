import os
import sys
import re
import ctypes
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
import optimizations
import RegisterAllocation


printDebugInfo = True

file = ''
LastStage = "codeEmission"
NoLink = False
NotAssembly = False


foldConstants = False
propagateCopies = False
eliminateUnreachableCode = False
eliminateDeadStores = False
optimize = False



library = None

def matchCommands(argument):

	global LastStage
	global library
	global NoLink
	global NotAssembly

	global foldConstants
	global propagateCopies
	global eliminateUnreachableCode
	global eliminateDeadStores
	global optimize


	cCommand = argument
	isLibary = r"-l"

	lMatch = re.match(isLibary, cCommand)
	if lMatch:
		cCommand = lMatch.string[lMatch.span()[1]:]
		#print(cCommand)
		library = cCommand
	else:
		match argument:
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
			case "-S":
				NotAssembly = True

			case "--fold-constants":
				foldConstants = True
			
			case "--propagate-copies":
				propagateCopies = True

			case "--eliminate-unreachable-code":
				eliminateUnreachableCode = True

			case "--eliminate-dead-stores":
				eliminateDeadStores = True

			case "--optimize":
				optimize = True

			case _:
				print("Error Invalid command option.")
				sys.exit(1)
"""
def listsAreEqual(optimizedFunctionBody,functionBody):
	for i, j in zip(functionBody, optimizedFunctionBody):
		if i == j:
			pass
		else:
			return False
		
	return True
"""
	
			
def optimizeFunction(functionBody, symbolTable):
	if functionBody == []:
		return functionBody
	
	while True:
		aliasedVars = optimizations.addressTakenAnalysis(functionBody, symbolTable)

		if foldConstants or optimize:
			postConstantFolding = optimizations.constantFolding(functionBody, symbolTable)
		else:
			postConstantFolding = functionBody

		cfg = optimizations.makeControlFlowGraph(postConstantFolding)

		if eliminateUnreachableCode or optimize:
			cfg = optimizations.unreachableCodeElimination(cfg)
		
		if propagateCopies or optimize:
			cfg = optimizations.copyPropagation(cfg, symbolTable, aliasedVars)

		if eliminateDeadStores or optimize:
			cfg = optimizations.deadStoreElimination(cfg, symbolTable, aliasedVars)

		optimizedFunctionBody = optimizations.cfgToInstructions(cfg)

		if optimizedFunctionBody == functionBody or optimizedFunctionBody == []:
			return optimizedFunctionBody

		functionBody = optimizedFunctionBody




if __name__ == "__main__":	

	print(assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM0)) == assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.AX)))

	print(sys.float_info)

	print(len(sys.argv))
	print(sys.argv)
	match len(sys.argv):
		case 1:
			#NOTE: no arguments
			pass
		case 2:
			file = sys.argv[1]	
			
		case 3:
			file = sys.argv[2]			
			matchCommands(sys.argv[1])

		case 4:
			file = sys.argv[3]
			matchCommands(sys.argv[1])
			matchCommands(sys.argv[2])

		case 5:
			file = sys.argv[4]
			matchCommands(sys.argv[1])
			matchCommands(sys.argv[2])
			matchCommands(sys.argv[3])

		case 6:
			file = sys.argv[5]
			matchCommands(sys.argv[1])
			matchCommands(sys.argv[2])
			matchCommands(sys.argv[3])
			matchCommands(sys.argv[4])
		
		case 7:
			file = sys.argv[6]
			matchCommands(sys.argv[1])
			matchCommands(sys.argv[2])
			matchCommands(sys.argv[3])
			matchCommands(sys.argv[4])
			matchCommands(sys.argv[5])

		case 8:
			file = sys.argv[7]
			matchCommands(sys.argv[1])
			matchCommands(sys.argv[2])
			matchCommands(sys.argv[3])
			matchCommands(sys.argv[4])
			matchCommands(sys.argv[5])
			matchCommands(sys.argv[6])

		case 9:
			file = sys.argv[8]
			matchCommands(sys.argv[1])
			matchCommands(sys.argv[2])
			matchCommands(sys.argv[3])
			matchCommands(sys.argv[4])
			matchCommands(sys.argv[5])
			matchCommands(sys.argv[6])
			matchCommands(sys.argv[7])

		case 10:
			file = sys.argv[9]
			matchCommands(sys.argv[1])
			matchCommands(sys.argv[2])
			matchCommands(sys.argv[3])
			matchCommands(sys.argv[4])
			matchCommands(sys.argv[5])
			matchCommands(sys.argv[6])
			matchCommands(sys.argv[7])
			matchCommands(sys.argv[8])

		case _:
			print("Error Invalid command option.")
			sys.exit(1)

	#lexonly
	
	print("File:", file)
	print("Last Stage:", LastStage)
	print("NoLink:", NoLink)
	print("NotAssembly:", NotAssembly)

	print("--fold-constants", foldConstants)
	print("--propagate-copies", propagateCopies)
	print("--eliminate-unreachable-code", eliminateUnreachableCode)
	print("--eliminate-dead-stores", eliminateDeadStores)
	print("--optimize", optimize)

	print("Libary:", library)

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
			

			typeChekedProgram, symbolTable, typeTable = typeChecker.typeCheckProgram(res)

			if printDebugInfo:
				print(typeChekedProgram.printNode(0))
				print("Type Table:\n", typeTable)
				print("Symbol Table:\n", symbolTable)

			loo = loopLabeling.labelProgram(typeChekedProgram)

			if printDebugInfo:
				print(loo.printNode(0))

			if LastStage == 'validate':
				sys.exit(0)

			tac = tacGenerator.TAC_parseProgram(loo, symbolTable, typeTable)


			if printDebugInfo:
				print(tac)
				print("Type Table:\n", typeTable)
				print("Symbol Table:\n", symbolTable)

			
			for i in tac.topLevelList:
				#print(type(i))
				match i:
					case tacGenerator.TAC_FunctionDef():
						print("OPTIMIZING FUNCTION {0}".format(i))
						i.instructions = optimizeFunction(i.instructions, symbolTable)
				
				#breakpoint()
			
			
			
			allAliasedVars = set()
			for i in tac.topLevelList:
				#print(type(i))
				match i:
					case tacGenerator.TAC_FunctionDef():		
						aliasedVars = optimizations.addressTakenAnalysis(i.instructions, symbolTable)
						allAliasedVars.update(aliasedVars)
			
			if printDebugInfo:
				print(tac)
				print("Type Table:\n", typeTable)
				print("Symbol Table:\n", symbolTable)
				print("All Aliased Vars:\n", allAliasedVars)

			if LastStage == 'tac':
				sys.exit(0)

			

			ass, backSymbolTable = assemblyGenerator.ASM_parseAST(tac, symbolTable, typeTable)

			if printDebugInfo:
				print(ass)
				print("Type Table:\n", typeTable)
				print("Backend Symbol Table:\n", backSymbolTable)

			#Register Allocator
			for i in ass.topLevelList:
				match i:
					case assemblyGenerator.Function():
						print("REGISTER ALLOCATE FUNCTION {0}".format(i.identifier))
						i.insList = RegisterAllocation.allocateRegisters(i.insList, symbolTable, backSymbolTable, allAliasedVars, i.identifier)

			
			ReplacePseudoRegisters.ReplacePseudoRegisters(ass, backSymbolTable)

			if printDebugInfo:
				print(ass)

			

			FixingUpInstructions.FixingUpInstructions(ass, backSymbolTable)

			if printDebugInfo:
				print(ass)
						
		
			if LastStage == 'assemblyGeneration':
				sys.exit(0)
			

			
			output = codeEmission.outputAsmFile(ass, backSymbolTable)

			if printDebugInfo:
				print(output)

			#ASSEMBLER
			asmFile = os.path.dirname(file) + "/" + os.path.basename(file).split('.')[0] + '.s'
			#print(asmFile)
			aFile = open(asmFile, 'w')
			aFile.write(output)
			aFile.close()

			if NotAssembly:
				sys.exit(0)

			if NoLink:
				assC = "gcc -ggdb -c " + asmFile + " -o " + os.path.dirname(file) + "/" + os.path.basename(file).split('.')[0] + '.o'

				print(assC)

				os.system(assC)

				pass
			else:	
				assC = "gcc -ggdb " + asmFile + " -o " + os.path.dirname(file) + "/" + os.path.basename(file).split('.')[0]

				if library:
					assC += ' -lm'
				
				print(assC)

				os.system(assC)
			
			

	sys.exit(0)
					

	