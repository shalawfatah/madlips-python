from goodadj import list_of_good_adj
from badadj import list_of_bad_adj

name = input('Write your name: ').capitalize()
adj = input('Adjective: ').lower()
verb1 = input('Verb: ').lower()
verb2 = input('Verb: ').lower()
famous = input('Famous Person: ').capitalize()

if adj.capitalize() in list_of_good_adj:
    print(f'Howdy {name}, for someone like you, the sky is not the limit. You are {adj}, you might like to {verb1} and {verb2}, and and admire {famous}. Go on, enjoy the day.')
elif adj.lower() in list_of_bad_adj:
    print(f'Hello {name}, You should not worry that much, all the negativity will be over soon. You are not {adj}, you might like to {verb1} and {verb2}, and and admire {famous}. Go on, enjoy the day.')
elif adj.capitalize() not in list_of_good_adj and adj.capitalize() not in list_of_bad_adj:
    print(f'Hi {name}, while you claim to be {adj}, and might like to do {verb1} and {verb2}, we cannot understand you. I am a computer and a I cannot understand!')

    






