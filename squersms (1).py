while(True):

    choice=int(input('''
    1] convert text to code 

    2] convert code to text

    enter your choice :  '''))

    if(choice==1):
        import random
        ran=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        text_input=str(input("\nenter text to create code:") )
        a=0;
        code=""
        newrand=""
        condi=4;
        while(a<len(text_input)):
            ind=text_input[a]
    
            if(condi==4):
                rand=random.choice(ran)
                code=code+ind+rand

                rand=random.choice(ran)
                code=code+rand

                rand=random.choice(ran)
                code=code+rand
      
                rand=random.choice(ran)
                code=code+rand
   
                condi=6;

            elif(condi==6):
  
                rand=random.choice(ran)
                code=code+ind+rand

                rand=random.choice(ran)
                code=code+rand

                rand=random.choice(ran)
                code=code+rand
      
                rand=random.choice(ran)
                code=code+rand

                rand=random.choice(ran)
                code=code+rand
      
                rand=random.choice(ran)
                code=code+rand
        
                condi=5;
        
            elif(condi==5):
                rand=random.choice(ran)
                code=code+ind+rand
    
                rand=random.choice(ran)
                code=code+rand

                rand=random.choice(ran)
                code=code+rand
      
                rand=random.choice(ran)
                code=code+rand

                rand=random.choice(ran)
                code=code+rand

                condi=3
        
            elif(condi==3):
    
                rand=random.choice(ran)
                code=code+ind+rand

                rand=random.choice(ran)
                code=code+rand

                rand=random.choice(ran)
                code=code+rand
       
                condi=4;
        
        
        
            a=a+1;
    
        print("\ntext in code format : ",code)

    if(choice==2):
        text=input("\nenter code :")

        text_code="";
        a=0
        l=len(text)
        l=l-1

        while(a<=l):
            if(a<l):
                ind=text[a]
                text_code=text_code+ind
                a+=5;

            if(a<l):
                ind=text[a]
                text_code=text_code+ind
                a+=7;
    
            if(a<l):
                ind=text[a]
                text_code=text_code+ind
                a+=6;

            if(a<l):
                ind=text[a]
                text_code=text_code+ind
                a+=4;


    
    
        print("\ncode in text format:",text_code)
    
