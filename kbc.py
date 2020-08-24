import sys
#Stores the amount in te variable
money =[5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
#function to print the money
def win_money(correct_answer):
		print(money[correct_answer-1])
		if money[correct_answer-1]==40000:
			print("Congratulation!You have completed first level.")
		elif money[correct_answer-1]==320000:
			print("Congratulation!You have completed second level.")
		elif money[correct_answer-1]==10000000:
			print("Congratulation!You have completed third level.")


def start():
		#Question list for kbc
		question=[
					  "The International Literacy Day is observed on?",
					  "The language of Lakshadweep. a Union Territory of India, is",
					  "Which of the following was the theme of the World Red Cross and Red Crescent Day?",
					  "Green Peace Foundation' is associated with",
					  "Rial is the currency of ?",
					  "Burma was known to ancient Indians as?",
					  "Who among the following wrote 'Glimpses of World History' ?",
					  "Who among the following is the authon of the book 'The Impressionist'?",
					  "Who wrote the line  'A thing of beauty is a joy forever'?",
					  "Ghototkach in Mahabharat was the son of ?",
                      "Which of the following Muslim festivals is based on the 'Holy Quran'? ",
                      "Which city of India was first of all affected by plague?"


				  ]
		# Option for the game
		first_option=[	
						"Sep 8","Tamil",
					  	"Dignity for all - focus on women","france",
					  	"Iran","Suvarnadvipa",
                        "Mahatma Gandhi","Tarun Tejpal",
					  	"P.B. Shelley","Duryodhana",
                        "Id -ul-Zuha","Jaipur"
                        

					 ]
		second_option=[	
						"Nov 28","Hindi",
					   	"Dignity for all - focus on Children","Italy",
					   	"Indonesia","Yavadvipa",
					   	"Rajendra Prasad","Vishriu Bhagat","William Wordsworth",
					   	"Arjuna","Id -ul-Fitr","Bombay"

					  ]
		third_option=[	
						"May 2","Malayalam",
					  	"Focus on health for all","Britain",
					  	"Zambia","Malayamandalam",
					  	"Mulk Raj Anand","Hari Kunzru","John Keats",
					  	"Yudhishthir","Bakri-id","Surat"
					  ]
		fourth_option=[	
						"Sep 22","Telugu",
						"Nourishment for all-focus on children'","West Germany",
						"Namibia","Suvarnabhumi"
						"Jawaharlal Nehru", "George Fernandes", "Robert Browning",
						"Bhima","Moharram","Kanpur"
						]
		#All option are kept in it for easy use 
		all_option=[
					first_option,second_option,
					third_option,fourth_option
					]
		#For iterating till user doesn't gives wrong answer
		wrong_answer=False
		#For counting at which level the user is
		correct_answer=0
		#List for keeping record of all answer in sequence wise
		#ans_key=[1,3,2,1,1,4,4,3,3,4,1,3]
		ans_key=[0,2,1,0,0,3,3,2,2,3,0,2]

		#Games  begins from here 
		while(wrong_answer!=True):
			#variable used to pick the questions from the list
			stage=0
			
			#prints the question from the list
			print("Q."+question[stage])

			#prints the option
			for Number,option in enumerate(all_option):
				print(str(Number+1)+". "+option[stage])
			

			#print Lifelines
			print("Enter Your Option - 1.50-50 2.SKIP 3.NO LIFELINES ")
			op=int(input())
		

			if op==1:
				#print two options
				for Number,option in enumerate(all_option):
					print(str(Number+1)+". "+option[stage])
				
				#Takes the input of the user
				answer=int(input("Write Your Answer: "))

				key = (ans_key[stage]+1)
				#checks if the answer is correct or not
				if  key == answer:
					print("Congratulation! Your answer is right and You have won : Rs", end="")
					correct_answer+=1
					win_money(correct_answer)
				else:
					print("Sadly! You have given wrong answer")
				
					correct_answer=0
					wrong_answer=True
				#checks if it is the last level or not
				if(correct_answer==12):
					break
				stage+=1


			elif op==2:

				stage+=1
				#print another question
				print("Q. "+question[stage])

				#prints the option
				for Number,option in enumerate(all_option):
					print(str(Number+1)+". "+option[stage])
				#Takes the input of the user
				answer=int(input("Write Your Answer: "))

				key = (ans_key[stage]+1)
				#checks if the answer is correct or not
				if  key == answer:
					print("Congratulation! Your answer is right and You have won : Rs", end="")
					correct_answer+=1
					win_money(correct_answer)
				else:
					print("Sadly! You have given wrong answer")
				
					correct_answer=0
					wrong_answer=True
				#checks if it is the last level or not
				if(correct_answer==12):
					break
			
			elif op==3:


				#Takes the input of the user
				answer=int(input("Write Your Answer: "))

				key = (ans_key[stage]+1)
				#checks if the answer is correct or not
				if  key == answer:
					print("Congratulation! Your answer is right and You have won : Rs", end="")
					correct_answer+=1
					win_money(correct_answer)
				else:
					print("Sadly! You have given wrong answer")
				
					correct_answer=0
					wrong_answer=True
					#checks if it is the last level or not
				if(correct_answer==12):
					break
				stage+=1
			
			else:
				print(".............INCORRECT CHOICE..........")
				sys.exit()





def rules():
	print('''\n ==========RULES==========  
    1. Each round consists of 12 random questions.
    To answer, you must press 1,2,3,4.Your final score will be given at the end.
    2. There's no negative point for wrong answers.
    3. There is two lifelines a."50-50" two wrongs answers will be removed b. "SKIP" Your question will be changed by another question for the same amount of money ''')

def about():
	print('''\n==========ABOUT US==========
This project has been created by AKANKSHA GANDHI.
The Classic Quiz Game, Kaun Banega Crorepati (The Indian version of Who wants to be a Millionaire?).
This is a Classic Quiz Game. 12 Questions will be presented to you one by one. Answer your way to win Rs. 1 Crore, and become a 'Crorepati' (Millionaire).
''')

def exit_quiz():
	sys.exit()

    
if __name__=="__main__":
	choice=0
	while choice!=4:
		print("========WELCOME TO KBC GAME========")
		print("------------------------------------")
		print("1. PLAY GAME")
		print("2. SEE THE INSTRUCTIONS HOW TO PLAY THE GAME")
		print("3. ABOUT US")
		print("4. EXIT THE GAME")
		ch=int(input("ENTER YOUR CHOICE:"))
		if ch==1:
			start()
		elif ch==2:
			rules()
		elif ch==3:
			about()
		elif ch==4:
			exit_quiz()
		else:
			print("WRONG INPUT.ENTER THE CHOICE AGAIN")
