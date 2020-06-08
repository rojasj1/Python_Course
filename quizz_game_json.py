print("This program works with requesting http requests using json")

import json
import requests
import pprint
import random
import html

winning_points = 0
loser_points = 0
url = "https://opentdb.com/api.php?amount=1&category=31&difficulty=easy&type=multiple"
endgame =  ""

while endgame != "quit":
              r = requests.get(url)
              if (r.status_code != 200):
                            endgame = input("Sorry there was a problem recieving the question. Press Enter to try again or type 'quit' to quit the game.")
              else:
                            valid_answer = False
                            answer_number = 1
                            data = json.loads(r.text)
                            question = data['results'][0]['question']
                            answers = data['results'][0]['incorrect_answers']
                            correct_answer = data['results'][0]['correct_answer']
                            answers.append(correct_answer)
                            random.shuffle(answers)

                            print(html.unescape(question) +"\n")

                            for answer in answers:
                                          print(str(answer_number)+ "- "+html.unescape(answer))
                                          answer_number += 1

                            while valid_answer == False:
                                          user_answer = input("\nType Type the number of the correct answer: ")
                                          try:
                                                        user_answer = int(user_answer)
                                                        if user_answer > len(answers) or user_answer <= 0:
                                                                      print("Invaid Entry. Only accepted numbers 1 - 4")
                                                        else:
                                                                      valid_answer = True                     
                                          except:
                                                        print("Invalid Entry. Use only numbers.") 
                                          
                                          
                            user_answer =  answers[int(user_answer)-1]

              if user_answer == correct_answer:
                            print("Correct! The answer was " +html.unescape(correct_answer))
                            winning_points += 1
              else:
                            print("Oh! So close! "+html.unescape(user_answer)+ " is incorrect! The correct answer is "+html.unescape(correct_answer)+"!")
                            loser_points += 1
              print("\n####################################")
              print("You have a total score of: ",(winning_points - loser_points))
              print("Correct answers: "+str(winning_points))
              print("Incorrect answers: "+str(loser_points))
              print("\####################################")
                            
              endgame = input("\nPress Enter to play again or type 'quit' to quit the game.").lower()

print("\nThanks for playing!")                            
                            




                          
                             
