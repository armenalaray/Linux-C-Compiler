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

def convertToInt(value):
	return int(value)

def constantFolding(functionBody):

	print("OLD LIST", functionBody)

	newList = []

	for i in functionBody.instructions:

		match i:
			case tacGenerator.TAC_UnaryInstruction(operator = operator, src = src,dst = dst):

				match src:
					case tacGenerator.TAC_ConstantValue(const = const):
						
						match const:
							case parser.ConstDouble():
								pass

							case parser.ConstChar():
								pass

							case parser.ConstUChar():
								pass

							case parser.ConstInt(int = int):

								match operator.operator:

									case tacGenerator.UnopType.NEGATE:
										
										print(operator.operator, -int)

										new = tacGenerator.TAC_ConstantValue(parser.ConstInt(-const.int))
										
										newList.append(tacGenerator.TAC_CopyInstruction(new, dst))

									case tacGenerator.UnopType.COMPLEMENT:
										
										#a = ctypes.c_int32(const.int)
										print(operator.operator, ~int)

										new = tacGenerator.TAC_ConstantValue(parser.ConstInt(~const.int))
										
										newList.append(tacGenerator.TAC_CopyInstruction(new, dst))
										

									case tacGenerator.UnopType.NOT:

										print(operator.operator, not int)

										value = 0

										if not int:
											value = 1
										else:
											value = 0

										new = tacGenerator.TAC_ConstantValue(parser.ConstInt(value))
										
										newList.append(tacGenerator.TAC_CopyInstruction(new, dst))

								

							case parser.ConstLong():
								pass
							
							case parser.ConstUInt():
								pass

							case parser.ConstULong():
								pass

						#estos son todos los const

					case _:
						newList.append(i)
						

			case tacGenerator.TAC_BinaryInstruction(operator = operator, src1 = src1, src2 = src2, dst = dst):
				match src1, src2:
					case tacGenerator.TAC_ConstantValue(const = const1), tacGenerator.TAC_ConstantValue(const = const2):
						#aqui todos son int!
						match const1, const2:
							case parser.ConstInt(int = int1), parser.ConstInt(int = int2):
								
								
								match operator.operator:
									case tacGenerator.BinopType.ADD:
										print(operator.operator, type(const1), type(const2))

										temp = ctypes.c_int32(convertToInt(int1 + int2))

										new = tacGenerator.TAC_ConstantValue(parser.ConstInt(temp.value))
										
										newList.append(tacGenerator.TAC_CopyInstruction(new, dst))

									case tacGenerator.BinopType.SUBTRACT:
										print(operator.operator, type(const1), type(const2))

										temp = ctypes.c_int32(convertToInt(int1 - int2))

										new = tacGenerator.TAC_ConstantValue(parser.ConstInt(temp.value))
										
										newList.append(tacGenerator.TAC_CopyInstruction(new, dst))

									case tacGenerator.BinopType.MULTIPLY:
										print(operator.operator, type(const1), type(const2))

										temp = ctypes.c_int32(convertToInt(int1 * int2))

										new = tacGenerator.TAC_ConstantValue(parser.ConstInt(temp.value))
										
										newList.append(tacGenerator.TAC_CopyInstruction(new, dst))

									case tacGenerator.BinopType.DIVIDE:
										print(operator.operator, type(const1), type(const2))
										
										temp = ctypes.c_int32(convertToInt(int1 / int2))

										new = tacGenerator.TAC_ConstantValue(parser.ConstInt(temp.value))
										
										newList.append(tacGenerator.TAC_CopyInstruction(new, dst))

									case tacGenerator.BinopType.REMAINDER:
										print(operator.operator, type(const1), type(const2))
										
										temp = ctypes.c_int32(convertToInt(int1 % int2))

										new = tacGenerator.TAC_ConstantValue(parser.ConstInt(temp.value))
										
										newList.append(tacGenerator.TAC_CopyInstruction(new, dst))

								

								
						
				

			case tacGenerator.TAC_JumpIfZeroInst():
				pass
			
			case tacGenerator.TAC_JumpIfNotZeroInst():
				pass

			case _:
				newList.append(i)

	functionBody.instructions = newList

	print("NEW LIST", functionBody)

			
	

def makeControlFlowGraph(functionBody):
	pass

def unreachableCodeElimination(cfg):
	pass

def copyPropagation(cfg):
	pass

def deadStoreElimination(cfg):
	pass

def cfgToInstructions(cfg):
	pass


def optimizeFunction(functionBody):
	if functionBody.instructions == []:
		return functionBody
	
	while True:
		postConstantFolding = None

		if foldConstants:
			postConstantFolding = constantFolding(functionBody)
		else:
			postConstantFolding = functionBody

		cfg = makeControlFlowGraph(postConstantFolding)

		if eliminateUnreachableCode:
			cfg = unreachableCodeElimination(cfg)
		
		if propagateCopies:
			cfg = copyPropagation(cfg)

		if eliminateDeadStores:
			cfg = deadStoreElimination(cfg)

		
		optimizedFunctionBody = cfgToInstructions(cfg)

		if optimizedFunctionBody == functionBody or optimizedFunctionBody.instructions == []:
			return optimizedFunctionBody

		functionBody = optimizedFunctionBody



if __name__ == "__main__":	
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
				print(type(i))
				match i:
					case tacGenerator.TAC_FunctionDef():
						optimizeFunction(i)


			if LastStage == 'tac':
				sys.exit(0)

			ass, backSymbolTable = assemblyGenerator.ASM_parseAST(tac, symbolTable, typeTable)

			if printDebugInfo:
				print(ass)
				print("Type Table:\n", typeTable)
				print("Backend Symbol Table:\n", backSymbolTable)

			#breakpoint()
			#a = backSymbolTable['tmp.14']
			ReplacePseudoRegisters.ReplacePseudoRegisters(ass, backSymbolTable)

			if printDebugInfo:
				print(ass)

			
			FixingUpInstructions.FixingUpInstructions(ass)

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
					

	