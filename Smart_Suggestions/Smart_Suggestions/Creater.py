from . import Behind_Scenes as bs
from . import TREES as t
from . import GRAPHS as graf

def find_con_req(con_req):
    for i in range(len(con_req)):
        if len(con_req[i].split('_')) == 2:
            con_req[i] = con_req[i].split('_')[0]
    
    return con_req

def info_seperator(all_info, root, parrent):
    info_con_sep = all_info.split('~')
    sep = info_con_sep[0].split('|')
    sep2 = [sep[i].split(':')[1] for i in range(len(sep))]
    sep2.insert(0, sep[0].split(":")[0])
    sep2[6] = int(sep2[6])
    # print(sep2)
    
    if type(info_con_sep) == list and info_con_sep[-1] != info_con_sep[0]:
        # print("info_con_sep")
        con = info_con_sep[1].split('|')
        con = [con[i].split(':')[1] for i in range(len(con))]
    
    else:
        # print("------------")
        con = []
    
    sep2.append(con)

    # person = bs.Graph(sep2)
    node = t.Tree(sep2)
    person = graf.Graph(sep2)
    # print(graf)
    person.graph_insert(parrent)
    # print(sep2[1:])
    root = node.bst_insert(root)

    # bs.Graph.new_user(person)


def specialized(all_info, tree2, con, rej, con_req):
    info_con_sep = all_info.split('~')
    sep = info_con_sep[0].split('|')

    con_reqests = con_req.copy()
    con_reqests = find_con_req(con_reqests)
    
    if sep[0].split(":")[0] not in con and sep[0].split(":")[0] not in rej and sep[0].split(":")[0] not in con_reqests:
        sep2 = [sep[i].split(':')[1] for i in range(1, len(sep))]
        sep2.insert(0, sep[0].split(":")[0])
        sep2[0], sep2[2] = sep2[2], sep2[0]
        sep2[5] = int(sep2[5])

        # print(sep2)

        node = t.Tree(sep2)
        tree2 = node.bst_insert(tree2)

def sirnames(all_info, tree3, con, rej, con_req):
    info_con_sep = all_info.split('~')
    sep = info_con_sep[0].split('|')

    con_reqests = con_req.copy()
    con_reqests = find_con_req(con_reqests)

    if sep[0].split(":")[0] not in con and sep[0].split(":")[0] not in rej and sep[0].split(":")[0] not in con_reqests:
        sep2 = [sep[i].split(':')[1] for i in range(1, len(sep))]
        sep2.insert(0, sep[0].split(":")[0])
        sep2.insert(0, sep2[1].split()[1])
        sep2[6] = int(sep2[6])

        node = t.Tree(sep2)
        tree3 = node.bst_insert(tree3)

def birth_year(all_info, tree4, con, rej, con_req):
    info_con_sep = all_info.split('~')
    sep = info_con_sep[0].split('|')

    con_reqests = con_req.copy()
    con_reqests = find_con_req(con_reqests)

    if sep[0].split(":")[0] not in con and sep[0].split(":")[0] not in rej and sep[0].split(":")[0] not in con_reqests:
        sep2 = [sep[i].split(':')[1] for i in range(1, len(sep))]
        sep2.insert(0, sep[0].split(":")[0])
        sep2[5] = int(sep2[5])
        sep2[0], sep2[5] = sep2[5], sep2[0]

        node = t.Tree(sep2)
        tree4 = node.bst_insert(tree4)

def region(all_info, tree5, con, rej, con_req):
    info_con_sep = all_info.split('~')
    sep = info_con_sep[0].split('|')

    con_reqests = con_req.copy()
    con_reqests = find_con_req(con_reqests)

    if sep[0].split(":")[0] not in con and sep[0].split(":")[0] not in rej and sep[0].split(":")[0] not in con_reqests:
        sep2 = [sep[i].split(':')[1] for i in range(1, len(sep))]
        sep2.insert(0, sep[0].split(":")[0])
        sep2[0], sep2[4] = sep2[4], sep2[0]
        sep2[5] = int(sep2[5])

        node = t.Tree(sep2)
        tree5 = node.bst_insert(tree5)


def education(all_info, tree5, con, rej, con_req):
    info_con_sep = all_info.split('~')
    sep = info_con_sep[0].split('|')

    con_reqests = con_req.copy()
    con_reqests = find_con_req(con_reqests)

    if sep[0].split(":")[0] not in con and sep[0].split(":")[0] not in rej and sep[0].split(":")[0] not in con_reqests:
        sep2 = [sep[i].split(':')[1] for i in range(1, len(sep))]
        sep2.insert(0, sep[0].split(":")[0])
        sep2[0], sep2[6] = sep2[6], sep2[0]
        sep2[5] = int(sep2[5])

        node = t.Tree(sep2)
        tree5 = node.bst_insert(tree5)





# region("ani14shaha@gmail.com:hBE2_$%%NR#HzxD|Name:Anish Shaha|specs:C++|hobby:Listening to podcasts|region:Ambad Maharashtra|year:2001~connection_req:<>|req_sent:[]|rejected:{}")