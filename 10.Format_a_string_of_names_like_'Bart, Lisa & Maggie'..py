'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated
by commas except for the last two names, which should be
separated by an ampersand.

Example:

list([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
// returns 'Bart, Lisa & Maggie'

list([ {'name': 'Bart'}, {'name': 'Lisa'} ])
// returns 'Bart & Lisa'

list([ {'name': 'Bart'} ])
// returns 'Bart'

list([])
// returns ''

Note: all the hashes are pre-validated and will only contain
A-Z, a-z, '-' and '.'.
'''
def format_name(lst):
    return ', '.join([i['name'] for i in lst])[::-1].replace(',', '& ', 1)[::-1]
print(format_name([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(format_name([{'name': 'Bart'}, {'name': 'Lisa'}]))
print(format_name([{'name': 'Bart'}]))
print(format_name([]))
print(format_name([{'name': 'Bart'}, {'name': 'Stan'},{'name': 'Danny'},{'name': 'Lisa'}, {'name': 'Maggie'}]))





