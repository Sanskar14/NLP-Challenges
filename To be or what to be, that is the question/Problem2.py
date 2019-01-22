# Get Inputs
response = int(input())
Texts = str(input())
ToDoList = Texts
ToDoList = ToDoList.split(" ")

# Replace Blank with To Do Words as two before and after words
for i in range(len(ToDoList)):
    if ToDoList[i] == '----':
        if ToDoList[i-1] == 'i':
            print('am')
            continue
        elif ToDoList[i-1].endswith('s') and ToDoList[i+1].endswith('ed'):
            print('were')
            continue
        elif ToDoList[i-1] in ['is','are','was','were']:
            print('being')
            continue
        elif not ToDoList[i-1].endswith('s') and ToDoList[i+1].endswith('ed'):
            print('was')
            continue    
        elif ToDoList[i-1].endswith('s'):
            print('were')
            continue
        elif ToDoList[i-1] in ['had','has','have']:
            print('been')
            continue
        elif ToDoList[i-1] in ["couldn't",'would',"will","wouldn't","shall","won't", "can't", "can", "not",'might',"could",'may',]:
            print("be")
            continue
        elif (ToDoList[i-1].endswith('s') or not ToDoList[i-1].endswith('s')) and ToDoList[i+1].endswith('ing'):
            a = ToDoList[i-20:i]
            if any(True for u in a if u.endswith('ed')):
                if ToDoList[i-1].endswith('s') and ToDoList[i+1].endswith('ing'):
                    print('were')
                    continue
                elif not ToDoList[i-1].endswith('s') and ToDoList[i+1].endswith('ing'):
                    print('was')
                    continue
                continue
            else:
                if ToDoList[i-1].endswith('s') and ToDoList[i+1].endswith('ing'):
                    print('are')
                    continue
                elif not ToDoList[i-1].endswith('s') and ToDoList[i+1].endswith('ing'):
                    print('is')
                    continue
        elif (not ToDoList[i-1].endswith('s') and not ToDoList[i-1].endswith('s') and not ToDoList[i+1].endswith('ing') and not ToDoList[i+1].endswith('ed')):
            a = ToDoList[i - 20:i]
            if any(True for u in a if u.endswith('ed')):
                print('was')
                continue
            else:
                print('is')
                continue

