# Pattern program intervoew question
"""
         *
        * *
       * * *
      * * * *
     * * * * *
    * * * * * *
   * * * * * * *
  * * * * * * * *
 * * * * * * * * *
* * * * * * * * * *
"""


n=10
c=(2*n-1)
initial_count=((c+1)/2)-1
# print(initial_count)
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1:
            s=" "*int(initial_count)+"*"
            print(s,end="")
        else:
            # print("code reached to else")
            s=" "+"*"
            print(s,end="")
    print()
    initial_count = initial_count -1
