# Recursive String Replacement:
#     Given a string (input), let's write a function to replace a substring (key) with a different substring (value).
#     e.g.  Given String (input) : 'abcpipipit', replace all instances of 'pi' with '3.14'.
#     So, expected output is: 'abc3.143.143.14t'

# Executed on Python 3.7.6

class StringReplacementRecursive:
    def recursive_replacement(self, input: str, key: str, value: str) -> str:
        result = ""
        return self.recursive_replace(input, 0, key, value, "", result)

    def recursive_replace(self, input:str, index: int, key: str, value: str, temp: str, output: str):
        literal = input[index]
        temp += literal

        if key[:len(temp)] == temp:
            if len(temp) == len(key):
                output += value
                temp = ""
        else:
            output += temp
            temp = ""

        if index == len(input)-1:
            output += temp
            return output
        else:
            return self.recursive_replace(input, index+1, key, value, temp, output)


obj = StringReplacementRecursive()
obj.recursive_replacement('abcpipipit', 'pi', '3.14')

# OUTPUT
# 'abc3.143.143.14t'
