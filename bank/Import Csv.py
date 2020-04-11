from .models import Bank, Branch

def import_bank(file_name):
    f = open(file_name, 'r', encoding='utf8')
    for line in f:
        try:
            line = line.split(';')
            Bank.objects.get_or_create(
                name   = line[0].rstrip()
            )
        except:
            pass
    f.close()

def import_branch(file_name):
    f = open(file_name, 'r', encoding='utf8')
    for line in f:
        try:
            line = line.split(';')
            Branch.objects.create(
                ifsc        = line[0],
                name        = line[1],
                address     = line[2],
                city        = line[3],
                state       = line[4],
            bank=Bank.objects.filter(name=line[-1].rstrip()).first()
            
            )
        except Exception as e:
                print('some error', i, e)
                i+=1
    f.close()
