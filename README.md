# NokeLock-CVE-test
NokeLcok can Modify other people’s information without authority, and even gain complete control of other people’s accounts  
There is a function to modify personal information in the application, as shown below：  

![image](https://user-images.githubusercontent.com/48674419/109612451-b4807780-7b6a-11eb-802d-fe0af6d77db3.png)  
Requets is:  
![image](https://user-images.githubusercontent.com/48674419/109612520-ceba5580-7b6a-11eb-9b25-63eb58860a18.png)  
Send request can get Response,the response is:  

![image](https://user-images.githubusercontent.com/48674419/109612622-fb6e6d00-7b6a-11eb-96e5-87f706a209da.png)

User nickname modified successfully,and we can get the userId and password,if we modified the value of userId from request,we will get the information of other users：  



It is found that the data is encrypted using MD5, and the rainbow table is used to obtain the password inscription：  
![image](https://user-images.githubusercontent.com/48674419/109613224-d3cbd480-7b6b-11eb-9544-ec0bf4ad0dbd.png)
