facts = {
    'Jason': 'Can fly an airplane.',
    'Jeff': 'Is afraid of clowns.',
    'David': 'Plays the piano.'
    }

def display_facts(facts):
    """Displays facts"""   
    print()
    for fact in facts:
        print('{}: {}'.format(fact, facts[fact])) 

display_facts(facts)


facts['Jeff'] = 'Is afraid of heights.'
facts['Jill'] = 'Can hula dance.'

display_facts(facts)

#TUPLE
airports = [
("O’Hare International Airport", 'ORD'),
('Los Angeles International Airport', 'LAX'),
('Dallas/Fort Worth International Airport', 'DFW'),
('Denver International Airport', 'DEN')
]

for (airport, code) in airports:
    print('The code for {} is {}.'.format(airport, code))


