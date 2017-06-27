
import re                                                                                                                                                                    
                                                                                                                                                                             
# the + means match at least 1 of whatever is in the parens
batty = re.compile(r'bat(wo)+man')                                                                                                                                           

mo1 = batty.search('I am batman')                                                                                                                                            
print(mo1 == None)  # batman                                                                                                                                                 
                                                                                                                                                                             
mo2 = batty.search('there goes batwoman')                                                                                                                                    
print(mo2.group())                                                                                                                                                           
                                                                                                                                                                             
mo3 = batty.search('she is batwowowowowowoman')                                                                                                                              
print(mo3.group())
