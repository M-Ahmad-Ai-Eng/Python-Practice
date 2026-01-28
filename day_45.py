import import_file    

import_file.greet() 

# if you run this file you see that "hello you open the file" 
# and if you add the {if __name__ == "__main__":}
# before the function call and after the function code
# so you could not see that greet() double in your output
# that is help full to use in the files because if you import the module and they are suddenly execute in your machine and might be this code is so complex or harmful for your computer and may cause some issue.
# in code the "__name__" reffers to the file path like is it the main file in which the code be executed or that is imported for some one other module
# if the code run in file that have import the module and we run it so python interpreter simply change the "__main__" to the module name like the import_file or some thing like that.
# conclusion:
# if we add this code into our file which will be imported and we don't want to run the function so we use that to avoide the self execution in the main file in which that is imported.