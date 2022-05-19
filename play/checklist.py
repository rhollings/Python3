# checklist script
# ask questions one by one, waiting for response
# if not checked, continue waiting 

# should list be a list or dict ?? -> dict is better


check_list = ['top', 'left', 'bottom', 'right']
check_dict = {'top': None, 'left': None, 'bottom': None, 'right': None}


def checklist_(clist):
    for item in clist:
        is_checked = input(item + '?')
        print(is_checked)
        if is_checked == 'c':
            clist[item] = 'checked'
            print('checked')
        else:
            clist[item] = 'needs attention'
    print(clist)

checklist_(check_dict)