
import html_with_python as hwpy

# to convert html tags in python to html document
import pytoh


# creating html tag
# thtml object in terms of python
html_1 =  hwpy.thtml();

# creating head tag
# thead object in terms of python
head_1 = hwpy.thead();

# creating body tag
# tbody object in terms of python
body_1 = hwpy.tbody();


# creating title tag
# ttitle in terms of python
title_1 =  hwpy.ttitle();
title_1.content = "Webpage 1"


# creating div tags
# tdiv objects in terms of python
div1_1 = hwpy.tdiv();
div2_1 = hwpy.tdiv();

# creating p tag
# tp object in terms of python
p1_1 =  hwpy.tp();
p1_1.content = "Hello here welcome to my webpage"
p1_1.id = "id1"
p1_1.classs = ["class1" , "class2"]


# creating p tag
# tp object in terms of python
p2_1 =  hwpy.tp();
p2_1.content = "Are you ready to know about some villages?"
p2_1.id = "id2"
p2_1.classs = ["class3", "class2"]





# structre the tags
html_1.tappend(head_1)
html_1.tappend(body_1)

head_1.tappend(title_1)

body_1.tappend(div1_1)
body_1.tappend(div2_1)

div1_1.tappend(p1_1)
div2_1.tappend(p2_1)





# to covert html tags in python to html document.
# html document is created with the specified name.
html_str = pytoh.pytoh(html_1 ,"index.html" , htmlstr = True)

#print(f"html_str : \n{html_str}")



