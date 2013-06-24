from sys import argv
from re import sub

script, filename = argv

f = open(filename)
# f_text = f.read()
# f_lowertext = f_text.lower()
f_text = f.read() #list of line strings ending in \n

f.close()

f_words = sub("[/!?,-:\"_';]", " ", f_text).lower().split()

f_dict = {}

for word in f_words:
	
		if f_dict.get(word) == None: #use get
			f_dict[word] = 1
		else: 
			f_dict[word]+=1 
					
# sorts alphabetically
sort_f_dict = sorted(f_dict)

#somehow 1 "the" ended up at the end
for word in sort_f_dict:
	print word, ":", f_dict[word]

#sorts by highest frequency

sort_freq_dict = sorted(f_dict, key=f_dict.get)
for word in sort_freq_dict[::-1]:
	print word, f_dict[word]

# for number in f_dict.itervalues():
# 	print number

















# new_f = []
# for lines in f_text:
# 	f_text.split(" ")

# print f_text
# #print f_words
# # for char in f_text:
# # 	print char
# # 	if char.isalpha() == False:
# # 		print "False char:", char
# # 		f_strip = f_text.strip(char)
# # 	# count += 1

# # print f_text

# #f_words is a list of strings
# # f_words = f_text.split(" ")

# # print f_words

# # f_strip = f_words.strip('') #strip only takes out leading or final characters


# # #initialized empty dictionary
# # f_dict = {}


# # for word in f_words:
# # 	if f_dict.setdefault(word, None) == None:
# # 		f_dict[word] = 1
# # 	else:
# # 		f_dict[word] += 1

# # print f_dict