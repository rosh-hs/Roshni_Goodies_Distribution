import sys
global input_items,final_output

def form_dictionary_help(lst):
	res_dct = {lst[i] : lst[i+1] for i in range(0,len(lst),2)}
	#print(res_dct)
	return res_dct
    
def Goodie_function(goodies_price, number_of_goodies_n, number_of_employees_m):
    min_int = +2147483647
    distribute_goodies_employees.clear();
    goodies_price.sort()
    for i in range(number_of_goodies_n - number_of_employees_m + 1):
        min_int = int(min(min_int,goodies_price[i+number_of_employees_m-1] - goodies_price[i]))
        
    for j in range(0,number_of_employees_m):
        for name,value in goodies_dictionary.items():
            if(int(value) == goodies_price[number_of_employees_m + j]):
                val = form_dictionary_help([name,value])
                final_output.update(val)
            
    return min_int
        
    
    
    
    



goodies_input = open("goodies.txt", "r")
global goodies_dictionary,final_output
goodies_dictionary = {}
goodies_distribute = {}
final_output = {}
distribute_goodies_employees = {}



for line in goodies_input:
    line = line.rstrip("\n");
    lines = line.split(":");
    val = form_dictionary_help(lines);
    goodies_dictionary.update(val)
    
val = (goodies_dictionary.values())
goodies_values = []
for n in val:
    goodies_values.append(int(n))
    
print(goodies_values)

goodies_input.close();
goodies_price = goodies_values
number_of_goodies = len(goodies_price)

#while(True):
output_file = open("goodies_output.txt", "a")
number_of_employees = int(input("Number of employees: "))
output_file.write("Number of Employees : "+ str(number_of_employees))
output_file.write("\n")
output_file.write("Here the goodies that are selected for distribution are: ")
output_file.write("\n")
result = Goodie_function(goodies_price, number_of_goodies, number_of_employees)
    
for name,value in final_output.items():
    output_file.write(name+":"+value)
        
output_file.write("\n")
print("output file written")
output_file.write("and the difference between the choosen goodie with highest and the lowest price is "+str(result))
output_file.write("\n")
output_file.close()
        
    
        
        
        
    
    

    
    
   





	
