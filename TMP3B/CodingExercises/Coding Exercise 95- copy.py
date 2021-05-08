'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy(input_file, output_file):
    with open(input_file, 'r') as input_file:
        copy = input_file.read()
        with open(output_file, 'w') as outputfile:
            outputfile.write(copy)


# alt

# def copy(file_name, new_file_name):
#     with open(file_name) as file:
#         text = file.read()
    
#     with open(new_file_name, "w") as new_file:
#         new_file.write(text)