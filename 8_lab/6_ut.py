from lab_6 import list

def test_list():
    llist = list.LinkedList()
    llist.append(3)
    llist.append(1)
    llist.append(2)

    print("Before sorting:")
    assert llist.__str__()=="3 1 2 "

    llist.sort_list()
    assert llist.__str__()=="1 2 3 "

