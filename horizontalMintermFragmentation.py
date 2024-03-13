import itertools

class HorizontalMinitermFragmentGenerator:
    def __init__(self, relations):
        self.relations = relations

    def generate_fragments(self):
        # Extract unique attribute values for each attribute in the relations
        attribute_values = {}
        for relation in self.relations:
            for key, value in relation.items():
                if key not in attribute_values:
                    attribute_values[key] = []
                attribute_values[key].append(value)

        # Generate minterm predicates by combining attribute values for all attributes
        minterm_predicates = list(itertools.product(*[[(attr, value) for value in attribute_values[attr]] for attr in attribute_values]))

        # Convert minterm predicates to list of dictionaries format
        minterm_predicates = [{key: value for key, value in predicate} for predicate in minterm_predicates]

        # Create fragments using minterm predicates
        fragments = []
        for predicate in minterm_predicates:
            fragment = [relation for relation in self.relations if all(relation[attr] == predicate[attr] for attr in predicate)]
            fragments.append(fragment)

        return fragments

# Example usage
relations = [
    {'name': 'abel', 'age': 27, 'city': 'addis ababa'},
    {'name': 'dawit', 'age': 40, 'city': 'dire dawa'},
    {'name': 'ayele', 'age': 60, 'city': 'welenchiti'}
]
fragment_generator = HorizontalMinitermFragmentGenerator(relations)
fragments = fragment_generator.generate_fragments()
for fragment in fragments:
    print(fragment)
