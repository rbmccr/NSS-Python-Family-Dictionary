# Define a dictionary that contains information about several members of your family. Use the following example as a template.

my_family = {
    'sister': {
        'name': 'Melissa',
        'age': 41
    },
    'mother': {
        'name': 'Brenda',
        'age': 67
    },
    'father': {
        'name': 'Robert',
        'age': 68
    }
}

# Using a dictionary comprehension, produce output that looks like the following example.

results = ['my ' + k + " " + v['name'] + ' is ' + str(v['age']) + ' years old' for (k,v) in my_family.items()]
print((". ").join(results).title())

# PRINT RESULT: My Sister Melissa Is 41 Years Old. My Mother Brenda Is 67 Years Old. My Father Robert Is 68 Years Old