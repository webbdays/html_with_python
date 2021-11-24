
import subprocess


tag_list = [];

def depth_traversal(tag):
    if (tag.inner==[]):
        tag_list.append("<" + tag.__class__.__name__[1:] + ">");
        tag_list.append(tag);
        tag_list.append("</" + tag.__class__.__name__[1:] + ">")
    else:
        tag_list.append("<" + tag.__class__.__name__[1:] + ">");
        tag_list.append(tag);
        for tagg in tag.inner:
            depth_traversal(tagg);
        tag_list.append("</"+tag.__class__.__name__[1:] + ">");



def pytoh(html ,file_name=None, htmlstr = None):

    if (file_name or htmlstr):
        print("Getting the tag list ..... ");
        depth_traversal(html);
        #print(f"tag list : {tag_list}");

        if file_name and open(f"{file_name}", "a"):
            print(f"Checking if {file_name} already exists ?")
            print(f"found that {file_name} already exists.")
            yesno = input("need to remove this file ? [y/n] : ")
            while(yesno.lower()!="y" and  yesno.lower() != "n"):
                print("Enter the proper way")
                yesno = input("need to remove this file ? [y/n] : ")
            if yesno.lower() =="y":
                subprocess.run(f"rm {file_name}".split(" "));
            else:
                print("Not creating the html document.\nEnd of the process ... ||| "); return False;

        html_str = "";
        html_str += ("<!DOCTYPE html>\n")
        for i in range(0,len(tag_list)):
            if str(type(tag_list[i])) =="<class 'str'>" :
                if tag_list[i] == "<html>":
                    html_str += ("<html>\n");
                elif tag_list[i] == "<head>":
                    html_str += ("<head>\n");
                elif tag_list[i] == "<title>":
                    html_str += ("<title>");
                    html_str += (f"{tag_list[i+1].content}");
                elif tag_list[i] == "<body>":
                    html_str += ("<body ")
                    classs = " ".join(tag_list[i+1].classs)
                    style = " ".join(tag_list[i+1].style)
                    html_str += ( f' class="{classs}" style="{style}" >\n');
                elif tag_list[i] =="<div>":
                    id = tag_list[i+1].id
                    classs = " ".join(tag_list[i+1].classs)
                    style = " ".join(tag_list[i+1].style)
                    html_str += ("<div ")
                    html_str += (f' id="{id}"  class="{classs}" style="{style}" >\n');
                elif tag_list[i] == "<p>":
                    id = tag_list[i+1].id
                    classs = " ".join(tag_list[i+1].classs)
                    style = " ".join(tag_list[i+1].style)
                    html_str += ("<p ")
                    html_str += (f' id="{id}"  class="{classs}" style="{style}" >\n');
                    html_str += (f"{tag_list[i+1].content}\n")
                elif tag_list[i][:2] == "</":
                    html_str += (f"{ tag_list[i] }\n")
    else:
        print("Give proper parameters.")
        return False
    if (file_name):
        with open(f"{file_name}" , "w") as f:
            print(f"Creating empty {file_name} after checking file not exist before.")
            f.write(html_str)
            print(f"html_str is written to html document : {file_name}")
    if (htmlstr == True):
        print("html_str is returned.")
        return html_str;
    else:
        return False;

