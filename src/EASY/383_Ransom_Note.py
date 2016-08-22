## 383. Ransom Note(EASY)
## Given  an  arbitrary  ransom  note  string  and  another  string  containing  letters
## from  all  the  magazines,  write  a  function  that  will  return  true  if  the  ransom
## note  can  be  constructed  from  the  magazines ;  otherwise,  it  will  return  false.   
##
## Each  letter  in  the  magazine  string  can  only  be  used  once  in  your  ransom  note.
##
## Note:
## You may assume that both strings contain only lowercase letters.
##
## canConstruct("a", "b") -> false
## canConstruct("aa", "ab") -> false
## canConstruct("aa", "aab") -> true

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_dict = {}
        for letter in magazine:
            if letter not in magazine_dict:
                magazine_dict[letter] = 1
            else:
                magazine_dict[letter] += 1
        for letter in ransomNote:
            if letter not in magazine_dict or magazine_dict[letter] == 0:
                return False
            else:
                magazine_dict[letter] -= 1
        return True
