#This file - WorldSeriesWinners.txt  Download WorldSeriesWinners.txtcontains a chronological list of the World Series’ winning teams from 1903 through 2009. 
# The first line in the file is the name of the team that won in 1903, and the last line is the name of the team that won in 2009. 
# (Note the World Series was not played in 1904 or 1994. There are entries in the file indicating this.)


#  Write a program that reads this file and creates a dictionary in which the keys are the names of the teams, 
# and each key’s associated value is the number of times the team has won the World Series.
# 
#  Create another dictionary in which the keys are the years,
#  and each key’s associated value is the name of the team that won that year.The program should prompt the user for a year in the range of 1903 through 2009. 
# It should then display the name of the team that won the World Series that year, and the number of times that team has won the World Series.

def create_worldSeries_dict(): 

    outfile=open('WorldSeriesWinners.txt','r')

    winners=outfile.read().split('\n')

    worldSeries={}

    for i in range(len(winners)):
        worldSeries[winners[i]]=0

    for i in range(len(winners)):
       worldSeries[winners[i]]+=1
    

    outfile.close()





def years_dict(): 
    outfile=open('WorldSeriesWinners.txt','r')

    worldSeriesWinners=outfile.read().split('\n')

    years_won={}
    year=1903

    #print(worldSeriesWinners)

    for i in range(len(worldSeriesWinners)):
        if year!=1904 and year!=1994: 
            years_won[year]=worldSeriesWinners[i]
        if year==1903 or year==1993:
            year+=2
        else:
            year+=1

    print(years_won)

    outfile.close()


def main(): 
    create_worldSeries_dict()
    years_dict()


main()


