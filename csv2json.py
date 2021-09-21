import json

filename = 'basic_science_jss3.csv'

output = { }
outputs = []
#print(filename)
with open(filename) as f:
    for line in f:
        
        QUESTION, ANSWER, OPTIONA, OPTIONB, OPTIONC, OPTIOND, OPTIONE, SCORES = line.strip().split(',', 7)
        
        output['QUESTION'] = QUESTION.strip()
        output['ANSWER'] = ANSWER.strip()
        options = [] 
        options.append(OPTIONA)
        options.append(OPTIONB)
        options.append(OPTIONC)
        options.append(OPTIOND)
        options.append(OPTIONE)
        output['options'] = options
        output['score'] = SCORES.strip()
        outputs.append(output)
        


        
        
       

        #Create a json file and write into it
        output_json = open('basic_science_jss3.json', 'w')
        json.dump(outputs, output_json, indent = 4, sort_keys= False)
        output_json.close()
