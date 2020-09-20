def check_input(input,pos):
    try:
        input = int(input)
        if pos == 1:
            if input > 5 or input < 2:
                print(" #table must be between 2 and 5 !!!\n")
                return 0
        elif pos == 2:
            if input > 30 or input < 10:
                print(" Size of table must be between 10 and 30 !!!\n ")
                return 0
    except ValueError:
        print(" Input must be an integer !!!\n")
        return 0
    return 1
def init_table():
    global HashTable
    HashTable = [["-"for x in range(size_of_table)] for y in range(number_of_table)] 
def hash(functionID,key):
    global collision_number
    sum=0
    val = 1
    for i in key:
        sum=sum+ord(i)*val  
        val=val+1
    return (sum*functionID)%size_of_table
def calculate_loadfactor():
    global load_factor
    number_of_index=0
    for i in range(number_of_table):
        
        for j in range(size_of_table):
            if HashTable[i][j]!="-":
                number_of_index=number_of_index+1
        print("Table%d -> #collision = %d  loadfactor = %f"%(i+1,collision_number[i],number_of_index/size_of_table))
        load_factor.append([i,number_of_index/size_of_table])
        number_of_index=0

def insertion( key,tableID,cnt,cycle_number):
    global collision_number
    global load_factor
    pos = []
    if cnt== cycle_number:
        print("\n!!!!!!!\n%s unpositioned\n"%key)
        print("\nCYCLE  PRESENT.\n")
        return
    i=0
    while(i<number_of_table):

        pos.append(hash(i+1, key))
        if (HashTable[i][pos[i]] == key):
            print("%s is already exist !!!\n"%key)
            return
        i=i+1
    if (HashTable[tableID][pos[tableID]]!="-"):
        dis = HashTable[tableID][pos[tableID]]
        HashTable[tableID][pos[tableID]] = key 
        insertion(dis, (tableID+1)%number_of_table, cnt+1, cycle_number)
        collision_number[tableID]=collision_number[tableID]+1
    else:
        HashTable[tableID][pos[tableID]] = key
    
def delete(key):
    for i in range(number_of_table):
        for j in range(size_of_table):
            if HashTable[i][j]==key:
                HashTable[i][j]="-"
                print("\n%s deleted !!!\n"%key)
                return 1
    print("\n\"%s\" does not exist !!!\n"%key)
    return 0

def search(key):
    for i in range(number_of_table):
       if HashTable[i][hash(i+1,key)]==key:
           print("\n\nKey \"%s\" in \"Cell%d\" of \"Table%d\" \n"%(key,1+hash(i+1,key),i+1))
           return
    print("\n\"%s\" not found !!!\n"%key)

def print_HashTable():
    string =""
    index ="________"
    for j in range(size_of_table):
        index =index+"___"
    print("         %s\n"%index)
    for i in range(number_of_table):
        for j in range(size_of_table):
            string = string+"  "+str(HashTable[i][j])
        print("Table%d  %s\n"%(i+1,string))
        string=""
    calculate_loadfactor()
    print("\n\n         %s"%index)
            

if __name__ == "__main__":
    global number_of_table
    global size_of_table 
    global collision_number
    global load_factor
    load_factor = []
    print("------ CUCKOO HASHING ------\n")
    while(1):
        number_of_table = input(" Enter number of table: ") 
        if check_input(number_of_table,1) == 1:
            number_of_table = int(number_of_table)
            break
    while(1):
        size_of_table = input(" Enter size of table (cell): ") 
        if check_input(size_of_table,2) == 1:
            size_of_table = int(size_of_table)
            break
    init_table()
    collision_number = [0]*number_of_table
    while(1):
        choice =input("\n__________MENU_________\n1 : Insert an element\n2 : Delete an element\n3 : Search an element\n4 : Exit\n_______________________\n=> ")
        try:
            choice=int(choice)
            if choice == 1:
                key = input("Enter a word for insertion: ")
                insertion(key,0,0,size_of_table)
                print_HashTable()
            elif choice == 2:
                key = input("Enter a word for deleting: ")
                if delete(key) == 1:
                    print_HashTable()
            elif choice == 3:
                key = input("Enter a word for searching: ")
                search(key)
            elif choice == 4:
                print("Program is end. Goodbye :)\n")
                break
            else:
                print("INVALID CHOICE \n")
        except: 
            print("INVALID CHOICE\n")
     
        
