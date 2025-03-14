Tasks_list=[] 
while True :
 try:
   task = input("enter a task")
   if len(task) > 0 :
     print("task has been saved")
     tasks_list.append(task)
   else :
     print("Enter a task")
   print("type 'see task' to view your task")
   dec1=input().lower()
   if dec1 =="see task" :
      print(tasks_list)
   print("Type end to end this program")
   dec2=input().lower()
   if dec2 =="end" :
     print("Goodbye!")
     break
 except Exception as e : print("An error occurred", e)
