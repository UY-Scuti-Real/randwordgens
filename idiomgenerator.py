import wordlists as wl
import random

idiom_formats = ['{noun1} is wasted on the {adjective1}',
                 'Too many {noun1}s spoil the {noun2}',
                 'a {noun1} is as good as a {noun2}',
                 '{verb1} the {noun1}',
                 '{verb1} a {noun1}',
                 'the {noun1} is the {noun2}',
                 '{noun1} {verb1}s',
                 '{noun1}s maketh the {noun2}',
                 '{noun1}s should be {verb1}ed and not {verb2}ed',
                 'Better {adjective1} than {adjective2}',
                 'a little {noun1} is a {adjective1} thing',
                 'a {noun1} is worth a thousand {noun2}s',
                 'all that {verb1}s is not {noun1}',
                 'a watched {noun1} never {verb1}s',
                 'Absolute {noun1} {verb1}s absolutely',
                 "you can't get {noun1} from {noun2}",
                 "you can't make a {noun1} without {verb1}ing a few {noun2}s",
                 'a {noun1} in the {noun2} is worth two in the {noun3}',
                 'a {noun1} for your {noun2}s',
                 '{noun1}s speaks louder than {noun2}s',
                 '{verb1}ing up the wrong {noun1}',
                 'a {noun1}ing in {noun2}',
                 'a {noun1} a {noun2}',
                 '{verb1} around the {noun1}',
                 'another {noun1} another {noun2}',
                 'No {noun1}, no {noun2}',
                 "{noun1} {verb1}s when you're {verb2}ing {noun2}",
                 "We'll {verb1} that {noun1} when we come to it",
                 "A {noun1} {verb1}ed is a {noun1} {verb2}ed",
                 "by the {noun1} of your {noun2}",
                 "Comparing {noun1}s to {noun2}s",
                 "Don't {verb1} over {verb2}ed {noun1}",
                 "{noun1} breeds {noun2}",
                 "{noun1} makes {noun2}",
                 "They're not {verb1}ing with a full {noun1}",
                 "Let {verb1}ing {noun1}s {verb2}",
                 "like {verb1}ing a {noun1}",
                 "The {noun1} calling the {noun2} {adjective1}",
                 "Those who {verb1} in {adjective1} {noun1}s shouldn't {verb2} {noun2}s",
                 "Add {noun1} to {noun2}",
                 "At the {verb1} of the {noun1}",
                 "Back to the {verb1}ing {noun1}",
                 "The {noun1} is in your {noun2}",
                 "I'll be {adjective1} to {verb1} the {noun1} of {noun2}",
                 "Best thing since {verb1}ed {noun1}",
                 "Don't {verb1} more than you can {verb2}",
                 ]


def gen_idiom_from_form(form):
    kwargs = {"noun1":wl.rand_noun().lower(),
    "noun2":wl.rand_noun().lower(),
    "noun3":wl.rand_noun().lower(),
    "adjective1":wl.rand_adj().lower(),
    "adjective2":wl.rand_adj().lower(),
    "verb1": wl.rand_verb().lower(),
    "verb2": wl.rand_verb().lower()}
    idiom = form.format(**kwargs)
    return idiom.capitalize()

def gen_googlewhack():
    kwargs = {"noun1":wl.rand_noun().lower()}

def gen_rand_idiom(idiom_formats = idiom_formats):
    random_format = idiom_formats[random.randint(0, len(idiom_formats)-1)]
    return gen_idiom_from_form(random_format)

def gen_all_idioms(idiom_formats = idiom_formats):
    for form in idiom_formats:
        print(gen_idiom_from_form(form))

#print(gen_rand_idiom())
gen_all_idioms()
