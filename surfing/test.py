# import phonenumbers
# from phonenumbers import geocoder

# phone_number1= phonenumbers.parse("+91-9137413087")

# print("\nPhone number location:")
# print(geocoder.description_for_number(phone_number1,"en"))

class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if a>0 | b>0 and flag==False:
            return True
        elif a<0 and b<0 and flag==True:
            return True
        else:
            return False
        
print("")
var,var1,var2 = 1,2,3
print (var)
print (var1, var2 )