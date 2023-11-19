import os
import re

def search_files(directory, pattern):
   matches = []
   
   # Walk through each subfolder and file in the directory
   for root, _, files in os.walk(directory):
       for file_name in files:
           file_path = os.path.join(root, file_name)
           
           with open(file_path, "r",encoding="utf-8",errors = "ignore") as file:
               content = file.read()
               
               # Search for the pattern using regular expressions
               found_matches = re.findall(pattern, content)
               
               if found_matches:
                  matches.append((file_path, found_matches))
   
   return matches

def find_non_matching_files(directory, pattern1, pattern2, pattern3,pattern4):
   non_matching_files = []
   
   # Walk through each subfolder and file in the directory
   for root, _, files in os.walk(directory):
       for file_name in files:
           file_path = os.path.join(root, file_name)
           
           with open(file_path, "r",encoding="utf-8",errors = "ignore") as file:
               content = file.read()
               
               # Search for the patterns using regular expressions
               found_matches1 = re.findall(pattern1, content)
               found_matches2 = re.findall(pattern2, content)
               found_matches3 = re.findall(pattern3, content)
               found_matches4 = re.findall(pattern4, content)
               found_matches5 = re.findall(pattern5, content)

               if not found_matches1 and not found_matches2 and not found_matches3 and not found_matches4 and not found_matches5:
                  non_matching_files.append(file_path)
   
   return non_matching_files

directory_to_search = "."
pattern_to_search = r"URL:\s*(.*?)\n.*?Username:\s*(.*?)\n.*?Password:\s*(.*?)\n"
pattern_to_search2 = r"Host:\s*(.*?)\n.*?Login:\s*(.*?)\n.*?Password:\s*(.*?)\n"
pattern_to_search3 = r"SOFT:\s*(.*?)\n.*?URL:\s*(.*?)\n.*?USER:\s*(.*?)\n"
pattern_to_search4 = r"url:\s*(.*?)\n.*?login:\s*(.*?)\n.*?password:\s*(.*?)\n"
pattern_to_search5 = r"URL:\s*(.*?)\n.*?Login:\s*(.*?)\n.*?Password:\s*(.*?)\n"



result = search_files(directory_to_search , pattern_to_search )
result2 = search_files(directory_to_search , pattern_to_search2 )
result3 = search_files(directory_to_search , pattern_to_search3 )
result4 = search_files(directory_to_search , pattern_to_search4 )
result5 = search_files(directory_to_search , pattern_to_search5 )

# Write results to a text file
with open("credentials.txt", "w",encoding="utf-8",errors = "ignore") as output_file:
   for path, matches in result :
       #output_file.write(f"File: {path}\n")
       
       for match in matches:
           url, username ,password = match
           
           # Remove leading/trailing spaces (if any)
           url = url.strip()
           username = username.strip()
           password = password.strip()
           credential_line = f"{url}:{username}:{password}\n"
           output_file.write(credential_line)
   for path, matches in result2 :
       #output_file.write(f"File: {path}\n")
       
       for match in matches:
           url, username ,password = match
           
           # Remove leading/trailing spaces (if any)
           url = url.strip()
           username = username.strip()
           password = password.strip()
           credential_line = f"{url}:{username}:{password}\n"
           output_file.write(credential_line)
   for path, matches in result3 :
       #output_file.write(f"File: {path}\n")
       
       for match in matches:
           url, username ,password = match
           
           # Remove leading/trailing spaces (if any)
           url = url.strip()
           username = username.strip()
           password = password.strip()
           credential_line = f"{url}:{username}:{password}\n"
           output_file.write(credential_line)
   for path, matches in result4 :
       #output_file.write(f"File: {path}\n")
       
       for match in matches:
           url, username ,password = match
           
           # Remove leading/trailing spaces (if any)
           url = url.strip()
           username = username.strip()
           password = password.strip()
           credential_line = f"{url}:{username}:{password}\n"
           output_file.write(credential_line)
   for path, matches in result5 :
       #output_file.write(f"File: {path}\n")
       
       for match in matches:
           url, username ,password = match
           
           # Remove leading/trailing spaces (if any)
           url = url.strip()
           username = username.strip()
           password = password.strip()
           credential_line = f"{url}:{username}:{password}\n"
           output_file.write(credential_line)



# Find non-matching files
non_matching_files = find_non_matching_files(directory_to_search, pattern_to_search, pattern_to_search2,pattern_to_search3,pattern_to_search4,pattern_to_search5)

# Write non-matching files to a text file
with open("non_matching_files.txt", "w",encoding="utf-8",errors = "ignore") as output_file:
   for file_path in non_matching_files:
      output_file.write(f"{file_path}\n")


