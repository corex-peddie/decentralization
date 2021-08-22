from HashMap import HashMap
from datetime import datetime
from predict import model_prediction
import time

class Script:
    elements = []
    database = HashMap(1000)
    
    def script(self):
        print("Here are the following commands: ".title())
        print("/feedback: To recieve feedback on your design")
        print("/view_versions: To see various version(s) of your design")
        print("/delete: To delete a design from the program")
        print("/quit: To quit the program")
        print('-'*24)
        playing = True 
        while playing:
            print()
            prompt = str(input(':'))

            if prompt == '/feedback' or prompt == '/feedback ':
                design = str(input("Please enter a name for your design: "))
                current_date = datetime.now().strftime("%m/%d/%y, %H:%M:%S")
                self.elements.append(design)
                web_status = model_prediction()
                self.database.setter(design, [current_date, web_status])
                time.sleep(0.2)
                print("loading...")
                time.sleep(0.3)
                print('...')
                time.sleep(0.3)
                print('...')
                time.sleep(0.3)
                print("Your design has been successfully added to the database!")
            
            elif prompt == '/view_versions':
                design = str(input("Please enter a name for your design: "))
                if not design in self.elements:
                    print("That design does not seem to be registered under this database")
                    time.sleep(0.2)
                    print("You might have to add it to the program with \"/feedback\".")
                else:
                    self.database.retrieve(design)

            elif prompt == "/delete":
                design = str(input("Please enter a name for your design: "))
                if not design in self.elements:
                    print("That design does not seem to be registered under this database")
                    time.sleep(0.2)
                else:
                    print("Please wait as we are deleting your design from our database")
                    time.sleep(0.3)
                    print("loading...")
                    time.sleep(0.3)
                    print('...')
                    time.sleep(0.3)
                    print('...')
                    self.database.delete(design)
                    self.elements.remove(design)
                    time.sleep(0.3)
                    print("Your design, \"{design}\", has been succesfully deleted from our program".format(design=design))

            elif prompt == "/quit":
                break
            else:
                print("That command does not seem valid")
                
                

script = Script()

print(script.script())

                
            
            

        
