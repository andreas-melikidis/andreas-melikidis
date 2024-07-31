def descending_order():
    
    import array as XXX
    m = XXX.array('d', [3 , 4, 23, 7, -24])    

    change = True

    while change:
        change = False
        for i in range(0,4):
           
            for j in range(i+1,5):
                
                if m[j] > m[i]:
                    m[j],m[i] = m[i],m[j]
                    
                    change = True
            
                
            
        
    print(m[0],"\t",m[1],"\t",m[2],"\t",m[3],"\t",m[4])
        
descending_order()