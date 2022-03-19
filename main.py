#Header
def header(text):
    print('--------------------------')
    print('*',text,'*')
    print('--------------------------')

#Import and convert CSV to List of list
from csv import reader
open_file = open('HN_posts_year_to_Sep_26_2016.csv')
read_file = reader(open_file)
hn_posts = list(read_file)

hn_posts_header = hn_posts[0]
hn_posts = hn_posts[1:]

#Explore dataset
def explore_dataset(dataset,start=0,end=5):
    for row in dataset[start:end]:
        print(row)

header('Explore dataset')
print('Total posts:',len(hn_posts))
print(hn_posts_header)
explore_dataset(hn_posts)

#Remove posts has 0 comment
header('Remove posts has 0 comment')
hn_posts_has_comments = []

for row in hn_posts:
    num_comments = int(row[4])
    if num_comments != 0:
        hn_posts_has_comments.append(row)

print('Total posts has comments:',len(hn_posts_has_comments))

#Separate posts
header('Separate posts')
ask_posts = []
show_posts = []
other_posts = []

for row in hn_posts_has_comments:
    title = row[1]
    if title.lower().startswith('ask hn') == True:
        ask_posts.append(row)
    elif title.lower().startswith('show hn') == True:
        show_posts.append(row)
    else:
        other_posts.append(row)

print('Ask HN:',len(ask_posts))
explore_dataset(ask_posts)
print('Show HN:',len(show_posts))
explore_dataset(show_posts)
print('Other HN:',len(other_posts))
explore_dataset(other_posts)

#Determine if ask posts or show posts receive more comments on average
header('Determine if ask posts or show posts receive more comments on average')
total_ask_posts_comments = 0
total_show_posts_comments = 0

for row in ask_posts:
    num_comments = int(row[4])
    total_ask_posts_comments += num_comments

for row in show_posts:
    num_comments = int(row[4])
    total_show_posts_comments += num_comments

avg_ask_posts_comments = total_ask_posts_comments / len(ask_posts)
avg_show_posts_comments = total_show_posts_comments / len(show_posts)

print('Average Ask posts comments:',avg_ask_posts_comments)
print('Average Show posts comments',avg_show_posts_comments)