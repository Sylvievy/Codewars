'''
Cat years, Dog years
8kyu
10 d ago
'''

def human_years_cat_years_dog_years(human_years):
    cy,dy=0,0
    if human_years==1:
        cy,dy=15,15
    elif human_years==2:
        cy,dy=24,24
    elif human_years>2:
        cy=24+4*(human_years-2)
        dy=24+5*(human_years-2)
        

    
    return [human_years,cy,dy]
