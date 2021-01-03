def solution(l):
    all_pairs = []
    x = 1
    
    tmp = 0
    template_list = [0]
    while True:
        while True:
            tmp = l-x
            if x < tmp:
                temp_list = template_list + [tmp,x]
                x +=1
            else:
                break
            all_pairs.append(temp_list)
         
        template_list.append(template_list[-1] + 1)
        l -= template_list[-1]
        x = template_list[-1] + 1
        if(len(all_pairs[-1]) > l):
            break

    for pair in all_pairs:
        if len(pair) > 4:
            
    
    for step in all_pairs:
        print(sorted(step))
        
    all_pairs.sort()
    return len(all_pairs)
    

if __name__ == "__main__":
    brick = int(input("number of bricks: "))
    tmp = solution(brick)