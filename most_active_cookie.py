
import sys


def cleaning_logs(file_name):
    logs=[]
    
    
    with open (file_name,'r') as full_logs:
        result = []
        result1=[]
        for line in full_logs:            
            rows=line.split('\n')
            result.append((rows[:1]))

        for x in result:
            name=x[0].split("T")
            logs.append(name[0])


    del logs [0:3]
    return logs


        
def most_active(list,date):
      
        found=[]
        not_active=[]
        active=[]

        for logs in list:
            if date in logs:                   #find logs that match the date 
                found.append(logs)
        required=[i.split(",")[0] for i in found]    

  
        for j in required:                     # check wheter the log are already in the list
            if j not in not_active:
                not_active.append(j)
            else:
                active.append(j)
        if active:
            for x in range(len(active)):
             print(active[x])
            return active
             
        else:
            for x in range(len(required)):
             print(required[x])
            return required     
                
            
        


if __name__ == '__main__':
    
    
    file_name= sys.argv[1]
    
    date=sys.argv[3]
    
    logs=cleaning_logs(file_name)

    active_logs=most_active(logs,date)

    sys.exit()
        
        
    



