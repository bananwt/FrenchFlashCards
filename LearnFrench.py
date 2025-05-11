import random

words = [
    {"french": "le", "english": "the"},
    {"french": "de", "english": "of/from"},
    {"french": "un", "english": "a/an"},
    {"french": "être", "english": "to be"},
    {"french": "et", "english": "and"},
    {"french": "à", "english": "to/at"},
    {"french": "il", "english": "he/it"},
    {"french": "avoir", "english": "to have"},
    {"french": "ne", "english": "not"},
    {"french": "je", "english": "I"},
    {"french": "son", "english": "his/her/its"},
    {"french": "que", "english": "that"},
    {"french": "se", "english": "oneself"},
    {"french": "qui", "english": "who"},
    {"french": "ce", "english": "this/it"},
    {"french": "dans", "english": "in"},
    {"french": "en", "english": "in/on"},
    {"french": "du", "english": "some/of the"},
    {"french": "elle", "english": "she/it"},
    {"french": "au", "english": "to the"},
    {"french": "pour", "english": "for"},
    {"french": "pas", "english": "not"},
    {"french": "vous", "english": "you"},
    {"french": "par", "english": "by"},
    {"french": "sur", "english": "on"},
    {"french": "faire", "english": "to do/make"},
    {"french": "plus", "english": "more"},
    {"french": "dire", "english": "to say"},
    {"french": "me", "english": "me/myself"},
    {"french": "on", "english": "one/we"},
    {"french": "mon", "english": "my"},
    {"french": "lui", "english": "him/her"},
    {"french": "nous", "english": "we/us"},
    {"french": "comme", "english": "like/as"},
    {"french": "mais", "english": "but"},
    {"french": "y", "english": "there"},
    {"french": "leur", "english": "their"},
    {"french": "elle", "english": "she"},
    {"french": "si", "english": "if"},
    {"french": "tout", "english": "all/everything"},
    {"french": "bien", "english": "well"},
    {"french": "où", "english": "where"},
    {"french": "aussi", "english": "also"},
    {"french": "alors", "english": "so/then"},
    {"french": "très", "english": "very"},
    {"french": "avec", "english": "with"},
    {"french": "être", "english": "to be"},
    {"french": "avoir", "english": "to have"},
    {"french": "aller", "english": "to go"},
    {"french": "voir", "english": "to see"},
    {"french": "autre", "english": "other"},
    {"french": "sans", "english": "without"},
    {"french": "tout", "english": "all"},
    {"french": "dire", "english": "to say"},
    {"french": "pouvoir", "english": "can/to be able to"},
    {"french": "vouloir", "english": "to want"},
    {"french": "venir", "english": "to come"},
    {"french": "falloir", "english": "to be necessary"},
    {"french": "voir", "english": "to see"},
    {"french": "demander", "english": "to ask"},
    {"french": "trouver", "english": "to find"},
    {"french": "donner", "english": "to give"},
    {"french": "prendre", "english": "to take"},
    {"french": "rien", "english": "nothing"},
    {"french": "temps", "english": "time"},
    {"french": "jour", "english": "day"},
    {"french": "homme", "english": "man"},
    {"french": "femme", "english": "woman"},
    {"french": "enfant", "english": "child"},
    {"french": "chose", "english": "thing"},
    {"french": "vie", "english": "life"},
    {"french": "main", "english": "hand"},
    {"french": "part", "english": "part"},
    {"french": "oeil", "english": "eye"},
    {"french": "moment", "english": "moment"},
    {"french": "travail", "english": "work"},
    {"french": "mot", "english": "word"},
    {"french": "rue", "english": "street"},
    {"french": "fois", "english": "time (occasion)"},
    {"french": "an", "english": "year"},
    {"french": "monde", "english": "world"},
    {"french": "petit", "english": "small"},
    {"french": "grand", "english": "big"},
    {"french": "nouveau", "english": "new"},
    {"french": "premier", "english": "first"},
    {"french": "dernier", "english": "last"},
    {"french": "bon", "english": "good"},
    {"french": "mauvais", "english": "bad"},
    {"french": "jeune", "english": "young"},
    {"french": "vieux", "english": "old"},
    {"french": "beau", "english": "beautiful"},
    {"french": "fort", "english": "strong"},
    {"french": "important", "english": "important"},
    {"french": "même", "english": "same"},
    {"french": "dernier", "english": "last"},
    {"french": "nouvelle", "english": "news/new"},
    {"french": "encore", "english": "again/still"},
    {"french": "trop", "english": "too much"},
    {"french": "jamais", "english": "never"},
    {"french": "déjà", "english": "already"},
    {"french": "peu", "english": "little"},
    {"french": "toujours", "english": "always"},
    {"french": "souvent", "english": "often"},
    {"french": "ainsi", "english": "thus"},
]



def quiz_user(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['french']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong, the correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Let's learn some French words!")
    input("Press Enter to test your knowledge...")
    quiz_user(words)

if __name__ == "__main__":
    main()