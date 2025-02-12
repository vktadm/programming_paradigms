notes = 'доремифасольляси'

# lst_in = input().split()
lst_in = 'до фа соль до ре фа ля си'.split()

print(*sorted(lst_in, key=notes.find))
