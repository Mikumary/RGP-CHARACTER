full_dot = '■'
empty_dot = '□'

def create_profile (name,coding,communication):
    #---name validation----
    if not isinstance(name,str):
        return 'The name should be a string'
    if len(name)==0:
        return "The name should have a value"
    #**** skill validation ******

    skills=[coding,communication]

    if not all(isinstance(skill,int)for skill in skills):
        return 'All skills should be integer'
    if all(skill<1 for skill in skills):
        return 'All skills should be no less than 1'
    if all(skill > 5 for skill in skills):
        return 'All skills should be no more than 5'
    if sum(skills)>6 :
        return "skills should start with 6 points"
    def skills_line(label,value):
        return f"{label}{full_dot*value}{empty_dot *(8 - value)}"
    return(
        f"{name}\n"
        f"{skills_line("COD",coding)}\n"
        f"{skills_line("COM",communication)}\n"

    )
print (create_profile("miku",4,2))