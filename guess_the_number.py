import random

def guess_the_number():
number_to_guess =
random.randit(1,  100)
attempts = 0
guess = none


print("Ես մտածել եմ 1-ից
100-ի միյև թվի մասին։ ՌՒնեք 10 փռրձ։ ")

  while attempts < 10 and guess ! = number_to_guess:
             guess =
	int(input("Գուշակեք թիվը։ "))
	          attempts += 1
			  
		      if guess <
  number_to_guess:
              print("Լավ! ձեր
  գուշակած թիվը փոքր է։")
           elif guess >
  number_to_guess:
            print("Լավ ! ձեր
  գուշակած թիվը մեծ է։")
  
  
  print(f"Շնորհակալություն! Դուք
  ճիշտ Գուշակեցիք թիվը
  {number_to_guess} - ը {attempts}
  փռրձումից հետո։")
  
  
       if guess != number_to_guess:
	       print(f"Դուք չկարողացաք
  գուշակել, ճիշտ թիվը
  {number_to_guess} էր։")
  
  guess_the_number()
  