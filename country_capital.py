"""
Input data containing N countries and their capital will be provided as input.
The program must then print the capital for a given country.
Input Format:First line will contain the integer value N representing how many
country-capital pairs are to be provided as input.Next N lines will contain the name of the country
and the name of the captial as string values separated by a space.The last line will contain the name
of the country as a string value for which the capital is to be printed as output.
Output Format:First line will contain the capital of the country.
If the name of the country is NOT found in the input data then NONE must be printed as output.
Constraints:N will be from 2 to 100.
Sample Input/Output:Example 1:
Input:
5
Afghanistan Kabul
Austria Vienna
Armenia Yerevan
Chile Santiago
Croatia Zagreb
Austria
Output:
Vienna
Example 2:
Input:
4
Armenia Yerevan
Chile Santiago
Croatia Zagreb
Iran Tehran
Japan
Output:NONE
Explanation:
As Japan is not mentioned in the input data, NONE is printed as output.
"""
code:
n=int(input())
l=[]#list for storing both country and capital name
non=[]#list for storing only country name
for i in range(n):
    x,y=map(str,input().split())
    l.append([x,y])
    non.append(x)
cname=input()
f=0
for i in range(len(l)):
    if cname not in non:
        f=1
        break
    elif cname==l[i][0]:
        print(l[i][1])
        break
if f==1:
    print("NONE")
