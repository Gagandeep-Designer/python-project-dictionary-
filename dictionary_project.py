#Create a dictionary
employee_dict={
   'employee_1':{
      'name':'joy',
      'age':'28',
      'profession':'software devloper',
      'salary':20000
   },
   'employee_2':{
      'name':'Tom',
      'age':'28',
      'profession':'web devloper',
      'salary':21000
   },
   'employee_3':{
      'name':'jerry',
      'age':'26',
      'profession':'software devloper',
      'salary':25000
   }
}
# print(employee_dict)
# print(employee_dict['employee_2']['age'])
employee_dict['employee_2']['name']='Deep'
for k,v in employee_dict.items():
   print(k,v)
while True:
  list=[]
 
  user_choice=int(input('''
                        1.Add your Name,Email,Phone-no
                        2.Delete Incoreect Data.
                        3.Show Last Name.
                        4.Display All Details.
                        5.Exit.'''))
  if user_choice==1:
    name_input=input("Enter your Name:-")
    email_input=input("Enter your Email-id:-")  
    phone_input=input("Enter your phone-no:-")  
    address_input=input("Enter your City Address:-")
    list.append("Name:-"+name_input + "  "+"Email-id is:-"+ email_input +"  "+"Phone-no is:-"+ phone_input +"  "+"City Address is:-"+ address_input)
    print(list)
  elif user_choice==2:
      if len(list)==0:
        print("Empty List")
      else:
        delete_item=list.pop()
        print(delete_item)
        print(list)
  elif user_choice==3:
      if len(list)==0:
        print("Empty List")
      else:
        print("Last Name:-",list[-1])
  elif user_choice==4:
      print("Display Data",list)
  elif user_choice==5:
    break
  else:
      print("Invalid operation.....")