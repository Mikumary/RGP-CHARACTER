full_dot = '●'
empty_dot = '○'

def create_character(character_name,strength,intelligence,charisma):
    #*****character name validation****

    #checking if the character is a string 
    if not isinstance(character_name,str):
        return 'The character name should be a string'
    #if the charater is na empty string 
    if  len(character_name)==0:
        return 'the character should have a name'
    if len(character_name)>10:
        return 'The character name is too long'
    #if the character contain spaces 
    if " " in character_name:
        return "The character should ot contain spaces"
    
    #-------state validation------

    stats=[strength,intelligence,charisma]

    #checking if the states are integers 

    for stat in stats:
        if not (isinstance(stat,int)):
            return 'all states should be an integer '
        if (stat < 1):
            return "all states should not be less than one"
        if (stat>4):
            return "all stats should be no more than 4 "
    if sum(stats)!=7:
            return "The character should start with 7 points"
    
    def stat_line(label,value):
        return f"{label} {full_dot * value} {empty_dot * (10-value)}"
    
    return (
        f"{character_name}\n"
        f"{stat_line('STR',strength)}\n"
        f"{stat_line('INT',intelligence)}\n"
         f"{stat_line('CHA',charisma)}"


            )
print(create_character('ren', 4, 2, 1))





