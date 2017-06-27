
import re                                                                                                                                                                    
                                                                                                                                                                             
# the * means match 0 or many of (wo)                                                                                                                                        
batty = re.compile(r'bat(wo)*man')                                                                                                                                           
mo1 = batty.search('I am batman')                                                                                                                                            
print(mo1.group())  # batman                                                                                                                                                 
                                                                                                                                                                             
mo2 = batty.search('there goes batwoman')                                                                                                                                    
print(mo2.group())                                                                                                                                                           
                                                                                                                                                                             
mo3 = batty.search('she is batwowowowowowoman')                                                                                                                              
print(mo3.group())
