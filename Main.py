print("You're at your first hackathon! You just passed through registration and it's time to explore.")
print()
print('Choose your steps(enter number for corresponding choice)')
print('1. Continue through registration hall to next building')
print('2. Talk to volunteers that you see nearby')
first_choice = eval(input('>'))
if first_choice == 1:
    print('You have made you way to the main atrium')
    print('1. Show bracelet and get some lunch')
    print('2. Approach sponsor booths')
    second_choice = eval(input('>'))
    if second_choice == 1:
        print('You fill your plate with food, find a spot to sit and enjoy')
        print('1.Go look for people who are into similar things as you and start networking a team')
        print('2.Start hacking and ignore the opening ceremony. You are here to WIN!')
        print('3.Maybe you can learn something interesting at the opening ceremonies')
        third_choice = eval(input('>'))
        if third_choice == 3:
            print("Proceed to the opening ceremony")
    elif second_choice == 2:
        print('There are a lot of interesting sponsors showing things which should make creating an app or website much easier!')
        print('1.Collect some free swag and see whats being offered')
        print('2.Ask them for some advice and ways of coming up with great ideas')
        third_choice = eval(input('>'))
        if third_choice == 2:
            print('Talk to people, maybe visit a tech talk and see what resources are available')

elif first_choice == 2:
    print('What can I help you with?')
    print('1. I need help coming up with an idea for what to build')
    print('2. This is my first hackathon, I am not sure what to do')
    second_choice = eval(input('>'))
    if second_choice == 1:
        print('There is a lot you can do, I would recommend talking to some sponsors or \n looking for people to make a team with')
        print('1.Start brainstorming your daily activites and try to improve them by \n developing something relative.')
        third_choice = eval(input('>'))
        if third_choice == 1:
            print('There are many mentors and sponsors that can help you with that.')
