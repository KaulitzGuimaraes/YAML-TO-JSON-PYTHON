import yaml
import json
import os
'''
:author: Kaulitz.Guimaraes@ibm.com
'''
class PropertyFiles() :

    def get_files_from_dir(self):
        '''
        This method get all files from current dir and returns a list with files name.
        :return: list
        '''
        files = os.listdir("./")
        for file in files:
            file_n,extension = self.get_file_name_only(file)
            if (extension != 'yml'):
                files.remove(file)
        return files

    def read_file(self,file_name):
        '''
        This method returns the content from file given by parameter
        :param file_name:
        :return: str
        '''
        return  open(file_name,'r')




    def get_file_name_only(self,file_name):
        '''
        This method returns the file name without the extension.
        :param file_name:
        :return: str
        '''
        pieces =  file_name.split(sep='.')
        return pieces[0],pieces[1]


class JsonsFilesCreator :
    '''
    This class creates a json by a yaml given
    '''
    def __init__(self):
        '''
        Class constructor
        '''
        self.ppt_files = PropertyFiles()
        self.files = self.ppt_files.get_files_from_dir()
    def  create_json_per_file(self) :
        '''
        This method creates a json for each files founded.
        :return: void
        '''
        for file in self.files:
            try:
                file_name, content = self.get_content(file)
                self.create_json_file(file_name,content)
            except Exception :
                pass
    def get_content(self, file):
        '''
        This method get tje content from file given by parameter
        :param file: str
        :return: str,str
        '''
        content = self.ppt_files.read_file(file)
        file_name, ex = self.ppt_files.get_file_name_only(file)
        return file_name, content
    def create_json_file(self,file_name,content):
        '''
        This method creates the json file by content and name given
        :param file_name: str
        :param content: str
        :return: str
        '''
        self.yaml_to_json(content,file_name)

    def yaml_to_json(document,file_name) :
        '''
        This method parse the yaml to a json
        :param document: str
        :param file_name: str
        :return:
        '''
        s = yaml.load(document)
        js = json.dumps(s, indent=4, sort_keys=True, ensure_ascii=False)
        open(file_name + ".json", 'w').write(js)



if __name__ == '__main__' :
    '''
     Main method
    '''
    creator = JsonsFilesCreator()
    creator.create_json_per_file()
