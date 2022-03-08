import os
"""
    A file which contains methods to find a given file that meets 3 fixed conditions.
    
    ...
    
    Methods
    -------
    owner_is_admin(file_path)
        Returns 'True' if the given file is owned by "admin" user, 'False' otherwise. It is compared with the proper value in the fixed requirements dictionary.
    file_is_executable(file_path)
        Returns 'True' if the given file is executable, 'False' otherwise. It is compared with the proper value in the fixed requirements dictionary.
    size_is_acceptable(file_path)
        Returns 'True' if the given file size is lower than 14*2^20, 'False' otherwise. It is compared with the proper value in the fixed requirements dictionary.
    verify_requirements(file_path)
        Returns 'True' if the 3 methods explained above are 'True', so it verifies that all requirements are met.
    find_first_expected_file(file_path)
        Given a path, this function iterates the files contained in that path and finds the first one which meets the following requirements:
            - is owned by "admin" user
            - is executable
            - is lower than 14*2^20
    """

def owner_is_admin(file_path):  
    return True if os.stat(file_path).st_uid == requirements["file_owner"] else False
    
def file_is_executable(file_path):  
    return True if os.access(file_path, os.X_OK) == requirements["file_executable"] else False
    
def size_is_acceptable(file_path):  
    return True if os.path.getsize(file_path) < requirements["max_file_size"] else False
    
def verify_requirements(file_path):  
    return True if owner_is_admin(file_path) and file_is_executable(file_path) and size_is_acceptable(file_path) else False
    
def find_first_expected_file (file_path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            file_meets_requirements = verify_requirements (file_path)
            if (file_meets_requirements):
                print ("\n" + filename + " is the first file that meets all the requirements.")
                break
            else:
                print ("No files meet all the requirements.")
    return filename

requirements = {
        "file_owner":0,
        "file_executable":True,
        "max_file_size":14680064
    }

#path = "D:/USUARIO/Descargas/ProvaWB/ProvaWB/Ex2"
path = input("\nInput the directory absolute path where the files are contained: ")
find_first_expected_file (path)



