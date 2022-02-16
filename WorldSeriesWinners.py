#This file - WorldSeriesWinners.txt  Download WorldSeriesWinners.txtcontains a chronological list of the World Series’ winning teams from 1903 through 2009. 
# The first line in the file is the name of the team that won in 1903, and the last line is the name of the team that won in 2009. 
# (Note the World Series was not played in 1904 or 1994. There are entries in the file indicating this.)


#  Write a program that reads this file and creates a dictionary in which the keys are the names of the teams, 
# and each key’s associated value is the number of times the team has won the World Series.
# 
#  Create another dictionary in which the keys are the years,
#  and each key’s associated value is the name of the team that won that year.The program should prompt the user for a year in the range of 1903 through 2009. 
# It should then display the name of the team that won the World Series that year, and the number of times that team has won the World Series.

def main(): 

    outfile=open('WorldSeriesWinners.txt','r')

    winners=outfile.read().split('\n')

    worldSeries={}

    for i in range(len(winners)):
        worldSeries[winners[i]]=0

    for i in range(len(winners)):
       worldSeries[winners[i]]+=1


    #print(worldSeries)


    years_won={}
    year=1903

    for i in range(len(winners)):
        if year!=1904 and year!=1994: 
            years_won[year]=winners[i]

        if year==1903 or year==1993:
            year+=2
        else:
            year+=1

    #print(years_won)

# The program should prompt the user for a year in the range of 1903 through 2009. 
# It should then display the name of the team that won the World Series that year, and the number of times that team has won the World Series.

    response=float(input("Enter a year from 1903-2009 "))
    if response==1904 or response==1994:
        print('The world series was not played that year')
    else:
        print('The '+years_won[response]+' won the world series that year and they have won the world series '+str(worldSeries[years_won[response]])+' time')
        
    outfile.close()    
main()


