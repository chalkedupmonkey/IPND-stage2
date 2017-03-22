
"""
    https://learnpythonthehardway.org/book/ex39.html
    Dictionaries are much more intuitive than lists.
    Can call anything.
"""

tests = {   'guns':         """ \n The four rules of gun safety:
                                \n 1) All guns are always __1__.
                                \n 2) Never let the __2__ cover anything you are not willing to destroy.
                                \n 3) Keep your finger off the __3__ until your sights are on the target.
                                \n 4) Be sure of your __4__ and what is beyond it.
                                \n """,
            'climbing':     """ \n Rock climbing is the activity of climbing up, down, or across rock formations or purpose built climbing walls.
                                \n There are three basic types of rock climbing: bouldering, sport climbing, and traditional climbing.
                                \n In __1__, climbers work short, low routes without a rope for protection and instead use a crash pad.
                                \n For __2__ climbing the climber ascend a wall and clip into bolts pre-drilled into the wall to protect against falls.
                                \n Traditional, or __3__, climbing requires the climber to place their own protection and remove when done.
                                \n Of course, if you are Alex __4__, you don't use any __5__.
                                \n """,
            'mma':          """ \n Mixed Martial Arts is a full contact __1__ sport that allows both __2__ and __3__.
                                \n The first modern MMA event took place at UFC 1, when the __4__ introduced vale tudo to US audiences.
                                \n Originally promoted as a __5__-vs-style competition to determine the best martial art, fighters have since incorporated the most combat __6__ aspects of various martial arts into their training.
                                \n """}


ansbank = { 'guns':            [['loaded'],
                                ['muzzle'],
                                ['trigger'],
                                ['target']],
            'climbing':        [['bouldering'],
                                ['sport'],
                                ['trad'],
                                ['Honnold'],
                                ['protection']],
            'mma':             [['combat'],
                                ['striking'],
                                ['grappling'],
                                ['Gracies'],
                                ['style'],
                                ['effective']]
            }



able = True
difficulty = 1
topic = ""

"""
    Credit to my friend Jeff for suggesting global variables and 'if __name__ == '__main__'
    Fixed counting attempts and rebooting the test hurdles.
"""


#############
# Selection #
#############


def name():

    """
        Asks player for name and outputs a greeting.
    """

    name = raw_input("\nEnter your name: ")
    print "\nHello [%s], welcome to my pretty game." %(name,)


def selecttopic():

    """
        Asks player to choose topic and displays it back to them.
    """

    global topic
    topic = raw_input("\nSelect your topic from the following three: guns, climbing, mma: ")
    while topic not in tests:
        topic = raw_input("\nPlease select from the following: guns, climbing, mma: ")
    return topic
    print "\nYour chosen topic is " + topic + "."


def selectlevel():

    """
        Asks player how many attempts they would like per blank, more than zero but less than ten.
        If player inputs integer outside of permitted range, asks player to choose again.
    """

    global difficulty
    difficulty = raw_input("\nHow many attempts would you like per entry? \n (Choose a number between 0 and 10, exclusive.): ")

    while not difficulty.isdigit() or int(difficulty) < 1 or int(difficulty) > 9:
        difficulty = raw_input("\nPlease enter an integer greater than 0 and less than 10: ")
    return difficulty


def level():

    """
        Displays how many attempts per blank and which level dfficulty that falls in.
    """

    attempts = int(difficulty)
    if 0 < attempts < 4:
        print  "\nYou have chosen the hard setting. You will have " + difficulty + " attempts per entry."
    elif 3 < attempts < 7:
        print "\nYou have chosen the medium setting. You will have " + difficulty + " attempts per entry."
    else:
        print "\nYou have chosen the easy setting. You will have " + difficulty + " attempts per entry."


########
# Game #
########


def check(ansbank, guess):

    """
        Checks whether player input matches answers in answer bank.
        Only piece of code relevant from madlibs.
    """

    for answer in ansbank:
        if guess == answer:
            return True
    return False


def answered(index, test):

    """
        Using check, determines whether to take away an attempt.
        Determines if player can continue using global variable 'able'.
    """

    global able
    attempts = int(difficulty)
    answer = ansbank[topic][index]

    while attempts > 0:
        guess = raw_input("\nWhat goes in __%s__ ?: " % str(index + 1))
        if check(answer, guess):
            print "\n*" * 5
            print "\nCorrect. Let's move on."
            test = test.replace('__%s__' % str(index + 1), guess)
            print test
            break
        elif attempts > 1:
            print "\n*" * 5
            print "\nIncorrect. Try again."
            attempts -= 1
            print "\n", attempts, "attempt(s) left."
        else:
            able = False
            break
    return test


def dotest():

    """
        Runs functions.
        Displays test and ask plater for answers.
        If player uses all attempts, displays consolation message.
        If player successfully completes test, displays victory message.
    """

    name()
    selecttopic()
    selectlevel()
    level()
    test = tests[topic]

    print "\n*" * 5
    print "\nLet's go."
    print test

    """
        Have to give a shoutout to Adam for index in range from the live coding session.
        Really made life much easier.
    """

    for index in range(len(ansbank[topic])):
        test = answered(index, test)
        if not able: break

    if able:
        print "\nCongratulations, you have finished my pretty game."
    else:
        print "\nThat's too bad. You ran out of attempts."

    return able


if __name__ == "__main__":

    """
        Allows test to run on loop.
        Asks if player would like to play again regardless of outcome.
        Breaks loop if player decides not to continue.
    """

    while True:
        dotest()

        """
            Asks if player would like to play again regardless of outcome.
            Breaks loop if player decides not to continue.
        """
        if raw_input("\nPlay again? (Y/N): ") not in ['Y', 'y']:
            print "\nGood bye."
            break
