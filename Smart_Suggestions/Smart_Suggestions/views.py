from os import stat, truncate
import json
from types import coroutine
from typing import SupportsRound
from django.http.response import HttpResponseNotModified
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import Behind_Scenes as bs
from . import list_in_list as ls
from . import Creater as cg
from . import TREES as t
from . import encoder
from . import GRAPHS as graf
# Create your views here.

class Suggs:
    suggestions = {}
    search_mails = ''
    all_users = ''
    lines = []
    parrent = ''
    storage = []
    friends = []


def make_friendship_graph():
    graph_index = False
    connection_nework = []
    suggestion_list = []
    friends_already = []
    indices = []

    #Getting FOFs
    for i in range(len(Suggs.parrent.next)):
        if(Suggs.parrent.next[i].data == Suggs.suggestions['active_user']):
            graph_index = i
        temp = Suggs.parrent.next[i].extra_info[-1][0]
        temp = temp[temp.find('<')+1:temp.find('>')]
        if(len(temp)>=3):
            temp = temp.split(',')
            temp.pop()
            for j in range(len(temp)):
                if temp[j].find("_T") != -1:
                    temp[j]=temp[j].split('_')[0]
                else:
                    temp[j] = []
                
            connection_nework.append(temp)
        else:
            connection_nework.append([])


    for i in range(len(Suggs.parrent.next)):
        for j in range(len(Suggs.parrent.next)):
            if(Suggs.parrent.next[j].data in connection_nework[i]):
                Suggs.parrent.next[j].graph_insert(Suggs.parrent.next[i])
            
    #Existing Friends
    for i in range(len(Suggs.parrent.next[graph_index].next)):
        friends_already.append(Suggs.parrent.next[graph_index].next[i])
        
    for i in range(len(friends_already)):
        for j in range(len(friends_already[i].next)):
            if(friends_already[i].next[j].data.strip()!=Suggs.suggestions['active_user'].strip()) and friends_already[i].next[j].data.strip() not in Suggs.suggestions['rejection'] and friends_already[i].next[j].data.strip() not in Suggs.suggestions['conn_sent']:
                friends_already[i].next[j].extra_info.append(friends_already[i].next[j].data)
                temp = friends_already[i].next[j].extra_info.copy()
                suggestion_list.append([friends_already[i].extra_info.copy(), temp])
    
    # print(suggestion_list)
    for i in range(len(suggestion_list)):
        # print("start : ", suggestion_list[i][0].data, suggestion_list[i][1].data)
        suggestion_list[i][1][0] = suggestion_list[i][1][-1]
        suggestion_list[i][1].pop()
        suggestion_list[i][1].append([suggestion_list[i][0][1]])
        suggestion_list[i][1].pop(-2)
        suggestion_list[i] = suggestion_list[i][1]
        print("end : ", i)

    maxi = 0
    for i in range(0, len(suggestion_list)-1):
        counter = 0
        for j in range(i+1, len(suggestion_list)):
            if suggestion_list[i][0] == suggestion_list[j][0] and j not in indices:
                suggestion_list[i][-1].append(suggestion_list[j][-1][0])
                counter+=1
                indices.append(j)
        maxi = max(counter, maxi)

    for i in range(len(suggestion_list)):
        suggestion_list[i].append(len(suggestion_list[i][-1]))

    suggestion_list.sort(key=lambda x: x[-1], reverse=True)

    Suggs.suggestions['graph_suggs'] = [suggestion_list[i] for i in range(len(suggestion_list)) if i not in indices]

def file_read():
    with open("D:/SDP/data.txt", 'r') as f:
        lines = f.readlines()
    return lines

def write_into():
    # print(lines[0].split('|')[0].split(':')[1].encode())
    f = open("D:/SDP/data.txt", 'w')
    for line in Suggs.lines:
        f.write(line)

    f.close()


def startpage(request):
    return render(request, 'cards.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    # go_back = False
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']
        byear = request.POST['year']
        insti = request.POST['institute']
        city = request.POST['city'].strip()
        state = request.POST['state'].strip()
        specs = request.POST.get('specs')
        hobby = request.POST.get('hobby')

        # print(city, state)

        f = open("D:/SDP/data.txt", 'a')

        # print(hobby)
        f.write(str(email) + ":" + password + "|Name:" + str(fname + " " + lname) + "|specs:" + str(specs) + "|hobby:" + str(hobby) + "|region:"+ f"{str(city)} {str(state)}" + "|year:"+str(byear)+f"|institute:{str(insti)}"+"~connection_req:<>|req_sent:[]|rejected:{"+"}\n")
        f.close()
        return render(request, 'login.html')
    else:
        # lines = file_read()
        return render(request, 'login.html')

def logout(request):
    write_into()
    Suggs.suggestions = {}
    Suggs.all_users = ""
    Suggs.search_mails = ""
    return render(request, 'cards.html')

# def home(request):
    # email = request.POST['email']
    # # password = request.POST['pass']
    # f = open("D:/SDP/data.txt", 'r')

    # temp = f.readlines()

    # f.close()
    # if len(bs.Graph.Users)==0:
    #     for line in temp:
    #         # bs.Graph.Users.append(cg.info_seperator(line))
    #         cg.info_seperator(line)
    
    # # print(bs.Graph.Users[0].name, bs.Graph.Users[1].name)

    # can_be_conn = []

    # for user in bs.Graph.Users:
    #     if user.specializations.strip().lower() == bs.Graph.Users[-1].specializations.strip().lower():
    #         user.reason = "spec"
    #         can_be_conn.append(user)
    #     elif user.name.strip().lower() == bs.Graph.Users[-1].name.strip().lower():
    #         user.reason = "name"
    #         can_be_conn.append(user)
    #     elif user.hobbies.strip().lower() == bs.Graph.Users[-1].hobbies.strip().lower():
    #         user.reason = "hobby"
    #         can_be_conn.append(user)
        
    # # print(user)
    # s = sorted([i.reason for i in can_be_conn])
    
    # print(s)

    # return render(request, 'home.html', {"email":email, "users":can_be_conn})

def profile_me():
    loged_in_user = Suggs.search_mails
    temp = Suggs.lines

    conn_requests = loged_in_user.extra_info[-1][0]
    connections = loged_in_user.extra_info[-1][1]
    rejections = loged_in_user.extra_info[-1][2]

    print("reference : ", loged_in_user.extra_info)

    connections = connections.replace('[', '')
    connections = connections.replace(']', '')
    connections = connections.split(',')
    if len(connections) != 0:
        connections.pop(-1)

    rejections = rejections.replace('{', '')
    rejections = rejections.replace('}', '')
    rejections = rejections.split(',')
    if len(rejections) != 0:
        rejections.pop(-1)

    conn_requests = conn_requests.replace('<', '')
    conn_requests = conn_requests.replace('>', '')
    conn_requests = conn_requests.split(',')
    if len(conn_requests) != 0:
        conn_requests.pop(-1)

    # Recommend using Specializations
    user_data1 = loged_in_user.extra_info.copy()
    user_data1[0], user_data1[2] = user_data1[2], user_data1[0]
    tree2 = t.Tree(user_data1)

    # Recommend using Community
    user_data2 = loged_in_user.extra_info.copy()
    user_data2.insert(0, loged_in_user.extra_info[1].split()[1])
    tree3 = t.Tree(user_data2)

    # Recommend using Birth Year
    user_data3 = loged_in_user.extra_info.copy()
    user_data3[0], user_data3[5] = int(user_data3[5]), user_data3[0]
    tree4 = t.Tree(user_data3)

    # Recommend using Region
    user_data4 = loged_in_user.extra_info.copy()
    user_data4[0], user_data4[4] = user_data4[4], user_data4[0]
    tree5 = t.Tree(user_data4)

    # Recommend using Education
    user_data5 = loged_in_user.extra_info.copy()
    user_data5[0], user_data5[6] = user_data5[6], user_data5[0]
    tree6 = t.Tree(user_data5)
    print(tree6.data, tree6.extra_info)

    for line in temp:
        cg.specialized(line, tree2, connections, rejections, conn_requests)
        cg.sirnames(line, tree3, connections, rejections, conn_requests)
        cg.birth_year(line, tree4, connections, rejections, conn_requests)
        cg.region(line, tree5, connections, rejections, conn_requests)
        cg.education(line, tree6, connections, rejections, conn_requests)

    # print("tree5 : ", user_data4)
    # print(tree5.right.left.data)
    # tree5.bst_traversal_pre("root : ")
    tree2.bst_traversal_pre("root : ")
    tree6.bst_traversal_pre("root : ")

    index = []

    found1 = []
    t.bst_exact_search(tree2, tree2.data, found1)
    print("found1_before : ", found1)
    for i in range(len(found1)):
        if found1[i][1].strip() == loged_in_user.data.strip():
            index.append(i)
        else:
            found1[i][3], found1[i][4] = found1[i][4], found1[i][3]
            found1[i][2], found1[i][3] = found1[i][3], found1[i][2]
            found1[i][1], found1[i][2] = found1[i][2], found1[i][1]
            found1[i][5], found1[i][4] = found1[i][4], found1[i][5]
            found1[i][2], found1[i][6] = found1[i][6], found1[i][2]
            found1[i][6], found1[i][4] = found1[i][4], found1[i][6]
            found1[i].append("With Same Specializations")
        
    for i in index:
        found1.pop(i)
    
    index = []

    print("found1 : ", found1)

    found2 = []
    
    t.bst_exact_search(tree3, tree3.data, found2)
    for i in range(len(found2)):
        if found2[i][0] == loged_in_user.data:
            index.append(i)
        else:
            found2[i].pop(-1)
            found2[i][0], found2[i][1] = found2[i][1], found2[i][0]
            found2[i][5], found2[i][1] = found2[i][1], found2[i][5]
            found2[i][5], found2[i][4] = found2[i][4], found2[i][5]
            found2[i].append("From Same Community")
            if found2[i][4] in [info[4] for info in found1]:
                found2[i].append("With Same Specializations")

    for i in index:
        found2.pop(i)
    
    index = []

    print("found2 : ", found2)

    found4 = []

    t.bst_exact_search(tree5, tree5.data, found4)
    for i in range(len(found4)):
        if found4[i][4] == loged_in_user.data:
            index.append(i)
        else:
            found4[i][3], found4[i][4] = found4[i][4], found4[i][3]
            found4[i][2], found4[i][3] = found4[i][3], found4[i][2]
            found4[i][2], found4[i][1] = found4[i][1], found4[i][2]
            found4[i][5], found4[i][6] = found4[i][6], found4[i][5]
            found4[i].append("From Same Area/Region")
            if found4[i][4] in [info[4] for info in found2]:
                found4[i].append("From Same Community")
            if found4[i][4] in [info[4] for info in found1]:
                found4[i].append("With Same Specializations")
        
    for i in index:
        found4.pop(index)

    index = []

    print("found4 : ", found4)

    found5 = []

    t.bst_exact_search(tree6, tree6.data, found5)
    print("before found5 : ", found5)
    for i in range(len(found5)):
        if found5[i][4] == loged_in_user.data:
            index.append(i)
        else:
            # found5[i].pop(-1)
            found5[i][3], found5[i][4] = found5[i][4], found5[i][3]
            found5[i][2], found5[i][3] = found5[i][3], found5[i][2]
            found5[i][2], found5[i][1] = found5[i][1], found5[i][2]
            found5[i][5], found5[i][6] = found5[i][6], found5[i][5]
            found5[i][4], found5[i][6] = found5[i][6], found5[i][4]
            found5[i][5], found5[i][6] = found5[i][6], found5[i][5]

            found5[i].append("From Same Institute")
            if found5[i][4] in [info[4] for info in found2]:
                found5[i].append("From Same Community")
            if found5[i][4] in [info[4] for info in found1]:
                found5[i].append("With Same Specializations")
            if found5[i][4] in [info[4] for info in found4]:
                found5[i].append("From Same Area/Region")
        
    # for i in index:
    #     found5.pop(index)

    index = []

    print("found5 : ", found5)


    found3 = []
    t.bst_exact_search(tree4, tree4.data, found3)
    print("before_found3 : ", found3)
    for i in range(len(found3)):
        if found3[i][4] == loged_in_user.data:
            index.append(i)
        else:
            found3[i][3], found3[i][1] = found3[i][1], found3[i][3]
            found3[i][2], found3[i][3] = found3[i][3], found3[i][2]
            found3[i][1], found3[i][6] = found3[i][6], found3[i][1]
            found3[i][5], found3[i][6] = found3[i][6], found3[i][5]
            found3[i].append("Age Mates")
            if found3[i][4] in [info[4] for info in found2]:
                found3[i].append("From Same Community")
            if found3[i][4] in [info[4] for info in found1]:
                found3[i].append("With Same Specializations")
            if found3[i][4] in [info[4] for info in found4]:
                found3[i].append("From Same Area/Region")

    for i in index:
        found3.pop(i)
    
    index = []

    for i in range(len(found2)):
        if found2[i][4] not in [info[4] for info in found3] and found2[i][4] != loged_in_user.data:
            found3.append(found2[i])

    for i in range(len(found4)):
        if found4[i][4] not in [info[4] for info in found3] and found4[i][4] != loged_in_user.data:
            found3.append(found4[i])

    for i in range(len(found5)):
        if found5[i][4] not in [info[4] for info in found3] and found5[i][4] != loged_in_user.data:
            found3.append(found5[i])

    for i in range(len(found1)):
        if found1[i][4] not in [info[4] for info in found3] and found1[i][4] != loged_in_user.data:
            found3.append(found1[i])

    for i in range(len(found3)):
        found3[i].insert(5, ((len(found3[i][7:]))/5)*100)


    print("----", found3)

    found3.sort(key=lambda x: x[5], reverse=True)

    tree3.bst_traversal_pre("root : ")
    Suggs.suggestions = {'active_user' : loged_in_user.data,'sugs':found3,'rejection':rejections,"conn_sent":connections, "conn_reqs":conn_requests}

    make_friendship_graph()

    print(Suggs.suggestions['graph_suggs'])


def myprofile(request):
    root = t.Tree("m")
    temp = file_read()
    parrent = graf.Graph("parrent")
    if len(Suggs.lines) == 0: Suggs.lines = temp

    for line in temp:
        cg.info_seperator(line, root, parrent)

    Suggs.parrent = parrent

    # new_person = bs.Graph([fname + " " + lname, specs, hobby, 2001])
    # bs.Graph.new_user(new_person)
    
    Suggs.all_users = root
    root.bst_traversal_pre("root : ")
    
    if request.method == "POST":
        mail = request.POST['email'].strip()
        pas = request.POST['pass']

        search_res = t.bst_search(root, mail)
        Suggs.search_mails = search_res

        if search_res == False:
            return render(request, 'signup.html')

        else:
            if search_res.extra_info[0] == pas:
                profile_me()
                return render(request, 'home.html', {'suggestions':Suggs.suggestions})
            else:
                return render(request, 'login.html')

    elif request.method == "GET":
        search_res = t.bst_search(root, Suggs.suggestions['active_user'])
        profile_me()
        if(len(Suggs.friends)==0): engraph_me()
        return render(request, 'home.html', {'suggestions':Suggs.suggestions, 'all': json.dumps(Suggs.storage), 'friends': json.dumps(Suggs.friends)})


def conrej(request):
    if(len(Suggs.friends)==0): engraph_me()
    con_rej = request.POST.get("confirm")
    con_rej = con_rej.split("|")

    connections_emails = con_rej[0].split(',')
    connections_emails.pop(-1)
    rejection_emails = con_rej[1].split(',')
    Suggs.suggestions['rejection'] = rejection_emails[1:]

    lines = Suggs.lines
    
    for i in range(len(lines)):
        if lines[i].split(':')[0].strip() == connections_emails[0].strip():
            for person_con in connections_emails[1:]:
                lines[i] = lines[i].replace(lines[i][lines[i].find(']')], f'{person_con},]', 1)
                Suggs.search_mails.extra_info[-1][1] = lines[i][lines[i].find('['):lines[i].find(']')+1]


            for person_rej in rejection_emails[1:]:
                lines[i] = lines[i].replace(lines[i][-2], f'{person_rej},'+"}", 1)
                Suggs.search_mails.extra_info[-1][2] = lines[i][lines[i].find('{'):lines[i].find('}')+1]
            
        else:
            for person_con in connections_emails[1:]:
                if person_con == lines[i].split(':')[0].strip():
                    lines[i] = lines[i].replace('>', Suggs.suggestions['active_user']+',>')

    
    Suggs.lines = lines
    profile_me()

    return render(request, 'home.html', {'suggestions':Suggs.suggestions, 'all': json.dumps(Suggs.storage), 'friends': json.dumps(Suggs.friends)})


def rejs_extension():
    rejections = Suggs.suggestions['rejection'].copy()

    res = []

    for i in rejections:
        print(i)
        res.append(t.bst_search(Suggs.all_users, i))
    
    rejections = []
    rejections_temp = []

    for i in res:
        rejections_temp = [i.extra_info[1], i.extra_info[2].strip(), i.extra_info[3].strip(), i.data.strip(), i.extra_info[4], i.extra_info[5], i.extra_info[6]]
        rejections.append(rejections_temp)
    
    return rejections


def rejects(request):
    if(len(Suggs.friends)==0): engraph_me()
    if request.method == "GET":
        # print(Suggs.suggestions)
        rejections = rejs_extension()

        return render(request, 'rejects.html', {'rejections':rejections})

    elif request.method == "POST":
        mails = request.POST.get('confirm')
        mails = mails.split(',')
        # print(mails)
        
        lines = Suggs.lines

        for i in range(len(lines)):
            if lines[i].split(':')[0].strip() == Suggs.suggestions['active_user'].strip():
                start = lines[i].find('{')
                end = lines[i].find('}')
                rejs = lines[i][start+1:end].split(',')
                commons = ls.same_values(mails, rejs)
                print(rejs, commons)
                for j in range(len(commons)):
                    print(lines[i][lines[i].find(commons[j])])
                    lines[i] = lines[i].replace(lines[i][lines[i].find(commons[j]):lines[i].find(',', lines[i].find(commons[j]))+1], '')
                    Suggs.search_mails.extra_info[-1][-1] = lines[i][start:end+2]
                break

        Suggs.lines = lines
        profile_me()

        rejections = rejs_extension()

        return render(request, 'rejects.html', {'rejections':rejections})

def con_req_extension():
    remaining = []
    for i in Suggs.suggestions['conn_reqs']:
        if len(i.split('_'))==2:
            continue
        else:
            remaining.append(i)

    res = []
    for i in remaining:
        res.append(t.bst_search(Suggs.all_users, i))

    remaining = []
    remaining_temp = []

    for i in res:
        remaining_temp = [i.extra_info[1], i.extra_info[2].strip(), i.extra_info[3].strip(), i.data.strip(), i.extra_info[4], i.extra_info[5], i.extra_info[6]]
        remaining.append(remaining_temp)

    return remaining

def connection_reqs(request):
    if(len(Suggs.friends)==0): engraph_me()
    if request.method == "GET":
        remaining = con_req_extension()
        print(remaining)
        return render(request, 'connection_requests.html', {'conn_reqs':remaining, 'all': json.dumps(Suggs.storage), 'friends': json.dumps(Suggs.friends)})

    elif request.method == "POST":
        commons = []
        mails = request.POST.get('confirm')
        mails = mails.split(',')
        
        lines = Suggs.lines

        for i in range(len(lines)):
            if lines[i].split(':')[0].strip() == Suggs.suggestions['active_user'].strip():
                start = lines[i].find('<')
                end = lines[i].find('>')
                accepted = lines[i][start+1:end].split(',')
                commons = ls.same_values(mails, accepted)

                for j in range(len(commons)):
                    lines[i] = lines[i].replace(lines[i][lines[i].find(commons[j]):lines[i].find(',', lines[i].find(commons[j]))+1], commons[j]+'_T,')
                    Suggs.search_mails.extra_info[-1][0] = lines[i][start:end+1]
                
        for j in range(len(lines)):
            if lines[j].split(':')[0].strip() in commons:
                lines[j] = lines[j].replace(lines[j][lines[j].find(Suggs.suggestions['active_user']):lines[j].find(',', lines[j].find(Suggs.suggestions['active_user']))+1], '')
                lines[j] = lines[j].replace('>', Suggs.suggestions['active_user']+'_T,>')

        Suggs.lines = lines

        print(Suggs.lines)

        profile_me()
        remaining = con_req_extension()

        return render(request, 'connection_requests.html', {'conn_reqs':remaining, 'all': json.dumps(Suggs.storage), 'friends': json.dumps(Suggs.friends)})

def your_connection(request):
    connected = []
    for i in Suggs.suggestions['conn_reqs']:
        if len(i.split('_'))==2:
            connected.append(i)
        else:
            continue
    
    res = []
    for j in connected:
        res.append(t.bst_search(Suggs.all_users, j.split('_')[0]))

    connected = []
    connected_temp = []

    for i in res:
        connected_temp = [i.extra_info[1], i.extra_info[2].strip(), i.extra_info[3].strip(), i.data.strip(), i.extra_info[4], i.extra_info[5], i.extra_info[6]]
        connected.append(connected_temp)
    
    if(len(Suggs.friends)==0): engraph_me()
    return render(request, 'your_connections.html', {"connections":connected, 'all': json.dumps(Suggs.storage), 'friends': json.dumps(Suggs.friends)})


def suggestions_from_graph(request):
    if(len(Suggs.friends)==0): engraph_me()
    return render(request, "graph_home.html", {"fof":Suggs.suggestions['graph_suggs'], 'active_user':Suggs.suggestions['active_user'], 'all': json.dumps(Suggs.storage), 'friends': json.dumps(Suggs.friends)})

def engraph_me():
    Suggs.all_users.bst_traversal_pre_storage_en(Suggs.storage)
    for i in Suggs.parrent.next:
        i.graph_traversal_dfs(Suggs.friends)
    return ('graphs.html', {'all': json.dumps(Suggs.storage), 'friends': json.dumps(Suggs.friends)})