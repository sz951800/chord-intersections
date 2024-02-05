def num_intersections(input1):
    radians=input1[0]
    identifiers=input1[1]
    
    chords={}
    
    for i in range(len(radians)):
        
        point_id = identifiers[i]
        
        try:
            chords[point_id[1:]].append(radians[i])
        except KeyError:
            chords[point_id[1:]]=[]
            chords[point_id[1:]].append(radians[i])
            
    
    for i in chords:
        chords[i]=sorted(chords[i])

    num_intersections = 0
    chord_list=[]

    for i in chords:
        chord_list.append(chords[i])
    
    
    for i in range(len(chord_list)):
        c1_start=chord_list[i][0]
        c1_end=chord_list[i][1]
        
        for j in range(i+1,len(chord_list)):
            c2_start=chord_list[j][0]
            c2_end=chord_list[j][1]
            
            if (c1_start <= c2_start <= c1_end) ^ (c1_start <= c2_end <= c1_end):
                num_intersections += 1
                
    return num_intersections