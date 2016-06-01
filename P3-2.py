t1= []

vect2= []

vectSub=[]

vectPsub=[]



def subtract(v1, v2):

	for i in range (0,5):

		vectSub.append(v1[i]-v2[i])

	return vectSub



def powerSubtract(v1):

	for i in v1:

		vectPsub.append(i**2)

	return vectPsub





def start():

	for i in range (0,5):

		b=input("Ingrese un numero")

		vect1.append(b)



	for i in range (0,5):

		b=input("Ingrese un numero")

		vect2.append(b)



	subtr=subtract(vect1, vect2)

	print(subtr)

	Psubtr=powerSubtract(subtr)

	print(Psubtr)

start()

