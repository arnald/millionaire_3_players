import random
import collections


class Level(object):

    def __init__(self, questions, possible_answers, answers):
        self.questions = questions
        self.possible_answers = possible_answers
        self.answers = answers

    def Q_info(self):
        # Returns the question, the list of possible answers, and the correct answers

        # picks a random question from available questions
        i = random.randint(1, len(self.questions))
        ans_key = collections.OrderedDict()
        choices = self.possible_answers[i]
        j = 0

        for ans in choices:
            ans_key[chr(65 + j)] = ans
            j += 1

        output = [self.questions[i], ans_key, self.answers[i]]
        return output


def level_1():
    # Lists containing questions, mutliple-choice options, and answers
    questions = {1: "Σε ποια πόλη βρίσκεται το Εθνοκό Καυτατζόγλειο Στάδιο?",
                 2: "Τι είναι το κασέρι?",
                 3: "Ποιος σκότωσε τον Άβελ?",
                 4: "Ποιο είναι το μεγαλύτερο νησί τον Επτανήσων?",
                 5: "Ποιό είναι το σύμβολο των Χριστιανών?"}
    possible_answers = {1: ['Θεσσαλονίκη', 'Αθήνα', 'Λάρισα', 'Αλεξανδρούπολη'],
                        2: ['Σάλτσα', 'Τυρί', 'Γλυκό',
                            'Σαλάτα'],
                        3: ['Ισαάκ', 'Κάιν', 'Αβραάμ', 'Αδάμ'],
                        4: ['Κεφαλλονιά', 'Ζάκυνθος', 'Κέρκυρα', 'Μεγανήσι'],
                        5: ['Περιστέρι', 'Σταυρός', 'Κερί', 'Ευαγγέλιο']}
    answers = {1: 'Θεσααλονίκη', 2: 'Τυρί', 3: 'Κάιν', 4:'Κεφαλλονιά', 5:'Σταυρός'}

    lvl = Level(questions, possible_answers, answers)

    return lvl.Q_info()


def level_2():
    # Lists containing questions, mutliple-choice options, and answers
    questions = {1: "Πώς αλλιώς ονομάζεται το Καλλιμάρμαρο?",
                 2: "Πού ζει σύμφωνα με τον μύθο, το περιβόητο τέρας του Λουχ Νες",
                 3: "Πώς ονομάζεται η συσκευή με την οποία μετράμε την ατμοσφαιρική πίεση?",
                 4: "Σε ποιο απο τα παρακάτω διαστημικά σώματα δεν έχει προσεδαφιστεί ποτέ διαστημική αποστολή?",
                 5: "Ποια είναι η πρώτη ελληνική ομάδα που κατέκτησε το ευρωπαικό το 1996?"}
    possible_answers = {1: ['ΣΕΦ', 'ΟΑΚΑ', 'Παναθηναϊκό Στάδιο', 'Γεώργιος Καραϊσκάκης'],
                        2: ['Ισλανδία', 'Ολλανδία', 'Σκωτία', 'Ιρλανδία'],
                        3: ['Βαρόμετρο', 'Ανεμόμετρο', 'Ταχογράφος', 'Πιεσόμετρο'],
                        4: ['Αφροδίτη', 'Ερμή', 'Σελήνη', 'Άρη'],
                        5: ['Άρης', 'ΠΑΟΚ', 'Παναθηναϊκός', 'Πανιώνιος']}
    answers = {1: 'Παναθηναϊκό Στάδιο', 2: 'Σκωτία', 3: 'Βαρόμετρο', 4:'Ερμή', 5:'Παναθηνάϊκός'}

    lvl = Level(questions, possible_answers, answers)

    return lvl.Q_info()


def level_3():
    # Lists containing questions, mutliple-choice options, and answers
    questions = {1: "Ποιό έτος συνέβη η έξοδος του Μεσολογγίου?",
                 2: "Ποιος σκηνοθέτησε τπ 1979 την ταινία επιστημονικής φαντασάς 'Allien'?",
                 3: "Ποιος μυθικός ήρωας έδωσε την φωτιά στους ανθρώπους?",
                 4: "Από ποιά χώρα προέρχεται το μπρέτσελ?",
                 5: "Πώς ονομάστηκε ο πρώτος ηλεκτρονικός υπολογιστής"}
    possible_answers = {1: ['1825', '1824', '1826', '1827'],
                        2: ['Στίβεν Σπίλβεργκ', 'Γκιγκέρμο Ντελ Τόρο', 'Ρίντλει Σκοτ', 'Φράνκ Ντάραμποντ'],
                        3: ['Ιδομενέας', 'Μενέλαος', "Αχιλλέας",
                            'Προμηθέας'],
                        4:['Τσεχία', 'Γερμανία', 'Ουγγαρία', 'Άυστρία'],
                        5:['HAL', 'Dvorac', 'Apple 1', 'ENIAC']}
    answers = {1: '1826', 2: 'Ρίντλει Σκοτ', 3: 'Προμηθέας', 4:'Αυστρία', 5:'ENIAC'}

    lvl = Level(questions, possible_answers, answers)

    return lvl.Q_info()


def level_4():
    # Lists containing questions, mutliple-choice options, and answers
    questions = {1: "Πού βρίσκεται το κτίριο La Pedrera του Γκαουντί?",
                 2: "Πόσοι Αμερικανοί αστροναύτες έχουν πατήσει στη Σελήνη?'",
                 3: "Ποιο ετος κυκλοφόρησε το κινητό τηλέφωνο Samsung Galaxy S5?",
                 4: "Ποια είναι η πρωτευουσα της Ελβετίας ?",
                 5: "Ποιος κατασκεύασε τον πρώτο ηλεκτρικό λαμπτήρα ?"}
    possible_answers = {
        1: ['Βαρκελώνη', 'Μάλαγα', 'Σεβίλλη', 'Μαδρίτη'],
        2: ['6', '12', '8', '3'],
        3: ['2012', '2011', '2014', '2013'],
        4: ['Λωζάνη', 'Γενεύη', 'Βέρνη', 'Ζυρίχη'],
        5: ['Έντισον', 'Κίρχοφ', 'Φαραντέι', 'Τζουλ']}
    answers = {1: 'Βαρκελώνη', 2: '12', 3: '2014', 4:'Βέρνη', 5:'Έντισον'}

    lvl = Level(questions, possible_answers, answers)

    return lvl.Q_info()


def level_5():
    # Lists containing questions, mutliple-choice options, and answers
    questions = {
        1: "Ποιος πάτησε πρώτος στον Νότιο Πόλο?",
        2: "Που βρίσκεται η πόλη Μοντρέ?",
        3: "Ποιά ήταν η πρώτη ταινία που δημιουργήθηκε αποκλειστικά με χρήση υπολογιστή ?",
        4: "Ποιά από τις παρακάτω κλίμακες δεν μπορεί να πάρει αρνητικές τιμές ?",
        5: "Ποιος είναι ο μεγαλύτερος ποταμός της Ευρώπης ?"}
    possible_answers = {1: ['Βίλχεμ', 'Αμούδσεν', 'Καργκελόν', 'Κουκ'],
                        2: ['Αυστρία', 'Γαλλία', 'Ελβετία', 'Ιταλία'],
                        3: ['Toy Story', 'Lilo & Stich', 'Final Destiny', 'Ice Age'],
                        4: ['Κλίμακα Κελσίου', 'Κλιμακα Φαρενάιτ', 'Κλίμακα Ρίχτερ', 'Κλίμακα Κέλβιν'],
                        5: ['Βιστούλας', 'Ρήνος', 'Δούναβης', 'Βόλγας']}
    answers = {1: 'Αμούδσεν', 2: 'Ελβετία', 3: 'Toy Story', 4: 'Κλίμακα Κέλβιν', 5: 'Βόλγας'}

    lvl = Level(questions, possible_answers, answers)

    return lvl.Q_info()


def level_6():
    # Lists containing questions, mutliple-choice options, and answers
    questions = {1: "Σε ποιον πλανήτη τέθηκε σε τροχία το διαστημικό όχημα Galileo το 1995?",
                 2: "Από ποιά χώρα καταγόταν ο Σιγκμουντ Φρόυντ?",
                 3: "Στο Wimbledon του 2010, το μεγαλύτερο χρονικά αγώνας τέννις διήρκησε?",
                 4: "Ποιο από τα παρακάτω σωματίδια έχει τη μικρότερη μάζα ?",
                 5: "Ποιό είναι το νόμισμα της Ρουμανίας ?"}
    possible_answers = {1: ['Ουρανό', 'Δία', 'Κρόνο', 'Ερμή'],
                        2: ['Γερμανία', 'Ελβετία', 'Βέλγιο', 'Αυστρία'],
                        3: ['6 hrs, 11 min', '8 hrs, 24 min', '11 hrs, 5 min', '3 hours, 42 min'],
                        4: ['Άτομο Οξυγόνου', 'Μόριο Νερού', 'Άτομο υδρογόνου', 'Πυρήνας ατόμου υδρογόνου'],
                        5: ['Σλότι', 'Λεβ', 'Ευρώ', 'Λέου']}
    answers = {1: 'Δία', 2: 'Αυστρία', 3: '11 hrs, 5 min', 4:'Πυρήνας ατόμου υδρογόνου', 5: 'Λέου'}

    lvl = Level(questions, possible_answers, answers)

    return lvl.Q_info()


def level_7():
    # Lists containing questions, mutliple-choice options, and answers
    questions = {1: "Πώς ονομαζόταν ο πρώτος δορυφόρος που έθεσαν σε τροχιά οι ΗΠΑ το 1958?",
                 2: "Ποιά από τις παρακάτω χώρες παρέμεινα επίσημα ουδέτερη και στους 2 Παγκόσμιους Πολέμους?",
                 3: "Σε ποιά ευρωπαϊκή χώρα ανήκει η χερσόνησος Καρπάσου ?",
                 4: "Ποιός Ισπανός Εξερευνητής κατέκτησε την Αυτοκρατορία των Ατζέκων"}
    possible_answers = {1: ['Voyager 1', 'Explorer 2', 'Explorer 1', 'Mariner 1'],
                        2: ['Νορβηγία', 'Σουηδία', 'Κούβα', 'Ελλάδα'],
                        3: ['Κύπρο', 'Ιταλία', 'Ισπανία', 'Ελλάδα'],
                        4: ['Φρανσίνσο Πισσάρο', 'Βάσκο Νούνιες ντε Μπαλμπόα', 'Χριστόφορος Κολόμβος', 'Ερνάν Κορτές']}
    answers = {1: 'Riley', 2: 'Σουηδία', 3: 'Κύπρος', 4: 'Ερνάν Κορτές'}

    lvl = Level(questions, possible_answers, answers)

    return lvl.Q_info()


def level_8():
    # Lists containing questions, mutliple-choice options, and answers
    questions = {1: "Τι είδους υλικά χρησιμοποιήθηκαν για την κατασκευη του μανδύα αορατότητας?",
                 2: "Ποιά ασθένεια είναι γνωστή 'νόσος του Χάνσεν' ?",
                 3: "Σε ποιά πόλη βρίσκονται τα 'φυλακισμένα μνήματα'?",
                 4: "Σε ποιά χώρα πρωτοεμφανίστηκε το κουνουπίδι ?",
                 5: "Ποιά είναι η πρωτεύουσα της Αιτής ?"}
    possible_answers = {1: ['Πλέξιγκλας', 'Ευφυή Υλικά', 'Κεραμικά', 'Μετα-Υλικά'],
                        2: ['Χολέρα', 'Πνευμονία', 'Ηπατίτιδα', 'Λέπρα'],
                        3: ['Αμμόχωστο', 'Λευκωσία', 'Λάπήθο', 'Πάφο'],
                        4: ['Μεξικό', 'Ινδία', 'Ισπανία', 'Κύπρο'],
                        5: ['Πορτ Σάιντ', 'Πόρτο Λάγο', 'Πορτ-ο-Πρένς', 'Πόρτο Ρίκο']}
    answers = {1: 'Μετα-Υλικά', 2: 'Λέπρα', 3: 'Λευκωσία', 4: 'Κύπρο', 5:'Πορτ-ο-Πρένς'}

    lvl = Level(questions, possible_answers, answers)

    return lvl.Q_info()


def level_9():
    # Lists containing questions, mutliple-choice options, and answers
    questions = {1: "Ποιος ζωγράφισε το παρεκκλήσι της Καπέλα Σιστίνα ?",
                 2: "Τι είναι η 'αρια' σε μία όπερα?",
                 3: "Σε ποια χώρα αμφανίστηκε για πρώτη φορά το παιχνίδι PacMan ?"}
    possible_answers = {1: ['Μιχαήλ Άγγελος', 'Ραφαήλ', 'Ντονατέλλο', 'Τιτσιάνο'],
                        2: ['Το σενάριό της', 'Η πρωταγωνίστρια', 'Τραγούδι', "Διάλογος"],
                        3: ['ΗΠΑ', 'Ιαπωνία', 'Κορέα', 'Γερμανία']}
    answers = {1: 'Μιχαήλ Άγγελος', 2: 'Τραγούδι', 3: 'Ιαπωνία'}

    lvl = Level(questions, possible_answers, answers)

    return lvl.Q_info()


def level_10():
    # Lists containing questions, mutliple-choice options, and answers
    questions = {
        1: "Ποια είναι η μικρότερη πολιτεία των ΗΠΑ ?",
        2: "Στην τανία 'Good Will Hunting,' το πρώτο πρόβλημα που έλυσε ο Will, σε ποιον μαθηματικό ανήκε?",
        3: "Ποιό έτος δημιουργήθηκε το λειτουργικό σύστημα DOS?"}
    possible_answers = {1: ['Κονεκτικατ', 'Ντέλαγουερ', 'Ρόουντ Άιλαντ', 'Νιου Τζέρσει'],
                        2: ['Joseph Fourier', 'Leonhard Euler', 'Carl Gauss', 'Fibonacci'],
                        3: ["1988", "1981", "1986", "1984"]}
    answers = {1: 'Pineapple', 2: 'Joseph Fourier', 3: "1981"}

    lvl = Level(questions, possible_answers, answers)

    return lvl.Q_info()

def level_11():
    # Lists containing questions, mutliple-choice options, and answers
    questions = {
        1: "Ποιά είναι η ηλικία του Σύμπαντος?",
        2: "Το νησί της Μαργαρίτας, στον ποταμό Δούναβη, βρίσκεται στην πόλη ...?",
        3: "Σε ποια χώρα αμφανίστηκε για πρώτη φορά το παιχνίδι PacMan ?"}
    possible_answers = {1: ['6,3 δις', '17,8 δις', '13,8 δις', '2,1 δις'],
                        2: ['Ουλμ', 'Μπρατισλάβα', 'Βουδαπέστη', 'Λιντς'],
                        3: ['ΗΠΑ', 'Ιαπωνία', 'Κορέα', 'Γερμανία']}
    answers = {1: '13,8 δις', 2: 'Βουδαπέστη', 3: "Ιαπωνία"}

    lvl = Level(questions, possible_answers, answers)

    return lvl.Q_info()